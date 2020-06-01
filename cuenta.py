class Cuenta:
    def __init__(self, titular,cantidad):
        self.titular=titular
        self.cantidad=cantidad
        
    def mostrar(self):
        return self.titular, self.cantidad
    
    def ingresar(self, monto_deposito):
        if monto_deposito<0:
            print('No puedes depositar este monto negativo')
        else:
            self.cantidad=self.cantidad+monto_deposito
            return self.cantidad, monto_deposito
        pass
    
    def retirar(self, monto_retiro):
        if monto_retiro<0:
            print('No puedes retirar este monto negativo')
            return self.cantidad, 0
        elif self.cantidad<monto_retiro:
            print('No posees esta cantidad disponible en tu cuenta')
            return self.cantidad, 0
        else:
            self.cantidad=self.cantidad-monto_retiro
            return self.cantidad, monto_retiro
    
class CuentaJoven(Cuenta):
    def __init__(self, titular,cantidad, bonificacion):
       Cuenta.__init__(self, titular, cantidad)
       self.bonificacion=bonificacion
        
    def mostrar(self):
        mensaje='Cuenta Joven'
        return mensaje,self.titular, self.cantidad, self.bonificacion
        pass
        
    def esTitularValido(self,edad):
        if 18<=edad<=25:
            return True
        else:
            return False
    
    def retirar(self,edad, monto_retiro):
        if edad ==True:
            if monto_retiro<0:
                print('No puedes retirar este monto negativo')
                return self.cantidad, 0
            elif self.cantidad<monto_retiro:
                print('No posees esta cantidad disponible en tu cuenta')
                return self.cantidad, 0
            else:
                self.cantidad=self.cantidad-monto_retiro
                return self.cantidad, monto_retiro
    
