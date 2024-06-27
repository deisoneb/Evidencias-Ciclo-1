let incomeArray = [];

function addIncome() {
    const income = parseFloat(document.getElementById('ingreso').value);
    if (!isNaN(income)) {
        incomeArray.push(income);
        showIncome();
        document.getElementById('ingreso').value = '';
    } else {
        alert('Por favor, ingresa un número válido');
    }
}

function showIncome() {
    const incomeList = document.getElementById('ingresosList');
    incomeList.innerHTML = '<h3>Ingresos Agregados:</h3>';
    incomeArray.forEach((ingreso, index) => {
        incomeList.innerHTML += `<p>Ingreso ${index + 1}: $${ingreso.toFixed(2)}</p>`;
    });
}

function count() {
    const sumIncome = incomeArray.reduce((acc, ingreso) => acc + ingreso, 0);
    document.getElementById('resultado').textContent = `Total de Ingresos: $${sumIncome.toFixed(2)}`;
}
