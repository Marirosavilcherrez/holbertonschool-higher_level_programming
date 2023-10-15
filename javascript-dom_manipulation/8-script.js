//Fetch and display the value from the HTML

fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then(response => response.json())
    .then(data => {
        const translation = data.hello;
        const helloElement = document.getElementById("hello");
        helloElement.textContent = translation;
    })

    .catch(error => {
        console.error('Error:', error);
      });
