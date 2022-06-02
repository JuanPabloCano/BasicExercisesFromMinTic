# 1- Realizar la carga del lado de un cuadrado.
# 2- mostrar por pantalla el perímetro del mismo (El perímetro de un cuadrado se calcula multiplicando el valor del lado por cuatro).

""" lado=(int(input("Ingrese el valor del lado del cuadrado\n")))
perimetro= lado * 4
print("El perímetro del cuadrado es: ", perimetro) """

# •	Escribir un programa en el cual se ingresen cuatro números, calcular e informar la suma de los dos primeros y el producto del tercero y el cuarto.

# 1- Ingresar 4 números
# 2- Calcular y mostrar la suma de los dos primeros
# 3- Calcular el producto del tercero y el cuarto

""" numeros=[]
for i in range(1,5):
    entrada_numeros=(int(input(f"Ingrese el número {i}: ")))
    numeros.append(entrada_numeros)
suma= numeros[0]+ numeros[1]
producto= numeros[2] * numeros[3]

print("La suma del primer y segundo número: ",suma)
print("El producto del tercer y cuarto número es: ", producto) """


# •	Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora.
# 1- Sueldo mensual del operario
# 2- Cantidad de horas trabajadas
# 3- Valor por hora

""" horas_trabajadas= int(input("Ingrese la cantidad de horas trabajadas: "))
valor_hora= int(input("Ingrese el valor por hora: "))
sueldo_mensual= horas_trabajadas * valor_hora
sueldo_mensual= sueldo_mensual * 30 # Número de días al mes
print(f"El salario mensual de un trabajador es de {sueldo_mensual} pesos")
"""

# Realizar un programa que reciba un menú de entrada funcional con operaciones aritmeticas

import os

""" def par():
    pares=(int(input("Ingrese un número: ")))
    if pares % 2 == 0:
        print("Has acertado, este número es Par")
    else:
        print("Inténtalo de nuevo")
    contin= "y"
    while contin == "y":
        x= input("Desea regresar al menú principal?: y/n ")
        if x == contin:
            menu_principal()
        else:
            print("Hasta luego")
            exit()

def promedio():
    average_list=[]
    count="s"
    while count == "s":
        num= int(input("Ingrese un número: "))
        count=input("Desea agregar otro número? s/n: ")
        average_list.append(num)
    if count == "n":
        suma = sum(average_list)
        average= suma / len(average_list)
    print(f"El promedio de los números ingresados es: {average}")
    contin= "y"
    while contin == "y":
        x= input("Desea regresar al menú principal?: y/n ")
        if x == contin:
            menu_principal()
        else:
            print("Hasta luego")
            exit()

def modulo():
    mod1 = float(input("Ingrese un número: "))
    mod2 = float(input("Ingrese el número divisor: "))
    residuo= mod1 % mod2
    print(f"El módulo la división de los números ingresados es: {residuo}")
    contin= "y"
    while contin == "y":
        x= input("Desea regresar al menú principal?: y/n ")
        if x == contin:
            menu_principal()
        else:
            print("Hasta luego")
            exit()

def porcentaje():
    lista_numeros = []
    for i in range(1,11):
        num= float(input(f"Ingrese el número {i}: "))
        lista_numeros.append(num)
    suma_numeros= sum(lista_numeros)
    porcentage= suma_numeros * 0.10
    print(f"El porcentaje de los números ingresados es: {porcentage}")
    contin= "y"
    while contin == "y":
        x= input("Desea regresar al menú principal?: y/n ")
        if x == contin:
            menu_principal()
        else:
            print("Hasta luego")
            exit()

def potencia():
    num=int(input("Ingrese un número: "))
    pot= int(input("Ingrese la potencia a elevar: "))
    result= num ** pot
    print(f"El resultado de la potencia del primer número elevado por el segundo es igual a: {result}")
    contin= "y"
    while contin == "y":
        x= input("Desea regresar al menú principal?: y/n ")
        if x == contin:
            menu_principal()
        else:
            print("Hasta luego")
            exit()

def menu_principal():
    os.system("cls")
    print("","Tenga usted un feliz día!\n",
    "Bienvenido a su menú principal, aquí encontrará diferentes opciones con las cuales podrá realizar diferentes tareas.\n",
    "Esperamos sea de total utilidad.")
    print()
    print("","1. Es par\n",
    "2. Promedio\n",
    "3. Módulo\n",
    "4. Porcentaje\n",
    "5. Potencia\n",
    "0. Salir\n")
    option= int(input("Seleccione una opción: "))
    if option == 1:
        par()
    elif option == 2:
        promedio()
    elif option == 3:
        modulo()
    elif option == 4:
        porcentaje()
    elif option == 5:
        potencia()
    elif option == 0:
        print("Ha cerrado sesión. Hasta pronto!")
        exit()    

menu_principal()"""


# Realizar un programa que muestre el IMC de un usuario y que tome datos ingresados por teclado

""" Desarrollo de variables y datos globales"""

""" weight= float(input("Ingrese su peso en KG:\n"))
height= float(input("Ingrese su altura en metros:\n"))
"""
""" Desarrollo de funciones """

""" def imc(weight, height):
    t= weight / (height ** 2)
    return round(t, 2)

def imc_values(t):

    if t == 0:
        print("Faltan datos")
        exit()
    else:
        if t < 16.00:
            print(f"Su IMC es {t} y se encuentra en el rango de delgadez severa")
        elif t >= 16.00 and t <= 16.99:
            print(f"Su IMC es {t} y se encuentra en el rango de delgadez moderada")
        elif t >= 17.00 and t <= 18.49:
            print(f"Su IMC es {t} y se encuentra en el rango de delgadez aceptable")
        elif t >= 18.50 and t <= 24.99:
            print(f"Su IMC es {t} y se encuentra en un rango normal")
        elif t >= 25.00 and t <= 29.99:
            print(f"Su IMC es {t} y se encuentra en el rango de sobrepeso")
        elif t >= 30.00 and t <= 34.99:
            print(f"Su IMC es {t} y se encuentra en el rango de obesidad tipo I, con un riesgo moderado para su salud")
        elif t >= 35.00 and t <= 39.99:
            print(f"Su IMC es {t} y se encuentra en el rango de obesidad tipo II, con un riesgo severo para su salud")
        elif t >= 40.00:
            print(f"Su IMC es {t} y se encuentra en el rango de obesidad tipo III, con un riesgo muy severo para su salud")

t=imc(weight, height)
imc_values(t)
"""


# Given two strings, determine if they share a common substring. A substring may be as small as one character.

""" def twoStrings(s1, s2):
    return "YES" if set(s1) & set(s2) else "NO" # El método set crea un conjunto que no repite elementos, y se utiliza la intersección & para imprimir los elementos iguales dentro de varios conjuntos
    
for _ in range(int(input("Ingrese la cantidad de conjuntos a evaluar: "))):
    print(twoStrings(input(f"Ingrese la palabara número {_ +1}: "), input(f"Ingrese la palabara número {_ +1}: ")))
"""

# Realizar un programa que diga si un año es bisiesto

"""def is_leap(year):
    if year % 4 == 0 and(year % 100 !=0 or year % 400 == 0): # Si es múltiplo de 4, no múltiplo de 100 pero si de 400, sería bisiesto
        print(True)
    else:
        print(False)

is_leap(int(input("Ingrese el año: ")))
"""

# Crear un programa que pida una contraseña por teclado. No podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta se imprime "Contraseña OK", sino "Contraseña errónea"

""" password=input("Ingrese la contraseña: ")
count=0

for i in range(len(password)):
    if password[i] ==" ":
        count=1
if len(password) < 8 or count > 0:
    print("Contraseña errónea")
else:
    print("Contraseña Ok") """













# Realizar un programa conversor que despliegue un menú de opciones, cuyos temas sean divisas, longitudes y operaciones algebraicas diversas


