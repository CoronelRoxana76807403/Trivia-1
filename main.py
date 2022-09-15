import time  # Importamos la librería time

puntaje = 0

iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print("Bienvenido a mi trivia sobre computación")
print("Pondremos a prueba tus conocimientos")
print("Tienes", puntaje, "puntos")

while iniciar_trivia == True:  #  Mientras iniciar_trivia sea True, repite:
    intentos += 1
    puntaje = 0

    print("\nIntento número:", intentos)
    input("Presiona Enter para continuar")

    print("Primera pregunta...")
    print("Imagina que aquí procede toda tu trivia")
    time.sleep(1)  # para ayudarnos a imaginar que vamos jugando
    print("Jugando...")
    time.sleep(1)
    puntaje = puntaje + 20  # Imaginaremos que ganó 20 puntos en el desarrollo de la trivia
    print("Excelente, has obtenido", puntaje, "puntos")

    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower(
        )

    if repetir_trivia != "si":  # != significa "distinto"
        print("\nEspero {nombre} que lo hayas pasado bien, hasta pronto!")
        iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
