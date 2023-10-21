//Toggles class when click tag id

const element = document.getElementById("toggle_header")

element.addEventListener("click", function(){
    const header = document.querySelector("header");

    //conditional if the color is red or green
    if (header.classList.contains("red")) {
        header.classList.remove("red");
        header.classList.add("green");
        
    } else {
        header.classList.remove("green");
        header.classList.add("red");
    }
});
