let intervalo;

document.addEventListener('DOMContentLoaded', (event) => {
    const hoy = new Date().toISOString().split('T')[0];
    document.getElementById('fecha').setAttribute('min', hoy);
});

function iniciarCuentaRegresiva() {
    const fechaSeleccionada = document.getElementById('fecha').value;
    if (!fechaSeleccionada) {
        alert('Por favor, selecciona una fecha válida');
        return;
    }

    const fechaObjetivo = new Date(fechaSeleccionada).getTime();
    clearInterval(intervalo);
    actualizarContador(fechaObjetivo);
    intervalo = setInterval(() => actualizarContador(fechaObjetivo), 1000);
}

function actualizarContador(fechaObjetivo) {
    const ahora = new Date().getTime();
    const distancia = fechaObjetivo - ahora;

    if (distancia < 0) {
        clearInterval(intervalo);
        document.getElementById('contador').textContent = '¡Tiempo terminado!';
        return;
    }

    const dias = Math.floor(distancia / (1000 * 60 * 60 * 24));
    const horas = Math.floor((distancia % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutos = Math.floor((distancia % (1000 * 60 * 60)) / (1000 * 60));
    const segundos = Math.floor((distancia % (1000 * 60)) / 1000);

    document.getElementById('contador').textContent = `Tiempo restante: ${dias}d ${horas}h ${minutos}m ${segundos}s`;
}
