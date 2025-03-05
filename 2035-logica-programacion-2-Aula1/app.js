// Version: 1.2

// Definir variables globales
let listaNumeroSorteados = [];
let numeroMaximos = 10;

// Función para generar un número secreto aleatorio entre 1 y 10
function generalNumeroSecreto() {
    if (listaNumeroSorteados.length == numeroMaximos) {
        asignarTextoElemento('.texto__parrafo', 'Ya se sortearon todos los números posibles');
        return null; // Retornar null si ya se sortearon todos los números
    }

    let numeroGenerado = Math.floor(Math.random() * 10) + 1; 
    
    console.log(listaNumeroSorteados);
    console.log(numeroGenerado);

    // Si el número generado está incluido en la lista
    if (listaNumeroSorteados.includes(numeroGenerado)) {
        // Se vuelve a llamar la función para generar un nuevo número
        return generalNumeroSecreto();
    } else {
        listaNumeroSorteados.push(numeroGenerado);
        return numeroGenerado;
    }
}

// Generar un número secreto aleatorio entre 1 y 10
let numeroSecreto = generalNumeroSecreto();
let intentos = 1;
console.log(numeroSecreto);

// Función para asignar texto a un elemento HTML
function asignarTextoElemento(elemento, texto) {
    let elementoHTML = document.querySelector(elemento);
    elementoHTML.innerHTML = texto;
}

// Función para verificar los intentos del usuario
function verificarIntentos() {
    let numeroDeUsuario = parseInt(document.getElementById('valorUsuario').value);

    if (numeroDeUsuario === numeroSecreto) { 
        asignarTextoElemento('.texto__parrafo', `Acertaste el número en ${intentos} ${(intentos === 1) ? 'vez' : 'veces'}`);
        document.getElementById('reiniciar').removeAttribute('disabled');
    } else { 
        // El usuario no acertó
        if (numeroDeUsuario > numeroSecreto) {
            asignarTextoElemento('.texto__parrafo', 'El número secreto es menor');
        } else {
            asignarTextoElemento('.texto__parrafo', 'El número secreto es mayor');
        }
        intentos++;
        limpiarCaja();
    }
}

// Función para limpiar la caja de entrada
function limpiarCaja() {
    document.querySelector('#valorUsuario').value = ''; 
}

// Función para mostrar los mensajes iniciales y reiniciar el juego
function condicionesIniciales() {  
    asignarTextoElemento('h1', 'Juego del número secreto!');
    asignarTextoElemento('.texto__parrafo', `Indica un número del 1 al ${numeroMaximos}`);
    numeroSecreto = generalNumeroSecreto();
    intentos = 1;
}

// Función para reiniciar el juego
function reiniciarJuego() {
    limpiarCaja();
    condicionesIniciales();
    document.querySelector('#reiniciar').setAttribute('disabled', true);
}

// Llamar a la función para mostrar los mensajes iniciales
condicionesIniciales();
