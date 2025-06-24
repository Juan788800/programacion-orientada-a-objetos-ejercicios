# Realizar un algoritmo que permita descomponer un número en sus factores primos.

#creaos una clase llamada descomponer_numeroprimo 
class descomponer_numeroprimo:
    #metodo constructor que recibe un número a descomponer y los guarda como atributo de la clase
    def __init__(self, numero):
        self.numero = numero #atributo que guarda el número a descomponer
    # metodo para calcular los factores primos del número
    def factores_primos(self):
        N= self.numero
        factores = [] #lista para guardar los factores primos
        divisor = 2 # inicializa el divisor en 2, el primer número primo
        # Bucle para encontrar los factores primos
        # mientras el cuadrado del divisor sea menor o igual al número N
        while divisor * divisor <= N:
            # Mientras N sea divisible por el divisor actual
            while N % divisor == 0:
                factores.append(divisor) #añadimos el divisor a la lista de factores
                N //= divisor
            divisor += 1 #incrementamos el divisor
        if N >1:
            factores.append(N) #si N es mayor que 1, lo añadimos a la lista de factores
        return factores # devolvemos la lista de factores primos

# Solicita al usuario un número entero mayor que 1
numero = int(input("ingrese un numero entero mayor que 1:"))
descomponer = descomponer_numeroprimo(numero) #creamos un objeto de la clase descomponer_numeroprimo
resultado = descomponer.factores_primos() #llamamos al método factores_primos

#imprimos el resultado
print(f"Los factores primos de {numero} son: {resultado}") 