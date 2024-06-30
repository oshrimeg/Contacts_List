
const addNameLabel = document.getElementById("addNameLabel")
const nameInput = document.getElementById("addName")


nameInput.addEventListener("focus", ()=> {
    addNameLabel.style.fontWeight = "bold"
})

nameInput.onblur = function() {
    addNameLabel.style.fontWeight = "normal"
}

const agreeCheckbox = document.getElementById("agree")



agreeCheckbox.onchange = ()=> {
    agreeCheckbox.style.accentColor = "green"
}




