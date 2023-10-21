/* Script that fetches and list the title for all movies */

$(document).ready(function() {
    // Wait until document is ready
  
    $.get("https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
      const films = data.results; // get data
  
      films.forEach(film => {
        const li = $("<li>").text(film.title); // Create element <li>
        $("#list_movies").append(li); // Add <li> to the list
      });
    })
    .fail(function(error) {
      console.error("Error:", error);
    });
  });
  