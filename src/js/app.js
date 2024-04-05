let btn = document.getElementById("btn")
let HumberMenu = document.getElementById("HumberMenu")
let closebtn = document.getElementById("close")

btn.addEventListener("click",function(){
    HumberMenu.classList.add("active")
})
closebtn.addEventListener("click",function(){
    HumberMenu.classList.remove("active")
})