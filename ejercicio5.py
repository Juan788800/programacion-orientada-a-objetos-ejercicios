#Ejercicio 5
#Diseñar un programa que permita adivinar al ordenador un determinado número entero y positivo para
#lo cual se deben leer los límites en los que está comprendido dicho número. El programa deberá ir
#mostrando números que recibirán las siguientes respuestas:
#1. ‘S’, si es correcto.
#2. ‘A’, si es más alto que el número a adivinar.
#3. ‘B’, si es más bajo. Al finalizar el programa, se deberá escribir el número de intentos realizados
#para acertar el número.

# clase adivinador
class adivinador:
    # metodo constructor: inicializa los limites y el contador de intentos
    def __init__(self, limite_bajo, limite_alto):
        self.limite_bajo = limite_bajo  #limite bajo del rango de busqueda
        self.limite_alto = limite_alto # limite alto del rango de busqueda 
        self.intentos = 0 # contador de intentos realizados
    # metodo principal para adivinar el numero
    def adivinar_numero(self):
        # mensajes para el usuario
        print("Piensa en un número entre", self.limite_bajo, "y", self.limite_alto)

        print("intentare adivinar el número .")
        print("'S' si es correcto")
        print("'A' si es mas bajo")
        print("'B' si es mas alto")
        # bucle principal del juego
        while True:
            self.intentos += 1 # incrementa el contador de intentos en cada ciclo
            # calcula el numero q tiene q adivinar usando el punto medio del rango actual
            intento = (self.limite_bajo + self.limite_alto) //2
            #solicita al usuario la respuesta 
            respuesta = input(f"¿Es {intento}? (S/A/B): ")

            # si la respuesta es 's' correcto
            if respuesta == 's':
                print(f"adivine el numero {intento} {self.intentos} intentos")
                return #termina el metodo y el juego
            
            # si la respuesta es 'B' el numero es mas alto
            elif respuesta == 'B':
                self.limite_bajo = intento - 1 # ajusta el limite bajo
            
            # si la respuesta es 'B' el numero es mas bajo
            elif respuesta == 'A':
                self.limite_alto = intento + 1 # ajusta el limite alto
            # si la respuesta no es valida 
            else:
                print("Respuesta no valida porfa vor ingresar 'S', 'A' o 'B'")

 # funcion para inicializar el juego
def juego():
    # solicita al usuario los limites bajos y altos del rango
    print("Bienvenido al juego de adivinar el número")
    limite_bajo = int(input("Ingrese el límite bajo: "))
    limite_alto = int(input("Ingrese el límite alto: "))
    # crea una instancia de la clase adivinador con los limites dados
    juego= adivinador(limite_bajo, limite_alto)
    #llama al metodo para incializar el juego
    juego.adivinar_numero()

#llama a la funcion principal para inciar el programa
juego()