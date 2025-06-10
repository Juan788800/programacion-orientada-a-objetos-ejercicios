#Realizar una aplicación que recoja por teclado la cantidad total a pagar y la cantidad #que se ha
#entregado. La aplicación debe calcular el cambio correspondiente con el menor número #de monedas
#y/o billetes posibles.


class aplicacion():
    def __init__(self,billetes):
        self.billetes=billetes
    

    def pagar(self):
        self.billetes