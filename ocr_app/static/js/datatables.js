// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#customerTable').DataTable( {
        responsive: true,
        "order": [[ 0, "asc" ]],
        stateSave: true,
        "scrollY": "350px",
        "scrollCollapse": true,
        "scrollX": true,
        "lengthMenu": [[5, 25, 50, -1], [5, 25, 50, "All"]],
//        serverSide: true,
//        ajax: '/data-source'
    } );

    var table = $('#customerTable').DataTable();
    $('#customerTable tbody').on('click', 'tr', function () {
//        console.log( table.row( this ).data() );
        var data = table.row( this ).data();
//        alert( "You clicked on "+data[0]+"\'s row" );
        window.location = 'customer_profile'
    });


    var table = $('#customerTable').DataTable();
    $('#customerTable tbody').on('click', 'tr', function () {
        $.ajax({
            type: "POST",
            url: "/customer_profile",
            data: {
                id: $table.row( this ).data()[0]
            },
//            .done(function(data) {
//               if (response.d == true) {
//                    window.location.replace("customer_profile")
//                }
//            )},
        });
    });
});