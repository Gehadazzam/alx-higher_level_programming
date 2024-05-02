$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json')
    .done(function (data) {
      $('#character').text(data.name);
    })
    .fail(function () {
      $('#character').text('Error fetching character name.');
    });
});
