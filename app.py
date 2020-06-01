from cuenta import Cuenta, CuentaJoven


def new_user(usuario,new_saldo=0):
    imprimir_usuario=list(user.mostrar())
    print('NOMBRE Usuario : ',imprimir_usuario[0])
    print('SALDO Usuario: ',imprimir_usuario[1])
    
def depositarDinero(monto_deposito):
    depositar=user.ingresar(monto_deposito)
    if depositar==None:
        pass
    else:
        depositar=list(depositar)
        print('Dinero Depositado: ', depositar[1])
        print('Nuevo Saldo Disponible: ', depositar[0])


def retirarDinero(monto_retirar):
    retirar=list(user.retirar(monto_retirar))
    print('Dinero Retirado: ', retirar[1])
    print('Nuevo Saldo Disponible: ', retirar[0])

### CUENTA JOVEN ###
def mostrar_cuentaJoven(usuario,edad, new_saldo=0):
    imprimir_usuario_cuentajoven=user_cuenta_joven.mostrar()
    print(imprimir_usuario_cuentajoven[0])
    print('Nombre de usuario Cuenta Joven: ',imprimir_usuario_cuentajoven[1])
    print('EDAD de usuario Cuenta Joven: ',edad)
    print('Saldo Nuevo Usuario: ',imprimir_usuario_cuentajoven[2])
    print('Bonificacion: ',imprimir_usuario_cuentajoven[3])

def depositarDineroCuentaJoven(monto_deposito):
    depositar=user_cuenta_joven.ingresar(monto_deposito)
    if depositar==None:
        pass
    else:
        depositar=list(depositar)
        print('Dinero Depositado: ', depositar[1])
        print('Nuevo Saldo Disponible: ', depositar[0])

def evaluacion_titular(edad):
    evaluacion_edad=user_cuenta_joven.esTitularValido(edad)
    return evaluacion_edad

def retirarDineroCuentaJoven(edad, monto_retiro):
    retiro_cuenta_joven=list(user_cuenta_joven.retirar(edad, monto_retiro))
    print('Dinero Retirado: ', retiro_cuenta_joven[1])
    print('Nuevo Saldo Disponible: ', retiro_cuenta_joven[0])


print('''
What would you like to do (type a number and press Enter)?\n
1.- Desea Crear Usuario? \n2.-Salir
    ''')
opcioninicial=input()
if '1' in opcioninicial:
    print('Ingrese el Nombre de usuario: ')
    usuario=input()
    print('Ingrese LA EDAD del usuario: ')
    edad=int(input())         

    if edad<18:
        print('No puedes aperturar una cuenta por ser MENOR de edad')

    elif 18<=edad<=25:
        print('Desea ingresar dinero de Apertura a su cuenta JOVEN? \n1.-SI \n2.-NO \n')  
        respuesta=input()
        if '1' in respuesta:    
            print('Ingrese el monto de Apertura: ')  
            monto_apertura=float(input())
            if monto_apertura<0:
                print('No puedes ingresar numeros negativos we \n')
        else:
            monto_apertura=0   
        user_cuenta_joven=CuentaJoven(titular=usuario,cantidad=monto_apertura,bonificacion='30')
        edad_valida=evaluacion_titular(edad)
        print('\n')
        mostrar_cuentaJoven(usuario,edad,monto_apertura)
            
    else:
            print('Desea ingresar dinero de Apertura a su cuenta? \n1.-SI \n2.-NO \n')  
            respuesta=input()
            if '1' in respuesta:    
                print('Ingrese el monto de Apertura: ')  
                monto_apertura=float(input())
                if monto_apertura<0:
                    print('No puedes ingresar numeros negativos we \n')
            else:
                monto_apertura=0     
            print('\n')
            user=Cuenta(titular=usuario,cantidad=monto_apertura) 
            new_user(usuario,monto_apertura)
else:
    print('Hasta pronto')       

if '1' in opcioninicial:
    stop = False
    while stop == False:
        
        print('''
    What would you like to do (type a number and press Enter)?
    - Type 1: DEPOSITAR DINERO a su cuenta.
    - Type 2: RETIRAR DINERO de su cuenta.
    - Type 3: MOSTRAR USER Y DINERO de su cuenta.
    - Type 4: To quit
        ''')

        option = int(input("Enter a number:"))
        # add your options here using conditionals (if)    
        try: 
            if option == 1:
                print('Ingrese el monto a Depositar: ')  
                monto_depositar=float(input())
                print('\n')
                if 18<=edad<=25:
                    depositarDineroCuentaJoven(monto_depositar)
                else:
                    depositarDinero(monto_depositar) 
            if option == 2:
                print('Ingrese el monto a Retirar: ')  
                monto_retirar=float(input())
                if 18<=edad<=25:
                    print('\n')
                    retirarDineroCuentaJoven(edad_valida,monto_retirar)
                else:
                    print('\n')
                    retirarDinero(monto_retirar)
                    
            if option == 3:
                if 18<=edad<=25:
                    mostrar_cuentaJoven(usuario,edad)
                else:
                    new_user(usuario)
                    
            if option==4:
                print("Bye bye!")
                stop = True             
        except IndexError as e:
            print(e)