$('.submit').click(function () {
  $.ajax({
          url: 'localhost/set_user',
          data: {username: $('.my-input').val()},
          success: function (data) {
              alert('ok');
          }
        });

  console.log($('.my-input').val());
});