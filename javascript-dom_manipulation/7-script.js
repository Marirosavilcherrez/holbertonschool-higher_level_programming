//Fetch and list the title by using URL

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then(response => response.json())
  .then(data => {
    const titleElement = document.getElementById("list_movies");
    const films = data.results;

    const ul = document.createElement("ul");

    films.forEach(film => {
      const li = document.createElement("li");
      li.textContent = film.title;
      ul.appendChild(li);
    });

    titleElement.appendChild(ul);
  })

  .catch(error => {
    console.error('Error:', error);
  });
