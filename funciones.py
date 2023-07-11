import numpy as np
import os
import time

lista_rut = []
lista_nombre = []
lista_apellido = []
lista_entrada = []
lista_platinum = []
lista_gold = []
lista_silver = []
lista_fila = []
lista_columna = []
cont_platinum = 0
cont_gold = 0
cont_silver = 0
t_platinum = 0
t_gold = 0
t_silver = 0

platinum = 120000
gold = 80000
silver = 50000


def mostrar_menu ():
    print('''Bienvenido al menú de "Creativos.cl", 
    1.Comprar Entrada
    2.Mostrar Ubicaciones Disponibles
    3.Ver Listado de Asistentes
    4.Mostrar Ganancias Totales
    5.Salir
    ''')

def validar_opcion():
    while True:
        try:
            opc = int(input("Escoga una opción del menú (1 a 5): "))
            if opc in (1,2,3,4,5):
                return validar_opcion
            else:
                print("ERROR! Debe escoger una opción dentro del menú")
        except:
            print("ERROR! Debe seleccionar un número entero")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut (Sin punto ni digíto verificador: "))
            if len(str(rut)) >= 7 and len(str(rut)) <=8:
                lista_rut.append(rut)
                return validar_rut
            else:
                print("ERROR! El rut no cumple con los solicitado")
        except:
            print("ERROR! No es un número entero")

def validar_nombre(): #No sirve, pq no sabia que eran mis datos, pero para ver si estan bien
    while True:
        nom = input ("Ingrese su nombre: ")
        if len(nom)>=3:
            lista_nombre(nom)
            return validar_nombre
        else:
            print("ERROR! El nombre no cumple con los requisitos")

def validar_apellido(): #No sirve, pq no sabia que eran mis datos, pero para ver si estan bien
    while True:
        apellido= input ("Ingrese su apellido: ")
        if len(apellido)>=3:
            lista_apellido(apellido)
            return validar_apellido
        else:
            print("ERROR! El apellido no cumple con los requisitos")

def validar_entrada():
    while True:
        try:
            entrada = int(input("Ingrese las entradas que desea comprar (1 a 3): "))
            if entrada >= 1 and entrada <= 3:
                lista_entrada (entrada)
                return validar_entrada
            else:
                print("ERROR! La cantidad de entradas es incorrecta")
        except:
            print("ERROR! La cantidad no es un número entero")

def validar_dia(): #No sirve, pq no sabia que eran mis datos, pero para ver si estan bien
    while True:
        try: 
            dia = int(input("Ingrese el día en el cuál comprara las entradas (Solo el día)"))
            if dia>= 1 and dia<=31:
                return validar_dia
            else:
                print("ERROR! El día escogido no existe")
        except:
            print("ERROR! El día elegido no es un número entero")

def mostrar_escenario():
    escenario = np.zeros((10,10),int)
    print("           _________________ ")
    print("          |                 |")
    print("          |    ESCENARIO    |")
    print("          |_________________|")
    print("")
    for x in range(10):
        print (f"Fila {x+1}:", end=" ")
        print(" ")
    for y in range(10):
        print (escenario [x][y], end=" ")
        print(" ")
print ("Columna:  1 2 3 4 5 6 7 8 9 10")
        

def validar_fila():
    while True:
        try: 
            fila = int(input("Ingrese la fila donde desea comprar las entradas"))
            if fila >= 1 and fila<=10:
                return validar_fila
            else:
                print("ERROR! La fila escogida no existe")
        except:
            print("ERROR! La fila elegida no es un número entero")

def validar_columna():
    while True:
        try: 
            columna= int(input("Ingrese la columna donde desea comprar las entradas"))
            if columna >= 0 and columna<=9:
                return validar_columna
            else:
                print("ERROR! La columna escogida no existe")
        except:
            print("ERROR! La columna elegida no es un número entero")


def comprar_entrada():
    rut = validar_rut()
    escenario = mostrar_escenario()
    entrada = validar_entrada()
    for ubi in range (entrada):
        fila = validar_fila()
        columna = validar_columna()

        
    
    while True:
        if fila >= 0 and fila <=2:
            val_fila = platinum
            cont_platinum = cont_platinum + 1
        elif fila >=3 and fila <=5:
            val_fila = gold
            cont_gold = cont_gold + 1
        elif fila >=6 and fila <= 10:
            val_fila = silver
            cont_silver = cont_silver + 1
        break

    while True:
        if entrada == 1:
            print("Gracias por comprar su entrada")
        else:
            print("Gracias por comprar sus entradas")
        break

def mostrar_ubi_dis():
    pass

def ver_lista_asis():
    print (lista_rut.sort())

def mostrar_ganancias_t():
    t_platinum = platinum*cont_platinum
    t_gold = gold*cont_gold
    t_silver = silver*cont_silver
    t_cont = cont_platinum + cont_gold + cont_silver
    total = t_platinum + t_gold + t_silver

    print(f"""
 __________________________________________________________
|    Tipo Entrada     |    Cantidad    |       Total       |
|----------------------------------------------------------|
|Platinum ${platinum}     |       {cont_platinum}        |         {t_platinum}         |
|Gold     ${gold}      |       {cont_gold}        |         {t_gold}         |
|Silver   ${silver}      |       {cont_silver}        |         {t_silver}         |  
|----------------------------------------------------------|
|TOTAL                |       {t_cont}        |         {total}         |
|__________________________________________________________|    
""")
    
def salir ():
    nom = "Matías"
    ape = "Recabarren"
    dia = "11/07/2023"
    while True:
        print(f"""
            Muchas gracias por visitar nuestra página {nom} {ape}, que tenga buen día.
            Fecha visita: {dia}""")
        break
        
