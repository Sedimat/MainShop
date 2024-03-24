

document.addEventListener("DOMContentLoaded", function() {
    var screenWidth = window.innerWidth;
    var screenHeight = window.innerHeight;

    var contentDiv = document.querySelector(".content");

    if (contentDiv) {
        contentDiv.style.minHeight = screenHeight - 300 + "px";
    }else{
        console.log('Не той', screenHeight);
    }
});