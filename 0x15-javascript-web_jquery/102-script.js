$(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/';
  $('#btn_translate').click(function () {
    const language = $('#language_code').val();
    $.get(url, { lang: language }, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
