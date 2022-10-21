// navbar
let buttonShowLi = document.getElementById("show-all-li");
let navUl = document.querySelector("header ul");

buttonShowLi.onclick = function () {
    if(navUl.style.display == "flex")
        navUl.style.display = "none";
    else
        navUl.style.display = "flex";
}