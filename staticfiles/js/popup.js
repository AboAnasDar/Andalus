let mainPopup = document.getElementsByClassName("delete-popup")[0];
let closePopup = document.getElementsByClassName("close")[0];
let cancel = document.getElementsByClassName("cancel")[0];
let deleteItem = document.getElementsByClassName("delete")[0];
let btnRemove = document.getElementsByClassName("remove");
let spanName = document.getElementsByClassName("item-name")[0];
let btnReomveValue = "";

Array.from(btnRemove).forEach(btn => {
        btn.onclick = function () {
            mainPopup.style.display = "block";
            btnReomveValue = btn.getAttribute("page-del");
            spanName.textContent = btn.getAttribute("text");
        }
    }
);

deleteItem.onclick = _ => {
  deleteItem.setAttribute("href", btnReomveValue);
}

// popup display none
closePopup.onclick = _ => popupNone();
cancel.onclick = _ => popupNone();
window.onclick = function(event) {
  if (event.target == mainPopup) popupNone();
}
function popupNone() {
  mainPopup.style.display = "none";
}