//Adds the class to the header when click on the tag

const element2 = document.getElementById("red_header")

element2.addEventListener("click", function(){
    //Select the header
    const header = document.querySelector("header")
    

    //Add the class to the header
    header.classList.add("red");
});
