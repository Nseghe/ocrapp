from ubuntu:latest

RUN apt-get update --fix-missing
RUN apt-get --yes install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get --yes install build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel
RUN apt-get update && apt-get --yes install openalpr openalpr-daemon openalpr-utils libopenalpr-dev

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

RUN apt-get update && apt-get --yes install locales && locale-gen en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV FLASK_APP run

CMD ["flask", "run", "--port=5000"]

