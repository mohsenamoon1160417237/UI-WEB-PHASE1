let rate1 = document.querySelectorAll(".rate-1")
let rate2 = document.querySelectorAll(".rate-2")
let rate3 = document.querySelectorAll(".rate-3")
let rate4 = document.querySelectorAll(".rate-4")
let rate5 = document.querySelectorAll(".rate-5")



for (let i = 0; i < rate1.length; i++) {
     rate1[i].addEventListener("click", function() {
       console.log("Your rating to this product is 1")
     });
     rate1[i].style.cursor = 'pointer'
 }


for (let i = 0; i < rate2.length; i++) {
     rate2[i].addEventListener("click", function() {
       console.log("Your rating to this product is 2")
     });
     rate2[i].style.cursor = 'pointer'
 }


for (let i = 0; i < rate3.length; i++) {
     rate3[i].addEventListener("click", function() {
       console.log("Your rating to this product is 3")
     });
     rate3[i].style.cursor = 'pointer'
 }


 for (let i = 0; i < rate4.length; i++) {
     rate4[i].addEventListener("click", function() {
       console.log("Your rating to this product is 4")
     });
     rate4[i].style.cursor = 'pointer'
 }


for (let i = 0; i < rate5.length; i++) {
     rate5[i].addEventListener("click", function() {
       console.log("Your rating to this product is 5")
     });
     rate5[i].style.cursor = 'pointer'
 }
