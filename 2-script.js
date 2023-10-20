/* Updates the text color header when click */

$(document).ready(function() {
    // Wait until document is ready
    $("DIV#red_header").click(function() {
      $("header").css("color", "red");
    });
  });