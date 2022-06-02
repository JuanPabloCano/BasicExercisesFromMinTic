import math,time,os
import matplotlib.pyplot as plt
import numpy as np

operaciones= ["Suma", "Resta", "Multiplicación", "Logaritmo", "Coseno", "Seno", "Raíz cuadrada", "Convertir decimal a binario", "Convertir binario a decimal", "Salir"]

def addition():
    ul=[]
    u= int(input("Cuantos números desea ingresar?\n"))
    for i in range(u):
        entry= int(input(f"Ingrese el número {i+1}: "))
        ul.append(entry)

    o_n=(input("Desea ingresar más números?\n"))
    if o_n != "si":
        suma= sum(ul)
        print(f"La suma de los valores ingresados es: {suma}")
        time.sleep(2)
        os.system("cls")
    else:
        c_n= int(input("Cuantos números extra desea ingresar?\n"))
        for j in range(c_n):
            new_entry= int(input(f"Ingrese el valor extra número {j+1}: "))
            ul.append(new_entry)
        add_final= sum(ul)
        print(f"La suma de todos los valores ingresados es: {add_final}")
        time.sleep(2)
        os.system("cls")

def substraction():
    ul=[]
    u= int(input("Cuantos números desea ingresar?\n"))
    for i in range(u):
        entry= int(input(f"Ingrese el número {i+1}: "))
        ul.append(entry)

    o_n=input("Desea ingresar más números?\n")
    if o_n != "si":
        for k in range(len(ul)-1):
            resta= ul[0] - ul[k+1]
        print(f"La resta de los valores ingresados es: {resta}")
        time.sleep(2)
        os.system("cls")

    else:
        c_n= int(input("Cuantos números extra desea ingresar?\n"))
        for j in range(c_n):
            new_entry= int(input(f"Ingrese el valor extra número {j+1}: "))
            ul.append(new_entry)
        for x in len(ul):
            sub_final= ul[x] - ul[x+1]
        print(f"La suma de todos los valores ingresados es: {sub_final}")
        time.sleep(1)
        os.system("cls")

def multipl():
    ul=[]
    u= int(input("Cuantos números desea ingresar?\n"))
    for i in range(u):
        entry= int(input(f"Ingrese el número {i+1}: "))
        ul.append(entry)

    o_n=(input("Desea ingresar más números?\n"))
    if o_n != "si":
        multi= math.prod(ul) # Función .prod de la librería math que sirve para multiplicar los elementos de la lista
        print(f"La multiplicación de los valores ingresados es: {multi}")
        time.sleep(2)
        os.system("cls")

    else:
        c_n= int(input("Cuantos números extra desea ingresar?\n"))
        for j in range(c_n):
            new_entry= int(input(f"Ingrese el valor extra número {j+1}: "))
            ul.append(new_entry)
        multi_final= math.prod(ul)
        print(f"La multiplicación de todos los valores ingresados es: {multi_final}")
        time.sleep(2)
        os.system("cls")


def logaritm():
    base= int(input("Ingrese la base:\n"))
    x= int(input("Ingrese el número:\n"))
    l= math.log(x,base)
    print(f"El resultado del logaritmo Log{x}{base} es: {l}")
    time.sleep(2)
    os.system("cls")

""" def cosin():

def sine():

def square_root():

def decimal_binary():

def binary_decimal():
"""


def math_menu(operaciones):
    print("",str("1."),operaciones[0],"\n", 
    str("2."),operaciones[1],"\n",
    str("3."),operaciones[2],"\n",
    str("4."),operaciones[3],"\n",
    str("5."),operaciones[4],"\n",
    str("6."),operaciones[5],"\n",
    str("7."),operaciones[6],"\n",
    str("8."),operaciones[7],"\n",
    str("9."),operaciones[8], "\n",
    str("10."),operaciones[9], "\n")
    selection=int(input("Escoja una opción: "))
    return selection

def math_selection():
    count= 0
    selection=1
    while count != 3 and selection != 10:
        selection=math_menu(operaciones)
        if selection <= 0 or selection > 10:
            print("Los números ingresados no concuerdan con nuestro menú, por favor inténtelo de nuevo")
            time.sleep(1)
            os.system("cls")
            count +=1
        if count == 3:
            print("Ha alcanzado el límite máximo de oportunidades, por favor inténtelo más tarde")
            exit()
        else:
            if selection == 1:
                addition()
            elif selection == 2:
                substraction()
            elif selection == 3:
                multipl()
            elif selection == 4:
                logaritm()
            elif selection== 5:
                cosin()
            elif selection == 6:
                sine()
            elif selection == 7:
                square_root()
            elif selection == 8:
                decimal_binary()
            elif selection == 9:
                binary_decimal()
            elif selection == 10:
                print("Hasta luego")
                exit()

math_selection()