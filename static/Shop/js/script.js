

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


var contentDiv = document.querySelector('.logo');

    var img4 = document.createElement('img');
        img4.id = 'map4';
        img4.classList.add('map0');
        img4.style.width = '1200px';
        img4.style.left = 0 + 'px';
        img4.style.top = 0 + 'px';
        img4.style.position = 'absolute';
        img4.src = '/media/paralax/31.png'; // Шлях до зображення
        img4.alt = 'Dynamic Image'; // Альтернативний текст
        contentDiv.appendChild(img4);

    var img3 = document.createElement('img');
        img3.id = 'map3';
        img3.classList.add('map0');
        img3.style.width = '900px';
        img3.style.left = 300 + 'px';
        img3.style.top = 50 + 'px';
        img3.style.position = 'absolute';
        img3.src = '/media/paralax/3.png'; // Шлях до зображення
        img3.alt = 'Dynamic Image'; // Альтернативний текст
        contentDiv.appendChild(img3);

    var img2 = document.createElement('img');
        img2.id = 'map2';
        img2.classList.add('map0');
        img2.style.width = '1180px';
        img2.style.left = 10 + 'px';
        img2.style.top = 0 + 'px';
        img2.style.position = 'absolute';
        img2.src = '/media/paralax/2.png'; // Шлях до зображення
        img2.alt = 'Dynamic Image'; // Альтернативний текст
        contentDiv.appendChild(img2);


    var img1 = document.createElement('img');
        img1.id = 'map1';
        img1.classList.add('map0');
        img1.style.width = '1200px';
        img1.style.left = 0 + 'px';
        img1.style.top = 0 + 'px';
        img1.style.position = 'absolute';
        img1.src = '/media/paralax/1.png'; // Шлях до зображення
        img1.alt = 'Dynamic Image'; // Альтернативний текст
        contentDiv.appendChild(img1);

var x = window.innerWidth
var y = window.innerHeight

document.addEventListener('mousemove', function(event) {
    var mouseX = event.clientX;
    var mouseY = event.clientY;
    if (x / 2 > mouseX){
        play(img1, -15)
        play(img2, 0)
        play(img3,295)
    }else{
        play(img1, 15)
        play(img2,20)
        play(img3,305)
    }
});

function play(elem,num){
    elem.style.transition = 'left ' + 0.5 + 's linear'; // Плавний перехід з лінійною швидкістю
    elem.style.left = num + 'px'; // Переміщення на вказану позицію
}