// pregunta para el usuario// variables//

alert('Bienvenidas y Bienvenidos');
let Lasemana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'];
let Sabadodomingo = ['Sabado', 'Domingo'];

/*
este codigo realiza la comparacion 
*/

while (true) {
    let cualquierdiadeLasemana = prompt('Que dia de la semana es?');
    if (Lasemana.includes(cualquierdiadeLasemana)) {
        alert(`Buena semana, hoy es: ${cualquierdiadeLasemana}`);
        break;
    } else if (Sabadodomingo.includes(cualquierdiadeLasemana)) {
        alert("¡Buen fin de semana!");
        break;
    } else {
        alert("Día no válido, por favor ingrese un día de la semana válido.");
    }
}
