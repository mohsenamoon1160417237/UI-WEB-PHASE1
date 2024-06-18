let removeIcons = document.querySelectorAll(".remove-card-icon")

for (let i = 0; i < removeIcons.length; i++) {
    removeIcons[i].addEventListener("click", function() {
       let parentDiv = removeIcons[i].parentNode.parentNode.parentNode
       parentDiv.remove()
    })
}