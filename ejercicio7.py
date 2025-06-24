#Ejercicio 7
#Escribir dos funciones que permitan calcular:
#• La cantidad de segundos en un tiempo dado en horas, minutos y segundos. La cantidad de horas,
#minutos y segundos de un tiempo dado en segundos.


#• Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a
#segundos, convertir a horas, minutos y segundos o salir del programa.


class conversor_tiempo:
    def __init__(self):
        #constructor vacion ya que no se necesitan atributos iniciales
        pass

    def segundo(self, horas , minutos , segundos):
        return horas * 3600 + minutos *60 + segundos 
    
    def segundos(self,segundos):
        horas= segundos // 3600 #calcula cuantas horas compleyas hay
        minutos= (segundos % 3600) // 60 # calcula los minutos despues de las horas
        segundos = segundos % 60 # calcula los segundos restantes
        return horas, minutos , segundos 


# Función que muestra el menú y gestiona la interacción con el usuario
def menu():
    
    conversor = conversor_tiempo()  # Crea una instancia de la clase ConversorTiempo
    while True:
        # Muestra las opciones del menú
        print("--- Menú Conversor de Tiempo ---")
        print("1. Convertir horas, minutos y segundos a segundos")
        print("2. Convertir segundos a horas, minutos y segundos")
        print("3. Salir")
        opcion = input("Elige una opción (1/2/3): ")

        if opcion == "1":
            # Opción para convertir a segundos
            try:
                horas = int(input("Introduce las horas: "))  # Pide las horas al usuario
                minutos = int(input("Introduce los minutos: "))  # Pide los minutos al usuario
                segundos = int(input("Introduce los segundos: "))  # Pide los segundos al usuario
                total = conversor.segundo(horas, minutos, segundos)  # Llama al método de conversión
                print(f"{horas}h {minutos}m {segundos}s son {total} segundos.")
            except ValueError:
                # Controla si el usuario introduce un valor no numérico
                print("Por favor, introduce solo números enteros.")

        elif opcion == "2":
            # Opción para convertir a horas, minutos y segundos
            try:
                segundos = int(input("Introduce la cantidad de segundos: "))  # Pide los segundos al usuario
                h, m, s = conversor.segundos(segundos)  # Llama al método de conversión
                print(f"{segundos} segundos son {h}h {m}m {s}s.")
            except ValueError:
                # Controla si el usuario introduce un valor no numérico
                print("Por favor, introduce solo números enteros.")

        elif opcion == "3":
            # Opción para salir del programa
            print("¡Hasta luego!")
            break  # Sale del bucle y termina el programa

        else:
            # Si el usuario introduce una opción no válida
            print("Opción no válida. Intenta de nuevo.")

# Llama a la función del menú para iniciar el programa
menu()