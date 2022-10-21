let category = document.getElementById("category");
let itemSelector = document.getElementById("items");
let pCount = document.querySelector("p.count");
let items = document.querySelectorAll(`select[name="items"] option`);
let error = document.querySelector(".error");

window.onload = (_) => document.querySelector(`select[name="items"]`).style.display = "none";

// category selector change
category.addEventListener("change", function (){
    let acitveItems = document.querySelectorAll(`select[name="items"] option[category="${this.options[this.selectedIndex].getAttribute('category')}"]`)
    document.querySelector(`select[name="items"]`).style.display = "block";
    
    items.forEach(function (e) {
        let active = false;

        acitveItems.forEach(
            (e2) => {
                if(e == e2) active = true;
                });
                
        if(active || e.value == "") e.style.display = "block";
        else e.style.display = "none";
    });

    document.querySelector(`select[name="items"] option:first-child`).selected = true;
});

// items selecteor change
itemSelector.addEventListener("change", function (e){
    pCount.textContent = itemSelector.options[itemSelector.selectedIndex].getAttribute("count");
});

const form = document.getElementsByTagName("form")[0];

form.addEventListener('submit', event => {
    if(event.submitter.name === "remove" && parseInt(pCount.textContent) < parseInt(document.getElementsByName("count")[0].value)){
        error.textContent = "الرقم الي عم تسحبة اقل من الموجود!!"
        event.preventDefault();
    }
});
