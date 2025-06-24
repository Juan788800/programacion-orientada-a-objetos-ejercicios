# Vamos a realizar dos funciones: una que nos permita convertir un número entero a binario, y otra que
#nos permita convertir un numero binario a decimal.
#• ConvertirABinario: Función que recibe un número entero y devuelve una cadena con la
#representación del número en binario.
#• ConvertirADecimal: Función que recibe una cadena con la representación binaria de un número
#y devuelve el número en decimal.
#Crea un programa principal que permita convertir de decimal a binario y de binario a decimal.



# # Realizar un programa que permita convertir un número decimal a binario y viceversa.
class conversorBinario_y_Decimal:
    def __init__(self):
        #metodo constructor que inicializa la clase
        pass
    
    def convertir_a_binario(self,numero):
        if numero == 0:
            return "0" #si el numero es 0, devolvemos "0"
        binario = ""
        while numero > 0:
            #obitene el residuo de la division entre 2 y lo agrega al inicio de la cadena binario
            binario = str(numero % 2) + binario
            numero //= 2 #divide el numero entre 2 y descarta el residuo
        return binario
    
    def convertir_a_decimal(self,binario):
        decimal = 0
        potencia = 0
        #recorre la cadena binario de derecha a izquierda
        for digito in reversed(binario):
            #si el digito es '1', suma 2 elevado a la potencia correspondiente al decimal
            if digito == '1':
                decimal += 2 ** potencia
                #incrementa la potencia en 1
            potencia += 1
        return decimal

#función principal que permite al usuario interactuar con el conversor
def main():
    #creamos una instancia de la clasconversorBinario_y_Decimal
    conversor = conversorBinario_y_Decimal()
    while True:
        #muestra el menú de opciones al usuario
        print("conversor de binario a decimal y viceversa")
        print("1, convertir a binario")
        print("2. convertir a decimal")
        print("3. salir del programa")
        #solicita al usuario que elija una opción
        opciones=input("Elige una opcion: (1,2,3):")

        if opciones == "1":
            #opcion para convertir a binario
            try:
                numero = int(input("ingrese un numero decimal:"))
                #llama al metodo de conversion y muestra el resultado
                print(f"el numero {numero} en binario es: {conversor.convertir_a_binario(numero)}")
                # error si el usuario no ingresa un numero entero
            except ValueError:
                print("Por favor, introduce un número entero válido.")
        elif opciones == "2":
            #opcion para convertir a decimal
            binario= input("ingrese un numero binario:")
            try:
                #llama al metodo de conversion y muestra el resultado
                print(f"el numero {binario} en decimal es: {conversor.convertir_a_decimal(binario)}")
            except ValueError:
                # error si el usuario no ingresa una cadena binaria valida
                print("Por favor, introduce una cadena binaria válida.")
        elif opciones == "3":
            #opcion para salir del programa
            print("Saliendo del programa...")
            print("Gracias por usar el conversor.")
            break
# llama a la funcion principal
main()