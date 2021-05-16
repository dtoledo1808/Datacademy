
def reto1():
    menu_reto1 = 1
    while menu_reto1 == 1:
        print('Bienvenido al programa para hallar el area de un triangulo')
        base,altura = input('ingresa la base y posteriormente la altura separadas por un espacio ').split()
        base = int(base)
        altura = int(altura)
        area = (base * altura) / 2
        area = int(area)
        print(f'el area es: {area}')
        menu_reto1 = int(input('''        ////quieres volver a usar este reto////
        ////1: yes   2: not = '''))


def reto2():
    menu_reto2 = 1
    while menu_reto2 == 1:
        jugadores ='''
        ***********************************************
        *Bienvenido al juego de piedra, papel o tijera*
        *********vamos a definir los jugadores*********
        ***********************************************
        ********ingresa el nombre del jugador 1******** 
        ''' 
        jugador_1 = input(f'{jugadores}')
        print('    ********ingresa el nombre del jugador 2********')
        jugador_2 = input('    ') 
        jugadas = '''
        ***********************************************
        ************exelente vamos a jugar*************
        *****************cual escoges******************
        ********************piedra*********************
        ********************papel**********************
        ********************tijera*********************
        ***********************************************  
        '''  
        puntos1 = 0
        puntos2 = 0
        while puntos1 < 3 and puntos2 < 3:
            print(jugadas)
            print(f'    *****{jugador_1.capitalize()} porfavor ingresa tu movimiento******')
            jugada_1 = input('    ')
            print(f'    *****{jugador_2.capitalize()} porfavor ingresa tu movimiento******')
            jugada_2 = input('    ')
            jugada_1 = jugada_1.lower()
            jugada_2 = jugada_2.lower()
            if jugada_1 == jugada_2:
                puntos1 += 1
                puntos2 += 1
            elif jugada_1 == 'piedra' and jugada_2 == 'tijera':
                puntos1 += 1 
            elif jugada_1 == 'tijera' and jugada_2 == 'papel':
                puntos1 += 1
            elif jugada_1 == 'papel' and jugada_2 == 'piedra':
                puntos1 += 1 
            else:
                if jugada_2 == 'papel':
                    puntos2 += 1
                elif jugada_2 == 'piedra':
                    puntos2 += 1
                elif jugada_2 == 'tijera':
                    puntos2 += 1
                else:
                    print('    ****la opcion que ingresaste no es valida****')    
        if puntos1 == puntos2:
            print('    ***************es un empate****************')
        elif puntos1 == 3:
            print(f'     *******El ganador es {jugador_1.capitalize()}********')
        elif puntos2 == 3:
            print(f'     *******El ganador es {jugador_2.capitalize()}********')
        menu_reto2 = int(input('''        ////quieres volver a usar este reto////
        ////1: yes   2: not = '''))    


def reto3():
    menu_reto3 = 1
    while menu_reto3 == 1:
        bienvenida_reto3 = '''
        ////Bienvenido al conversor de millas a kilómetros////
        ////ingresa 1 para convertir millas a kilometros////
        ////ingresa 2 para convertir kilometros a millas////
        ////'''
        tipo_reto3 =int(input(f'{bienvenida_reto3}'))
        if tipo_reto3 == 1:
            millas = float(input(f'    ////ingresa la cantidad de millas: '))
            kilometros = millas * 1.609344 
            print(f'        ////Exelente {millas} millas es igual a {round(kilometros,1)} kilometros////')
        elif tipo_reto3 == 2:
            kilometros = float(input(f'    ////ingresa la cantidad de kilometros: ')) 
            millas = kilometros / 1.609344 
            print(f'        ////Exelente {kilometros} kilometros es igual a {round(millas,1)} millas////')
        menu_reto3 = int(input('''        ////quieres volver a usar este reto////
        ////1: yes   2: not = '''))    


def reto4():
    menu_reto4 = 1
    while menu_reto4 == 1:
        bienvenida_reto4 = '''
        ////bienvenido al programa para calcular volumenes////
        ////ingresa de que figura deseas saber el volumen////
        ////1 para un cilindro////
        ////2 para un cubo////
        ////3 para un prisma triangular////
        ////cual necesitas: '''
        tipo_reto4 = int(input(f'{bienvenida_reto4}'))
        if tipo_reto4 == 1:
            radio =float(input(f'////ingresa el radio en cm:')) 
            altura = float(input('////ingresa la altura en cm:'))
            volumen = 3.14159265359 * ((radio * radio)*altura)
            print(f'////el volumen de un cilindro con un radio de {radio}cm2 y una altura de {altura}cm es de {round(volumen,1)}cm3////')
        elif tipo_reto4 == 2:
            lado = float(input('////ingresa uno de los lados en cm: '))
            volumen = lado * lado * lado
            print(f'////el volumen de un cubo con lados de {lado}cm es de {round(volumen,1)}cm3')
        elif tipo_reto4 == 3:
            longitud = float(input('////ingrese la longitud en cm: '))
            ancho = float(input('////ingresa en ancho en cm: '))
            altura = float(input('////ingresa el alto en cm: '))
            volumen = (longitud * ancho) / 2 * altura
            print(f'////el volumen de el prisma es {volumen}cm3')
    menu_reto4 = int(input('''        ////quieres volver a usar este reto////
    ////1: yes   2: not = '''))    


def reto5():
    menu_reto5 = 1
    while menu_reto5 == 1:
        bienvenida_reto5 ='''
        ////Bienvenido a este jueguito///
        ////a continuación ingresaras 3 números////
        ////el primero como tu numero mas grande////
        ////el segundo como tu numero mas pequeño////
        ////tu tercer numero debería ser un numero en el rango////
        ////no te preocupes yo te visare si tu tercer numero esta en el rango////
        '''
        superior = int(input(f'{bienvenida_reto5}////ingresa tu numero mas grande:'))
        inferior = int(input(f'    ////ingresa tu numero mas pequeño: '))
        comparacion = int(input(f'    ////ingresa tu numero de comparacion: '))
        while superior <= comparacion or inferior >= comparacion:
                if superior <= comparacion:
                    if superior == comparacion:
                        print(f'    ////tu numero de comparacion es igual a tu numero superior')
                        comparacion = int(input(f'    ////ingresa un nuevo numero de comparacion: '))
                    else:
                        print(f'    ////tu numero de comparacion es superior a el que ingresaste como tu numero mas grande')
                        comparacion = int(input(f'    ////ingresa un nuevo numero de comparacion: '))
                elif inferior >= comparacion:
                    if inferior == comparacion:
                        print(f'    ////tu numero de comparacion es igual a tu numero inferior')
                        comparacion = int(input(f'    ////ingresa un nuevo numero de comparacion: '))
                    else:
                        print(f'    ////tu numero de comparacion es menor a el que ingresaste como tu numero inferior')
                        comparacion = int(input(f'    ////ingresa un nuevo numero de comparacion: '))
        print(f'    ////exelente {comparacion} esta en rango de {inferior} y {superior}')     
        menu_reto5 = int(input('''        ////quieres volver a usar este reto////
        ////1: yes   2: not = '''))    


def run():
    inicio = 0
    a = 0
    while inicio == 1 or a == 0:
        saludo = '''
        ///////////////////////////////////
        ////Bienvenido////
        ////escoge el programa que deseas usar////
        ////1 para Reto 1 - Área de un triángulo////
        ////2 para Reto 2 - Piedra, papel o tijera////
        ////3 para Reto 3 - Conversor de millas a kilómetros////
        ////4 para Reto 4 - Calculadora de volúmenes////
        ////5 para Reto 5 - Rangos cambiantes////
        /////////////////////////////////////////
        ////a cual quieres ingresar: '''
        menu = int(input(f'{saludo}'))
        a += 1
        if menu == 1:
            reto1()
        elif menu == 2:
            reto2()
        elif menu == 3:
            reto3()    
        elif menu == 4:
            reto4()
        elif menu == 5:
            reto5()
        inicio = int(input('''        ////quieres volver al menu principal///
        ////1: yes   2: not  =  ''')) 
        print('       ////gracias por usar el programa////')
        print('       ///////////////ADIOS////////////////')
     

if __name__ == '__main__':
    run()