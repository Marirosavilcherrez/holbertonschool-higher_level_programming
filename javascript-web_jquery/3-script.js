/* Add the class red to the header element when click */

$(document).ready(function() {
    // Wait until document is ready
    $("DIV#red_header").click(function() {
      $("header").addClass("red"); //add class
    });
  });