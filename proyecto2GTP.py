import random

# Variables iniciales
x = random.randint(1, 10)
intentos_max = 5
intentos_usados = 1
lista = []  # Lista para los números introducidos
acertado = False

# Función para obtener la entrada del usuario
def obtener_numero(lista, intentos_usados, intentos_max):
    while True:
        try:
            numero = int(input(f"Entra un número (1-10): "))
            if numero == -1:
                # Muestra el porcentaje de intentos utilizados
                porcentaje = (intentos_usados / intentos_max) * 100
                print(f"El número de intentos usados es {intentos_usados}, sobre intentos máximos {intentos_max}. El porcentaje es {porcentaje:.2f}%")
                continue
            elif numero < 1 or numero > 10:
                print("El número no es válido. Debe estar entre 1 y 10.")
            elif numero in lista:
                print("El número ya ha sido introducido. Intenta con otro.")
            else:
                return numero
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Función para mostrar el mensaje cuando se ha acertado
def mostrar_mensaje_acertado(intentos_usados, x):
    if intentos_usados == 1:
        print("¡Felicidades, acertaste a la primera!")
    else:
        print(f"¡Número acertado! El número era {x}.")

# Función para mostrar los mensajes de error o sugerencia
def mostrar_mensaje_error(numero, x, intentos_usados):
    if numero < x:
        print(f"El número es mayor. Llevas {intentos_usados} intentos, prueba otra vez.")
    elif numero > x:
        print(f"El número es menor. Llevas {intentos_usados} intentos, prueba otra vez.")

       
while not acertado:
    while intentos_usados <= intentos_max:
        numero = obtener_numero(lista, intentos_usados, intentos_max)
            
        # Agrega el número a la lista de números ya introducidos
        lista.append(numero)
           
        if numero == x:
            mostrar_mensaje_acertado(intentos_usados, x)
            acertado = True
            break
        else:
            mostrar_mensaje_error(numero, x, intentos_usados)
                
        intentos_usados += 1
        
    if not acertado:
        print(f"Has agotado tus {intentos_max} intentos. El número correcto era {x}.")
       
    # Preguntar si quiere jugar otra vez
    jugar_nuevamente = input("¿Quieres volver a jugar? (S/N): ").strip().upper()
    if jugar_nuevamente == 'N':
        print("¡Gracias por jugar!")
        break
    else:
        continue