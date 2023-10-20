/* Fetch and displays the value of hello */

$(document).ready(function() {
    // Wait until document is ready
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
      const helloValue = data.hello;
      $("DIV#hello").text(helloValue); //show data name in screen
    })
    .fail(function() {
        console.error("Error:", error);
    });
});