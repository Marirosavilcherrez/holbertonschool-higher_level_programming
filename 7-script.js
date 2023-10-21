/* Script that fetches character name from URL */

$(document).ready(function() {
    // Wait until document is ready
    $.get("https://swapi-api.hbtn.io/api/people/5/?format=json", function(data) {
      const element = data.name; //get name data
      
    $("DIV#character").text(element); //show data name in screen
    })
    .catch(error => {
        console.error("Error:", error);
    });
});