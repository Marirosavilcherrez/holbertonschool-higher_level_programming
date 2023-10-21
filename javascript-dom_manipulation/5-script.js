//Update the text of the header when the ser click the element

const element = document.getElementById("update_header");

//Call to action
element.addEventListener("click", function(){
    //get text of the header
    const header = document.querySelector("header");

    //update the text
    header.textContent = "New Header!!!";
})
