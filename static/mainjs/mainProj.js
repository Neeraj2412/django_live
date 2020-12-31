var prevScrollpos = window.pageYOffset;
window.onscroll = function () {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("newnav").style.top = "0";
    } else {
        document.getElementById("newnav").style.top = "-70px";
    }
    prevScrollpos = currentScrollPos;
}
// Navbar Vikas Singh
var hamburger = document.querySelector(".hamburgerContainer");
var menuContaienr = document.querySelector(".menusContainer");

hamburger.addEventListener("click", function () {
    hamburger.classList.toggle("active");
    menuContaienr.classList.toggle("active");

})

var menus = document.querySelectorAll(".menusContainer .menu");

window.addEventListener('resize', function () {
    var width = window.outerWidth;
    if (width <= 700) {
        menus.forEach(element => {
            element.classList.remove("open");
        });
    }
})

menus.forEach(element => {
    element.addEventListener('click', function () {
        element.classList.toggle("open");
    })
});
// Navbar Vikas Singh