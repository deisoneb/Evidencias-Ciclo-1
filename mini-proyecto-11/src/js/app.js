// src/js/app.js

const canvas = document.getElementById('drawingCanvas');
const context = canvas.getContext('2d');
let drawing = false;
let drawingData = [];

canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mousemove', draw);

function startDrawing(event) {
    drawing = true;
    draw(event); // To draw a point if you just click without moving
}

function stopDrawing() {
    drawing = false;
    context.beginPath(); // Reset the context's path
    drawingData.push(null); // Mark end of a line
}

function draw(event) {
    if (!drawing) return;

    const x = event.clientX - canvas.offsetLeft;
    const y = event.clientY - canvas.offsetTop;

    context.lineWidth = 5;
    context.lineCap = 'round';
    context.strokeStyle = 'black';

    context.lineTo(x, y);
    context.stroke();
    context.beginPath();
    context.moveTo(x, y);

    drawingData.push({x, y}); // Store the drawing data
}

// Add save functionality
document.getElementById('saveButton').addEventListener('click', saveDrawing);

function saveDrawing() {
    fetch('/save_drawing', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ drawing: drawingData }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert('Dibujo guardado exitosamente!');
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Error al guardar el dibujo.');
    });
}