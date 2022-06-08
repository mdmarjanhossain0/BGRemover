window.onscroll = function () {
    myFunction()
};

// Get the navbar
var navbar = document.getElementById("navbar");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
    if (window.pageYOffset > sticky) {
        navbar.classList.add("sticky")
        console.log("sticky")
    } else {
        navbar.classList.remove("sticky");
        console.log("nonstickty")
    }
}




// window.addEventListener("scroll", function() {
//     var navbar = document.getElementById("navbar");
//     navbar.classList.add("sticky", window.scrollY > 0)
// })