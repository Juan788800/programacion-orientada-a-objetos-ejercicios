#Realizar una aplicación que recoja por teclado la cantidad total a pagar y la cantidad #que se ha
#entregado. La aplicación debe calcular el cambio correspondiente con el menor número #de monedas
#y/o billetes posibles.

# Definición de la clase Cambio
class Cambio:
    # Método constructor: recibe el total a pagar y el dinero entregado
    def __init__(self, total, entregado):
        self.total = total  # Guarda el total a pagar
        self.entregado = entregado  # Guarda la cantidad entregada por el cliente
        self.cambio = entregado - total  # Calcula el cambio a devolver
        # Lista de moneda  disponibles en pesos colombianos
        self.denominaciones = [5000, 1000, 500, 200, 100, 50]

    # Método para calcular y mostrar el cambio
    def calcular_cambio(self):
        # Si el dinero entregado es menor que el total, muestra un mensaje y termina
        if self.entregado < self.total:
            print("El dinero entregado es menor que el total a pagar.")
            return  # Sale del método

        # Muestra el cambio total a devolver, redondeado a dos decimales
        print(f"Cambio a devolver: {round(self.cambio, 2)} pesos")
        cambio_restante = round(self.cambio, 2)  # Inicializa el cambio restante

        # Recorre cada denominación para calcular cuántas de cada una se deben dar
        for monedas in self.denominaciones:
            # Calcula cuántas monedas  caben en el cambio restante
            cantidad = int(cambio_restante // monedas)
            # Si hay al menos una moneda de esta denominación
            if cantidad > 0:
                # Muestra cuántas monedas se deben dar de esta denominación
                print(f"{cantidad} monedas de  {monedas} pesos")
                # Resta el valor entregado de esta denominación al cambio restante
                cambio_restante = round(cambio_restante - cantidad * monedas, 2)


# Solicita al usuario el total a pagar 
total = float(input("Introduce el total a pagar: "))

# Solicita al usuario la cantidad entregada
entregado = float(input("Introduce el dinero entregado: "))

# Crea un objeto de la clase Cambio con los valores introducidos
cambio = Cambio(total, entregado)

# Llama al método para calcular y mostrar el cambio
cambio.calcular_cambio()

