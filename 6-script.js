/* Updates the text of the header when click */

$(document).ready(function() {
    // Wait until document is ready

    $("DIV#update_header").click(function() {
        $("header").text("New Header!!!"); //change text
    });
});