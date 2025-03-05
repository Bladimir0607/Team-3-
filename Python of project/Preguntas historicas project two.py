while True:
                #Inicio de preguntas historicas 
        print("************************************************************")
        print("*                                                          *")
        print("*          ¡Bienvenido/a a Preguntas Históricas!           *")
        print("*                                                          *")
        print("************************************************************")
        print("Prepárate para un emocionante viaje a través del tiempo.")
        print("Descubre hechos fascinantes y pon a prueba tus conocimientos.")
        print("¡Buena suerte y disfruta del recorrido!")

            #Inicio de preguntas personales
        nombre_usuario = input("Por favor, introduce tu nombre: ")
        edad = print("Por favor, introduce tu edad: ")
        respuesta =input("Respuesta:")
        Como_estas = print("¿Como Estás? ") 
        respuesta =input("Respuesta:")
        Nuestro_viaje = print("Iniciamos nuestro viaje , pulse enter para continuar...") 
  
            #Continuación de preguntas historicas , primera parte.
            # Toma de deciciones de no , continuar o no continuar, Final del programa.
        viajemos = input("Viajemos al pasado, hacia el año 1822, Ocupación Haitiana, ¿Estás listo/a? ")
        if  viajemos.lower() == "no":
            print("¡Qué lástima! ¡Hasta la próxima!")
            break

        if viajemos.lower() == "si":
            print("¡Excelente! Empecemos con las preguntas, ¡Buena suerte!, pulse enter para continuar...") 
            # Toma de deciciones Si , continuar.
        como_produjo = print("¿Cómo se produjo la ocupación haitiana en la República Dominicana? ")
        respuesta =input("Respuesta:")
        Concecunecias = print("¿Cuáles fueron las consecuencias de la ocupación haitiana en la República Dominicana? ")
        respuesta =input("Respuesta:")
        tiempo = print("¿Cuánto tiempo duró la ocupación haitiana en la República Dominicana? ")
        respuesta =input("Respuesta:")
    
          #Continuación de preguntas historicas , segunda parte, 
          # Toma de deciciones Si , continuar o no continuar .
        continuar = input(f"{nombre_usuario}, ¿desea continuar con las preguntas históricas? (Si/No): ")
        if continuar.lower() == "si":
            avanzar = print("Avancemos 22 años despues, hacia el año 1844, donde se proclamó la Independencia Nacional.")
            trabuco = print("¿Quien disparo el trabucazo la noche del 27 de Febrero de 1844? ")
            respuesta =input("Respuesta:")
            independencia = print("¿Qué significó la independencia nacional para la República Dominicana? ") 
            respuesta =input("Respuesta:")
            Padres_de_la_patria = print("¿Quienes son los padres de la patria? ")
            respuesta =input("Respuesta:")
        if  continuar.lower() == "no":
            print("¡Qué lástima! ¡Hasta la próxima!")
            break

            #Continuación de preguntas historicas , tercera parte y final.
            # Toma de deciciones Si , continuar o no continuar .
        seguimos = input(f"{nombre_usuario}, ¿desea continuar con las preguntas históricas? (Si/No): ") 
        if seguimos.lower() == "si":
            avanzar = print("Avancemos al año 1863, Restauración de la República.")
            respuesta =input("Respuesta:")
            restauracion = print("¿Qué fue la restauración de la República Dominicana? ")
            respuesta =input("Respuesta:")
            restauradores = print("¿Quienes fueron los restauradores? ")
            respuesta =input("Respuesta:")
            batalla = print("¿Cuál fue la batalla más importante de la restauración de la República Dominicana? ")
            respuesta =input("Respuesta:")
        elif seguimos.lower() == "no":
            print("Gracias por participar en Preguntas Historica, hasta la proxima.")
            break
        if  print(f"¡Felicitaciones, {nombre_usuario} ! Has completado todas las preguntas históricas. ¡Eres un verdadero conocedor de la historia dominicana!") :
            break # Fin del programa. 