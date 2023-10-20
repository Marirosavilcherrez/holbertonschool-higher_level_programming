/* toggles the class of header element when click the tag */

$(document).ready(function() {
    // Wait until document is ready

    $("DIV#toggle_header").click(function() {
        let header = $("header");
        
        if (header.hasClass("red")) { //verify if the class is red
          header.removeClass("red").addClass("green");
        } else {
          header.removeClass("green").addClass("red");
        }
    });
});