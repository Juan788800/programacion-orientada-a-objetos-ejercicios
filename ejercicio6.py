#Realizar un programa que pida un mes y un año (superior a 1900) y muestre el calendario del mes de
#esta manera:
#L M M J V S D
#==========================
#1 2 3 4 5 6
#7 8 9 10 11 12 13
#14 15 16 17 18 19 20
#21 22 23 24 25 26 27
#28 29 30 31
#Para ello es necesario averiguar que día de la semana (Lunes, Martes, ...) corresponde con un fecha
#determinada. Hay muchas maneras de calcularlo: nosotros vamos a contar los días que han trascurridos
#desde el año 1900 (NOTA: ten en cuenta que queremos realizar un calendario que empiece en lunes, no
#en domingo).


# Importa el módulo calendar de la biblioteca estándar de Python
import calendar

# Definición de la clase que representará el calendario mensual
class calendariomensual:
    # Método constructor: recibe el año y el mes como parámetros
    def __init__(self, año , mes):
        self.año = año          # Guarda el año recibido como atributo de la instancia
        self.mes = mes          # Guarda el mes recibido como atributo de la instancia
        # Crea un objeto TextCalendar que inicia la semana en lunes (0)
        self.cal = calendar.TextCalendar(firstweekday=0)
    
    # Método para mostrar el calendario en el formato solicitado
    def mostrar_calendario(self):
        # Imprime el encabezado de los días de la semana
        print("L   M   M   J   V   S   D")
        print("========================")
        # Obtiene una lista de semanas del mes, donde cada semana es una lista de 7 días
        # Los días fuera del mes se representan con 0
        semanas = self.cal.monthdayscalendar(self.año, self.mes)
        # Itera sobre cada semana del mes
        for semanas in semanas:
            # Itera sobre cada día de la semana
            for dia in semanas:
                if dia == 0:
                    # Si el día es 0, imprime espacios para mantener la alineación
                    print("  ", end="  ")
                else:
                    # Si es un día válido, lo imprime con formato de dos espacios
                    print(f"{dia:2}", end="  ")
            # Salto de línea al terminar cada semana
            print()

# Función para pedir y validar los datos de entrada al usuario
def datos():
    while True:
        try:
            # Solicita el año al usuario
            año = int(input("Introduce el año (mayor a 1900): "))
            if año <= 1900:
                print("El año debe ser mayor a 1900.")
                continue  # Vuelve a pedir el año si no es válido
            # Solicita el mes al usuario
            mes = int(input("Introduce el mes (1-12): "))
            if not 1 <= mes <= 12:
                print("El mes debe estar entre 1 y 12.")
                continue  # Vuelve a pedir el mes si no es válido
            # Si ambos datos son válidos, los retorna como tupla
            return año, mes
        except ValueError:
            # Si el usuario introduce un valor no numérico, muestra un mensaje de error
            print("Por favor, introduce valores numéricos válidos.")

# Función principal del programa
def programa():
    # Llama a la función datos para obtener el año y el mes
    año, mes = datos()
    # Crea una instancia de la clase calendariomensual con los datos introducidos
    calendario = calendariomensual(año, mes)
    # Llama al método para mostrar el calendario
    calendario.mostrar_calendario()

# Llama a la función principal para iniciar el programa
programa()
