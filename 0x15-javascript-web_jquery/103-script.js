$(document).ready(function () {
  $('#btn_translate').click(fetchTranslation);
  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // Enter key pressed
      fetchTranslation();
    }
  });

  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode })
      .done(function (data) {
        $('#hello').text(data.hello);
      })
      .fail(function () {
        $('#hello').text('Error fetching translation.');
      });
  }
});
