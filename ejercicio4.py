#Ejercicio 4
#Crear un programa que convierta un número entero (mayor que 1 y menor o igual que 1000) a número
#romano.


class ConvertidorARomano:
    def __init__(self, numero):
        if not 1 < numero <= 1000:
            raise ValueError("El número debe ser mayor que 0 y menor o igual que 1000.")
        self.numero = numero
        self.romano = self.convertidor_a_romano()

    def convertidor_a_romano(self,):
        valores_romanos = [
            (1000, "M"),(900, "CM"),(500, "D"),(400, "CD"),(100, "C"),(90, "XC"),(50, "L"),(40, "XL"),
            (10, "X"),(9, "IX"),(5, "V"),(4, "IV"),(1, "I")
            ]
        resultado = []
        numero = self.numero
        for valor, simbolo in valores_romanos:
            while numero >= valor:
                resultado.append(simbolo)
                numero -= valor
        return (resultado)
def pantalla():
    try:
        numero = int(input("ingrese un numero entero mayor que 1 y menor o igual que 1000: "))
        conversor = ConvertidorARomano(numero)
        print(f"El numero {numero} en romano e{conversor.romano}")
    except ValueError as error:
        print(f"Error: {error}. Por favor, ingrese un número válido.")

pantalla()