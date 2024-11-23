import random

#Variables
x = random.randint(1,10)
intentos_max=5
intentos_usados=1
lista =[] #Guarda los elementos entrados.
porcentaje=0
acertado= False
numero= 0


def entrada():
    numero = int(input("Entra un numero (0-10): "))
    return numero
       
    
#Cuerpo del programa
while True:
    if acertado == True:
            break
    while intentos_usados != intentos_max:
        
        numero= entrada()
        if numero == -1:
            #intentos_usados -= 1
            porcentaje = (intentos_usados/intentos_max)*100            
            print(f"El numero de intentos usados es  {intentos_usados}, sobre intentos maximos {intentos_max},el porcentaje es {porcentaje}%")
            continue
        if numero > 10 or numero < 1:
            print("El numero no es correcto")
            continue       
        if numero in lista:
            print("El numero esta repetido")
            intentos_usados += 1
            continue          
        else:
            lista.append(numero) 
        if numero == x:
            if intentos_usados == 1:
                print("Felicidades, encertaste a la primera!")
                acertado=True    
                break
            print("Numero accertado!",x)
            acertado=True
            break
        elif numero < x:
            print("El numero es mayor!")
            print(f"Numero erroneo, llevas {intentos_usados} intentos, prueba otra vez!") 
        elif numero > x:
            print("El numero es menor")
            print(f"Numero erroneo, llevas {intentos_usados} intentos, prueba otra vez!") 
                
        intentos_usados += 1        
    else:
        print("Has agotado tus intentos")
        y=input("Quieres volver a jugar? S/N:")
        if y =="N":            
            break
        else:
            x = random.randint(1,10)
            intentos_max=5
            intentos_usados=1
            lista =[]
            porcentaje=0
            
            
    

