""" nombre=input("Ingrese su nombre")
print("Caracter seleccionado")
print(nombre[0]) # Sintaxis para hacer que el programa imprima el caracter selecccionado
print("Cantidad de letras del nombre")
print(len(nombre)) """

""" nombre1="mAriA"
print(nombre1)
nombre2=nombre1.upper()
print(nombre2)
nombre3=nombre1.lower()
print(nombre3)
nombre4=nombre1.capitalize()
print(nombre4) """

# Las funciones se utilizan para dividir un programa de forma estructurada

# Hacer un programa que muestra una presentación en pantalla, solicite la carga de 2 valores y muestre la suma de ellos

# Declaración de funciones

""" def presentación():
    print("Programa permite cargar dos valores por teclado")
    print("Efectúa la suma de los valores")
    print("Muestra el resultado de la suma")
    print("************************")
    
def carga_suma():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese el segundo valor: "))
    suma=valor1+valor2
    print("la suma de los dos valores es: ", suma)

def finalizacion():
    print("**************************")
    print("Gracias por utilizar este programa")

# Programa principal

presentación()       # Acá se llaman a las funciones 
carga_suma()
finalizacion()"""

# Hacer un programa que muestra una presentación en pantalla, solicite la carga de 2 valores y muestre la suma de ellos
# Y lo muestre 5 veces y finalice con una separación.

""" def carga_suma():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese el segundo valor: "))
    suma=valor1+valor2
    print("la suma de los dos valores es: ", suma)

def separacion():
    print("********************************")

#Programa principal

for x in range(5):
    carga_suma()
    separacion() """

# Hacer una función que le enviemos como parametro el valor del lado de u cuadrado y retorne la sueprficie

""" def retornar_superficie(lado):
    sup=lado*lado
    return sup

# Bloque principal

va=int(input("Ingrese el valor del lado del cuadrado: "))
superficie= retornar_superficie(va)
print("La superficie del cuadrado es:", superficie) """


# Ejemplo de un menú con operaciones básicas matemáticas usando la función Def

""" def menu():
    print("App de operaciones.")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    op = int(input ("Escriba la opcion:"))
    #op = int(op)
    if op==1: suma()
    elif op==2: resta()
    elif op==3: multiplicacion()
    elif op==4: division()
    else: exit()
    
def suma():
    print("")
    print ("Hacer sumas.")
    num1 = input("Numero 1: ")
    num2 = input("Numero 2: ")
    num1 = float(num1)
    num2 = float(num2)
    print ("Resultado: ", num1+num2)
    print("")
    menu()
    
def resta():
    print("")
    print ("Hacer restas.")
    num1 = input("Numero 1: ")
    num2 = input("Numero 2: ")
    num1 = float(num1)
    num2 = float(num2)
    print ("Resultado: ", num1-num2)
    print("")
    menu()
def multiplicacion():
    print("")
    print ("Hacer multiplicacion.")
    num1 = input("Numero 1: ")
    num2 = input("Numero 2: ")
    num1 = float(num1)
    num2 = float(num2)
    print ("Resultado: ", num1*num2)
    print("")
    menu()
def division():
    print("")
    print ("Hacer division.")
    num1 = input("Numero 1: ")
    num2 = input("Numero 2: ")
    num1 = float(num1)
    num2 = float(num2)
    print ("Resultado: ", num1/num2)
    print("")
    menu()
menu() """

# FUNCIONES Y LISTAS En una empresa se almacenaron los sueldos de 10 personas. Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
# 1) Carga de los sueldos en una lista. 
# 2) Impresión de todos los sueldos. 
# 3) Cuántos tienen un sueldo superior a $4000. 
# 4) Retornar el promedio de los sueldos.
# 5) Mostrar todos los sueldos que están por debajo del promedio.

# Crear funciones para cada uno de los bloques

""" def entrada_sueldos():
    salario=[]
    for i in range(1,11):
        sueldos1=int(input(f"Ingrese el sueldo {i}: "))
        salario.append(sueldos1)
    return salario
    

def impresion(sueldos):
    print("Listado de sueldos")
    for x in range(len(sueldos)):  # Longitud de la lista
        print(sueldos[x])

def sueldos_mayores_4000(sueldos):
    cantidad=0
    for x in range(len(sueldos)):
        if sueldos[x] >= 4000:
            cantidad +=1
    print("Cantidad de empleados con sueldos superiores a 4000:", cantidad)

def promedio(sueldos):
    suma=0
    for x in range(len(sueldos)):
        suma= suma + sueldos[x]
    promedio= suma / len(sueldos)
    return promedio

def sueldos_menores(sueldos):
    pro=promedio(sueldos)
    print("El sueldo promedio es:", pro)
    print("Los sueldos inferiores al promedio:")
    for x in range (len(sueldos)):
        if sueldos[x] <= pro:
            print(sueldos[x])

# Bloque principal

sueldos= entrada_sueldos()
impresion(sueldos)
sueldos_mayores_4000(sueldos)
sueldos_menores(sueldos) """

# La palabra clave Global nos sirve para modificar una variable por fuera de la función actual. Es usada para crear una variable gobal y hacer cambios en ella de manera local

""" c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c) """

# Global en un def anidado

""" def foo():
    x = 20  

    def bar():
        global x 
        x = 25
    
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main: ", x) """

# Otro ejemplo

""" x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo() """

# No hay necesidad declarar una variable global dentro de una función para acceder a ella

""" # global variable
a = 15
b = 10

# function to perform addition
def add():
    c = a + b
    print(c)

# calling a function
add() """


# Para cambiar esa variable global si es necesario declararla dentro de la función

""" # global variable
a = 15

def add():
    global a
    a += 5
    print(a)

# calling a function
add() """

# Hacer una función con un parámetro que ingrese datos por teclado y arroje salida mediante return

""" def various_return_types(n):
    if(n==1):
        return "Hello World."   # Return a string
    elif(n==2):
        return 42               # Return a value
    else:
        return True             # Return a boolean

print(various_return_types(int(input("Ingrese un número entre 1 y 3: ")))) """