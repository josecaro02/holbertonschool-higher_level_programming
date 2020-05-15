$(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(url, function (data) {
    for (let i = 0; i < data.results.length; i++) {
      const res = data.results;
      $('#list_movies').append('<li>' + res[i].title + '</li>');
    }
  });
});
