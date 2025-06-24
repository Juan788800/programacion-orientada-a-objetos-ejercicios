#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y
#cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los
#siguientes métodos para la clase:
#• Un constructor, donde los datos pueden estar vacíos.
#• Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
#directamente, sólo ingresando o retirando dinero.
#• mostrar(): Muestra los datos de la cuenta.
#• ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa,
#no se hará nada.
#• retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.


class cuenta:
    def __init__(self, titular="", cantidad=0 ):
        self.titular = titular 
        self.cantidad =float(cantidad)

    
    #getter para el titular
    def get_titular(self):
        return self.titular #devuelve el nombre del titular de la cuenta
    
    #setter para el titular 
    def set_titular(self,nuevo_titular):
        self.titular =nuevo_titular # establece el nombre del titular de la cuenta

    
    #getter para cantidad

    def get_cantidad(self):
        return self.cantidad # devuelve el saldo de la cuenta
    
    def set_cantidad(self,nueva_cantidad):
        self.cantidad = float(nueva_cantidad)

    def mostrar(self):
        #muestra los datos de la cuenta 
        print(f"titular: {self.titular}")
        print(f"cantidad {self.cantidad}")

    def ingresar (self,cantidad):
        # ingresa una cantidad ala cuenta si la cantidad es negativa no hace nada
        if cantidad > 0:
            self.cantidad += cantidad
            print(f"ingresados {cantidad:g} nuevo saldo {self.cantidad:g}") #g: si el numero es entero lo muestra sin decimales, si tiene decimales importantes los muestra
    

    def retirar (self,cantidad):
        #retirar una cantidad de la cuenta 
        self.cantidad -=cantidad 
        print(f"Retirados {cantidad:g}  Nuevo saldo: {self.cantidad:g}")



def menu():
    Cuenta = None 
    while True:
        print("\n--- Menú Cuenta Bancaria ---")
        print("1. Crear cuenta")
        print("2. Mostrar datos de la cuenta")
        print("3. Cambiar titular")
        print("4. Ingresar dinero")
        print("5. Retirar dinero")
        print("6. Salir")
        opcion = input("Elige una opción (1-6): ")
        #crear
        if opcion == "1":
            titular = input("Introduce el nombre del titular: ")
            try:
                cantidad = float(input("Introduce la cantidad inicial (puede ser 0): "))
            except ValueError:
                cantidad = 0
            Cuenta = cuenta (titular, cantidad)  
            print("¡Cuenta creada correctamente!")
        elif opcion == "2":
            if Cuenta:
                Cuenta.mostrar()
            else:
                print("Primero debes crear una cuenta.")
        elif opcion == "3":
            if Cuenta:
                nuevo_titular = input("Introduce el nuevo titular: ")
                Cuenta.titular = nuevo_titular
                print("Titular actualizado.")
            else:
                print("Primero debes crear una cuenta.")
        elif opcion == "4":
            if Cuenta:
                try:
                    cantidad = float(input("Cantidad a ingresar: "))
                    Cuenta.ingresar(cantidad)
                except ValueError:
                    print("Introduce una cantidad válida.")
            else:
                print("Primero debes crear una cuenta.")
        elif opcion == "5":
            if Cuenta:
                try:
                    cantidad = float(input("Cantidad a retirar: "))
                    Cuenta.retirar(cantidad)
                except ValueError:
                    print("Introduce una cantidad válida.")
            else:
                print("Primero debes crear una cuenta.")
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()

