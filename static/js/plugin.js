$(function () {

    $(".js-create-order").click(function () {
      $.ajax({
        url: '/order/create/',
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-order").modal("show");
        },
        success: function (data) {
          $("#modal-order .modal-content").html(data.html_form);
        }
      });
    });
  
  });