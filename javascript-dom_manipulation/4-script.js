//Add a li eleemnt when click id

document.addEventListener("DOMContentLoaded", function () {
    // Get a reference to the "add_item" element
    const addItemButton = document.getElementById("add_item");
  
    // Get a reference to the <ul> element with class "my_list"
    const myList = document.querySelector(".my_list");
  
    // Add a click event listener to the "add_item" element
    addItemButton.addEventListener("click", function () {
      // Create a new <li> element
      const newItem = document.createElement("li");
      newItem.textContent = "Item"; // Set the text content of the new element
  
      // Append the new <li> element to the <ul> element
      myList.appendChild(newItem);
    });
  });
