/* Script add li element to list when click */

$(document).ready(function() {
    // Wait until document is ready

    $("DIV#add_item").click(function() {
        $("UL.my_list").append("<li>Item</li>"); //add to the list
    });
});