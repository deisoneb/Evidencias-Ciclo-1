let ingresosArray = [];

function agregarIngreso() {
    const ingreso = parseFloat(document.getElementById('ingreso').value);
    if (!isNaN(ingreso)) {
        ingresosArray.push(ingreso);
        mostrarIngresos();
        document.getElementById('ingreso').value = '';
    } else {
        alert('Por favor, ingresa un número válido');
    }
}

function mostrarIngresos() {
    const ingresosList = document.getElementById('ingresosList');
    ingresosList.innerHTML = '<h3>Ingresos Agregados:</h3>';
    ingresosArray.forEach((ingreso, index) => {
        ingresosList.innerHTML += `<p>Ingreso ${index + 1}: $${ingreso.toFixed(2)}</p>`;
    });
}

function calcular() {
    const sumaIngresos = ingresosArray.reduce((acc, ingreso) => acc + ingreso, 0);
    document.getElementById('resultado').textContent = `Total de Ingresos: $${sumaIngresos.toFixed(2)}`;
}
