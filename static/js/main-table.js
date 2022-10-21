let tr = document.querySelectorAll(".main-table tbody tr");

tr.forEach(function (e) {
    if(e.lastElementChild.innerHTML == "add"){
        e.style.backgroundColor = "#eafbf9";
        e.style.color = "#2c4755";
        e.lastElementChild.innerHTML="إضافة";
    }else {
        e.style.backgroundColor = "";
        e.style.color = "#2c4755";
        e.lastElementChild.innerHTML="سحب";
    }

})