from PIL import Image
import numpy as np
import cv2


def CompareChars(img):
    maps = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
            6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
            12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H',
            18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N',
            24: 'O', 25: 'P', 26: 'Q',27: 'R', 28: 'S', 29: 'T',
            30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}
    results = []
    img2 = img
    compare = np.load("emnist.npy")
    for i in compare:
        img1 = i*255
        to_bin = lambda img: (img > 127).astype(np.uint8)
        img_1, img_2 = list(map(to_bin, [img1, img2]))

        img_1x, img_1y = np.where(img_1 == 1)
        img_1 = img_1[np.amin(img_1x):np.amax(img_1x)+1, np.amin(img_1y):np.amax(img_1y)+1]

        img_2x, img_2y = np.where(img_2 == 1)
        img_2 = img_2[np.amin(img_2x):np.amax(img_2x)+1, np.amin(img_2y):np.amax(img_2y)+1]

        ##plt.imshow(img_1, cmap='gray', vmin=0, vmax=1)
        ##plt.show()

        scale = min([img_1.shape[1], img_2.shape[1]]), min([img_1.shape[0], img_2.shape[0]])

        img_1 = cv2.resize(img_1, scale, interpolation=cv2.INTER_AREA).astype(np.int8)
        img_2 = cv2.resize(img_2, scale, interpolation=cv2.INTER_AREA).astype(np.int8)

        img_1x, img_1y = np.where(img_1 == 1)
        img_2x, img_2y = np.where(img_2 == 1)

        img_1a, img_1b = int(img_1x.mean()), int(img_1y.mean())
        img_2a, img_2b= int(img_2x.mean()), int(img_2y.mean())

        d, f = img_1.shape
        g, h = img_2.shape

        if img_1a <= img_2a:
            img_1x1 = img_2a - img_1a
            img_1x2 = img_1x1 + d
            
            img_2x1, img_2x2 = 0, g
            
        else:
            img_2x1 = img_1a - img_2a
            img_2x2 = img_2x1 + g
            
            img_1x1, img_1x2 = 0, d
            

        if img_1b <= img_2b:
            img_1y1 = img_2b - img_1b
            img_1y2 = img_1y1 + f
            
            img_2y1, img_2y2 = 0, h
            
        else:
            img_2y1 = img_1b - img_2b
            img_2y2 = img_2y1 + h
            
            img_1y1, img_1y2 = 0, f
            
        r = max((img_1x2, img_2x2))
        c = max((img_1y2, img_2y2))

        img_n1 = np.zeros((r, c), dtype=np.int8)
        img_n1[img_1x1:img_1x2, img_1y1:img_1y2] = img_1
        img_n2 = np.zeros((r, c), dtype=np.int8)
        img_n2[img_2x1:img_2x2, img_2y1:img_2y2] = img_2

        img_b = img_n2.copy()
        img_b[img_n1 == 0] = 0

        z1 = 1 - abs(img_b - img_n1).mean()
        z2 = 1 - abs(img_b - img_n2).mean()
        z3 = 1 - abs(img_n2 - img_n1).mean()

        similarity_ratio = (z1 + z2 + z3)/3
        results.append(similarity_ratio)
    return maps[results.index(max(results))]
