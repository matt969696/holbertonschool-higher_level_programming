window.addEventListener('DOMContentLoaded', (event) => {
  $('input#btn_translate').click(function () {
    const language = $('input#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/?lang=' + language;
    $.get(url, function (data, textStatus) {
      $('div#hello').text(data.hello);
    });
  });
});