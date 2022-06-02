# Estructuras iterativas, son bucles. Repiten instrucciones varias veces
# While es una bucle infinito, que no se detendrá hasta que no se le ordene
# For es un bucle finito que siempre se va a detener
#Realizar un programa que imprima los números de 1 a 100

# While examples:

"""x=1
while x<=100:   # Mientras x sea mayor o igual a 100, la x incrementa su valor en 1 hasta llegar a la condición 100
    print(x)
    # x=x+1 
    x += 1  """        # Esto reemplaza la forma como está escrita el comentario superior.
    

# Hacer un programa que imprima despliegue el número que ha sido ingresado
"""num=0
x=int(input("Numero: "))
while num <= x:
    print(num)
    num+=1 """

""" clase= 8 
while clase <= 12:
    print(clase, "Clase en proceso")
    if clase == 12:
        print("Clase finalizada")
    clase += 1  """

""" num=0
while num<=50:
    print(num ,("Hecho"))
    num +=  1
    if num==40:
        print("Finalizado")
        break """
        
# Desarrollar un programa que tome un valor ingresado por teclado y haga la cuenta hasta ese número

""" n=int(input("Ingrese un valor: "))
x=1
while x<=n:
    print(x)
    x=x + 1
print("Finalice la ejecución") """

# Desarrollar un programa que permita ingresar 5 valores por teclado y muestre la suma de esos valores y el promedio

""" x = 1  # La variable x funciona como un contador, para llevar un control del programa y pueda detenerse correctamente
suma = 0
while x <= 5:
    valor = float(input("Ingrese el valor " + str(x) + ": "))
    suma = suma + valor
    x += 1
promedio = suma / 5
print("La suma de los valores es:", round(suma))
print("El promedio de los valores es:", promedio) """

# Calcular el promedio de números ingresador por teclado hasta que el usuario decida terminar el programa

""" total = 0
count = 0
while (True):  # While True hará que el programa funcione hasta que el usuario no utilice el comando para el break
    inp = input('Enter a number: ')
    if inp == 'done': break   # Con la función break se controla que el usuario pueda finalizar el ingreso de números cuando lo requiera
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print('Average:', average) """

# Una planta que fabrica perfiles de hierro posee un lote de n piezas.Confeccionar un programa que pida ingresar porteclado la cantidad de piezas a procesar y luego ingrese la longitud de cada perfil; sabiendo que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en el lote. 

""" x = 1
cantidad = 0
n = int(input("Ingrese la cantidad de piezas: "))
while x <= n:
    longitud = float(input("Ingrese la longitud: "))
    if longitud >= 1.20 and longitud <= 1.30:
        cantidad= cantidad + 1
    x += 1
print("La cantidad de piezas aptas son:", cantidad)"""


""" Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste
exactamente sí (en minúsculas y con tilde) """

""" print("Escriba sí para continuar")
respuesta = input("Desea continuar con el programa?: ")
while respuesta == "sí":
    respuesta = input("Desea continuar con el programa?: ")    
print("Hasta la vista!!") """

""" Escriba un programa que pregunte una y otra vez si desea terminar el programa, salvo si se contesta exactamente SI
(en mayúsculas y sin tilde) """

""" print("Debe escribir sí!")
respuesta = input("Desea terminar con el programa? ")
while respuesta != "sí":
    respuesta = input("Desea terminar con el programa? ")
print("Hasta luego") """

""" Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar
hasta que las dos contraseñas coincidan. """

""" print("Confirme su contraseña")
contraseña_1= input("Ingrese su contraseña\n")
contraseña_2= input("Ingrese de nuevo su contraseña\n")
while contraseña_1 != contraseña_2:
    print("Las contraseñas no coinciden, inténtelo de nuevo")
    contraseña_1= input("Ingrese su contraseña\n")
    contraseña_2= input("Ingrese de nuevo su contraseña\n")
print("Contraseña confirmada") """

""" Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de 
dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando,
hasta que el total ahorrado iguale o supere al objetivo. El programa no comprobará que las cantidades sean positivas. """

""" print("Hora de ahorrar")
objetivo= float(input("Cuanto desea ingresar?: "))
total_ahorrado= 0
while  objetivo > total_ahorrado:
    total_ahorrado += float(input("Cuanto quiere ahorrar?: "))
print(f" Muy bien! Ha ahorrado {total_ahorrado} ") """


# For examples:
# For variable in elementos (lista, cadena, range, etc):--- Sintaxis
# En general se usa para las situaciones en las que se quiere que una variable tome un valor de una lista definida

""" print("Comienzo")
for i in [0,1,2,3,4]:
    print("Hola",i, end=" ")
print()
print("Final") """

""" print("Comienzo")
for i in range (1,16,2): # El tercer número indica los saltos, en este caso saltaría de dos en dos
    print(f"Hola soy el número:{i}")
print("Final") """

# Programa que acepte la entrada por teclado de 10 valores y que muestre la suma y el promedio

""" suma=0
for i in range (1,11):
    valor=int(input(f"Ingrese el valor # {i} :"))
    suma+= valor
promedio= suma / i
print(f"La suma es: {suma}")
print(f"El promedio es: {promedio}") """

# realizar un programa que imprima en pantalla los números del 0 al 100

""" print("BIENVENIDOS A LA CUENTA")
for i in range(101):
    print(f"Este es el número: {i}")
print("Bien hecho!") """

# Imprimir cada letra de una palabra

""" word="Esternocleidomastoideo"
for i in "Esternocleoidomastoideo":
    print(i)
print("En total son:", len(word), "palabras") """


# For comprimido

# Hacer una lista que se llene con números del 1 al 100

"""l= [i for i in range(1,101)]
print(l)"""


# Organizar los números de la lista de mayor a menor usando sort()

"""a=[3,69,1,4,7,12,40,38,90,100,17,65,34,89,76,45,38,76,91]
print(f"Lista desordenada: {a}")
nums=[i for i in a]
nums.sort()
print(f"Lista ordenada: {nums}")"""

# Hacer un programa que arroje números pares e impares

"""z=[i for i in range(101)]
l=[i for i in range(len(z)) if i % 2 == 0]
a=[i for i in range(len(z)) if i % 2 != 0]
print(f"Pares: {l}")
print(f"Impares: {a}")"""



# Hacer un programa con booleanos que me pida una dirección de email, repetir la pregunta hasta que el email contenga @ y .com, imprimir mensaje de error o de sesión iniciada.

# Hacer un programa con conteo de intentos que me pida una dirección de email, repetir la pregunta hasta que el email contenga @ y .com, imprimir mensaje de error si supera 3 intentos fallidos o de sesión iniciada.



