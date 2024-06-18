let btn = document.getElementById("btn")
let HumberMenu = document.getElementById("HumberMenu")
let closebtn = document.getElementById("close")
let descriptionBtn = document.getElementById("description-head")
let additionalInfoBtn = document.getElementById("add-info-head")
let reviewsBtn = document.getElementById("reviews-head")
let color1 = document.querySelector(".prod-color-1")
let color2 = document.querySelector(".prod-color-2")
let color3 = document.querySelector(".prod-color-3")
let color4 = document.querySelector(".prod-color-4")
let price = document.querySelector(".prod-price")


descriptionBtn.style.cursor = 'pointer'
additionalInfoBtn.style.cursor = 'pointer'
reviewsBtn.style.cursor = 'pointer'
color1.style.cursor = 'pointer'
color2.style.cursor = 'pointer'
color3.style.cursor = 'pointer'
color4.style.cursor = 'pointer'



btn.addEventListener("click",function(){
    HumberMenu.classList.add("active")
})

closebtn.addEventListener("click",function(){
    HumberMenu.classList.remove("active")
})

descriptionBtn.addEventListener("click",function(){
    window.location.href = window.location.href.split("/").slice(0,-1).join("/") + "/" + "ProductD.html"
})

additionalInfoBtn.addEventListener("click",function(){
    window.location.href = window.location.href.split("/").slice(0,-1).join("/") + "/" + "ProductA.html"
})

reviewsBtn.addEventListener("click",function(){
    window.location.href = window.location.href.split("/").slice(0,-1).join("/") + "/" + "ProductR.html"
})

color1.addEventListener("click",function(){
    price.textContent = '$1999.00'
})

color2.addEventListener("click",function(){
    price.textContent = '$1700.00'
})

color3.addEventListener("click",function(){
    price.textContent = '$1600.00'
})

color4.addEventListener("click",function(){
    price.textContent = '$1900.00'
})