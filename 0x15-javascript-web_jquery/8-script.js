$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json')
    .done(function (data) {
      const movies = data.results;
      const list = $('#list_movies');
      $.each(movies, function (index, movie) {
        list.append('<li>' + movie.title + '</li>');
      });
    })
    .fail(function () {
      $('#list_movies').text('Error fetching movie titles.');
    });
});
