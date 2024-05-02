$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .done(function (data) {
      $('#hello').text(data.hello);
    })
    .fail(function () {
      $('#hello').text('Error fetching translation.');
    });
});
