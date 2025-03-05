//varibles 
    let numeroMazimoPosible = 100;
    let numeroSecreto = Math.floor(Math.random() *numeroMazimoPosible) + 1;
    let numeroUsuario = 0; //Declarar fuera del bucle while.
    let intentos = 1; //Declarar fuera del bucle while.
    //let PalabraVeces = 'vez'; //Declarar fuera del bucle while.
    let Maximosintentos = 10; //Declarar fuera del bucle while.


    
    




    //Bucle while.
    while (numeroUsuario !== numeroSecreto) { 
        numeroUsuario = parseInt(prompt(`Me indicas un numero entre 1 y ${numeroMazimoPosible} por favor: `));
        console.log(numeroUsuario); 
    
    /*
    este codigo realiza la comparacion 
    */
    if (numeroUsuario == numeroSecreto) {
        //ACEPTAMOS, FUE VERDADERA // 
        alert(`Acertaste, el numero es : ${numeroUsuario}. Lo lograste en ${intentos} ${intentos == 1 ? 'vez' : 'veces'}`); //Mostrar mensaje de acierto.
        break; // Salir del bucle cuando acierta.
        } else {
        if (numeroUsuario > numeroSecreto) {
            alert('El numero secreto es menor');
        } else {
            alert('El numero secreto es mayor ');
        }

        //intentos = intentos + 1;  //Incrementar el contador cuando no acierta.
        //intentos += 1;

        intentos ++; 
        //PalabraVeces =  'veces'; //Cambiar la palabra a plural cuando no acierta.
        if (intentos > Maximosintentos) {
            alert(`Llegaste al numero maximo de ${Maximosintentos} intentos`);
            break; // Salir del bucle cuando no acierta.
        }
    
    

        // La condicion no se cumplio //
        //alert('Lo siento, no acertaste el numero');
    }
} //Fin del bucle while.

