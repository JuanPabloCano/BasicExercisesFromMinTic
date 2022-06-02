# Son variables que almacenan arrays, son heterogeneas y pueden estar conformadas
# por elementos de distintos tipos, incluidas otras listas.
# Se usan mediante []

""" lista1=[1,2,3,4,5,6,7,8,9] # Lista de enteros
print(lista1) """

""" lista2=["Lunes,Martes,Miercoles,Jueves"] # Lista de strings
print(lista2) """

""" lista3=["Lunes", 4, 3.6] # Lista con diferentes tipos de elementos
print(lista3) """

# Definir una lista que almacene 5 enteros, sumarlos y mostrar la suma

""" lista=[10, 34, 43, 8, 76]
suma=0
x=0
while x<len(lista): # Mientras que x sea menor que el RECORRIDO de la lista, o sea, recorre 5 veces, capturando cada elemento de ella
    suma=suma+lista[x] # X es la posición cero
    print(f"El elemento de la lista que está en la posición {x} es: {lista[x]}")
    x+=1
print("Los elementos de la lista son: ")
print(lista)
print("La suma de los elementos es: ", suma) """

# Hacer una lista que almacena los nombres de los primeros cuatro meses del año, que muestre el primero y el último

""" meses=["Enero", "Febrero", "Marzo", "Abril"]
print(len(meses))
meses.append("Mayo") # Append asigna un nuevo elemento en la última posición
print(f"El primer mes de la lista es: {meses[0]}") # De esta forma se escoge un elemento especifico de la lista, comenzando desde cero
print(f"El último mes de la lista es: {meses[4]}") """

# Hacer un programa que me muestre el nombre del estudiante y sus dos últimas notas, calcular el promedio

""" lista=["Ana", 7, 9]
print("Nombre del estudiante:" ) 
print(lista[0])
promedio= (lista[1] + lista[2]) //2
print("Promedio de sus dos notas es: ", promedio) """

# Hacer una lista vacía que añada datos por teclado

""" lista=[]
for i in range(5):
    dato=(input(f"Ingrese el dato {i+1}:  "))
    lista.append(dato)
print(lista) """

# Hacer un programa que tome datos por teclado y si encuentra un cero, se detenga

""" lista=[]
valor=int(input("Ingresar valor (0 para finalizar): "))
while valor!=0:
    lista.append(valor)
    valor=int(input("Ingresar valor (0 para finalizar): "))
print("El tamaño de la lista es:", len(lista)) """

# Hacer una lista que recoja datos por teclado y me muestre el número mayor

""" lista=[]
for x in range(5):
    valor=int(input("Ingrese valor: "))
    lista.append(valor)

mayor=lista[0]
for x in range(1,5):
    if lista[x] > mayor:
        mayor=lista[x]

print("Lista completa")
print(lista)
print("Mayor de la lista")
print(mayor) """

# Listas pararlelas, cuando hay relación entre los componentes de igual subindice (misma posición) de una lista y otra

# Desarrollar un programa que recoja datos por teclado de 5 nombres y sus edades. Luego imprima los nombres de los mayores de edad

""" nombres=[]
edades=[]
for i in range(5):
    nom=input("Ingrese el nombre de la persona: ")
    nombres.append(nom)
    ed=int(input("Ingrese la edad de la persona: "))
    edades.append(ed)

print("nombre de las personas mayores de edad: ")
for i in range(5):
    if edades[i] > 18:
        print("El nombre de la persona es: ", nombres[i]) """


# Hacer listas desordenadas y que ordene el número mayor al final

""" sueldos=[]
for x in range(5):
    valor=int(input("Ingrese sueldo: "))
    sueldos.append(valor)
print("Lista sin ordenar")
print(sueldos)

for x in range(len(sueldos)-1):
    if sueldos[x] > sueldos[x+1]:    # La x representa la posición cero en la lista
        aux=sueldos[x]   # La variable aux es la que se va a encargar de llevar el número mayor al final de la lista
        sueldos[x]= sueldos[x+1] # El programa funciona evaluando aux entre cada uno de los datos de sueldo y cambiandose de posición si se cumple la condición de mayor
        sueldos[x+1] = aux
print("Lista con el elemento mayor ordenado al final")
print(sueldos) """

# Intercambiar 2 elementos de una lista de datos de nombres, la posición 5 con la 8

""" nombre= ["Juan", "Pablo", "Cano", "Saldarriaga", "Jose", "Sebastian", "Jordan", "Pedro", "Ivan", "Ana"]
print("La longitud de la lista es: ",len(nombre))
print("Antes del intercambio: ", nombre)
aux= nombre[4]
nombre[4]= nombre[7]
nombre[7]= aux

print("Después del intercambio: ", nombre)
"""

""" alumnos=[]
notas=[]
for x in range(5):
    nom=input("Ingrese el nombre del alumno: ")
    alumnos.append(nom)
    no=int(input("Ingrese la nota de dicho alumno: "))
    notas.append(no)

# Este bloque funciona como una lista de ordenamiento mediante la utilización de listas paralelas
for k in range(4):
    for x in range(4-k):
        if notas[x] < notas[x+1]:
            aux1=notas[x]
            notas[x]= notas[x+1]
            notas[x+1]= aux1
            aux2=alumnos[x]
            alumnos[x]= alumnos[x+1]
            alumnos[x+1]= aux2

print("Lista de alumnos y sus notas ordenadas de mayor a menor")
for x in range(5):
    print(f"Alumno: {alumnos[x]}, Nota: {notas[x]}") """


# Crear una lista por asignación, con cuatro elementos. Cada elemento debe de ser una lista de 3 enteros

""" lista=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
# Se imprime la lista completa
print(lista)
print("---------")
# Se imprime el primer componente de la lista
print(lista[0])
print("---------")
# Se imprime el primer comoponente contenido en la lista principal
print(lista[0][0])
print("---------")
# Se imprime los datos contenidos en la primera lista
for x in range(len/lista[0]):
    print(lista[0][x])
print("---------")
# Se imprimen los datos de todas las listas
for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][k]) """

# Para eliminar elementos de una lista se utiliza el método .pop(posición del elemento a eliminar)

# Crear una lista de 10 elementos y eliminar el primero

""" lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

lista.pop(0)
print("El primer número borrado: ", lista)
print("**************")
lista.pop(1)
print("El segundo elemento borrado de la lista:", lista) """

# Del es una función que elimina el índice seleccionado

""" lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

del lista[0]
print("El primer número borrado: ", lista)
print("**************")
del lista[3] # Se toma el valor de la nueva lista con el primer elemento eliminado
print("El segundo elemento borrado de la lista:", lista)
"""

# Mediante un método .insert se pueden agregar valores a una lista, de acuerdo a la posición que en la que se quiera agregar

# Agregar un elemento en una posición determinda

""" nombre= ["Juan", "Pedro", "Luis", "Hector", "Esteban"]
print(nombre)
nombre.insert(0, "Nuevo nombre") # El valor del inicio es la posición a la cual se va a añadir el dato
print("***************")
print(nombre) """

# El método count cuenta las veces que se repite un mismo dato

# Contar cantidad de apariciones elementos
""" nombre = ["Juan","Ivan","Pedro","Luis","Hector","Esteba","Juan","Marcos","Juan"]
x= nombre.count("Juan") 
print(x)
y= nombre.count("Ivan")
print(y) """


# Métodos de las listas

# El método extend toma una lista como argumento y le agrega sus valores a otra lista
""" t1 = [1,2,3]
t2 = [4,5] 
t1.extend(t2) 
print(t1) """

# El método .index obtiene el número de índice de una lista, o sea, la posición en la que se encuentra un elemento dentro de ella, este método busca en todo la lista desde una posición específica

# Obtener número de índice
""" nombre = ["Juan","Ivan","Pedro","Luis","Hector","Esteba","Juan","Marcos","Juan"]
x= nombre.index("Luis")
print(x)
print("******************")
y = nombre.index("Juan")
print(y)
"""
# El método .reverse ordena una lista al réves

""" nombre = ["Juan","Ivan","Pedro","Luis","Hector","Esteba","Juan","Marcos","Juan"]
print(nombre)
nombre.reverse()
print(nombre) """

# sort ordena los elementos de la lista de menor a mayor:
""" t = [4,7,5,8,1,22,78]
print(t)
t.sort()
t1 = ["d","a","f","b","k","c"]
print(t1)
t1.sort()
print(t)
print("---------------")
print(t1)
"""

# La instrucción set devuelve una colección desordenada de elementos diferentes de una lista

""" a= [2, 4, 4, 4, 4, 4, 9, 9, 3, 3, 5, 5, 6, 6, 8, 8, 10, 10, 13, 13] # Lista con elementos repetidos
b = set(a) # Instrucción set para crear una colección de elementos no repetidos
b=list(b)
print(a)
print(b)
"""

# Rebanado de listas 
""" t = ["a","b","c","d","e","f"] 
print(t[1:3]) 
print(t[:]) # Un operador de rebanado al lado izquierdo de una asignación puede actualizar múltiples elementos:
t[1:3] = ["x","y"]
print(t) """

""" t = ["a","b","c","d","e","f"]
print(t) 
print("Aplicando t[1:4]: ",t[1:4])
print("Aplicando t[2:100] (no genera error): ",t[2:100]) 
print("Imprime la lista completa", t[:]) # Un operador de rebanado al lado izquierdo de una asignación puede actualizar múltiples elementos: 
print("lista completa antes de la asignacion", t)
t[1:3] = ["x","y"] 
print("Lista modificada",t) 
t[5:7] = ["x","y","x","k","m","r"]
print("Lista modificada t[5:7]",t) """

# Forma para cambiar de posición los elementos de una lista

""" miLista = [10, 1, 8, 3, 5]

miLista [0], miLista [4] = miLista [4], miLista [0]
miLista [1], miLista [3] = miLista [3], miLista [1]

print(miLista)  """

# Forma para intercambiar de posición elementos de una lista de gran cantidad utilizando un ciclo for

""" miLista = [10, 1, 8, 3, 5, 7 ,8 ,9 ,6 ,5 ,4 ,2, 4 ,4, 23, 67, 43, 56, 87, 22, 12, 11, 13, 15, 52, 64]
print(miLista)
longitud = len(miLista)
print(f"La longitud de la lista es: {longitud}")

for i in range (longitud // 2): # Se utiliza este cuerpo para que funcione con las listas pares e impares
    miLista[i], miLista[longitud-i-1] = miLista[longitud-i-1], miLista[i] # -1 equivale a la última posición de la lista

print(f"La lista intercambiada es: {miLista}")  """

# Ordeamiento burbuja de una lista 

""" miLista = [8, 10, 6, 2, 4] # lista para ordenar
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while

while swapped:
    swapped = False # no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped= True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print(miLista) """

# Ordenamiento en burbuja con ingreso por teclado 

""" miLista = []
swapped = True
num = int (input("¿Cuántos elementos deseas ordenar?:"))

for i in range(num):
    val = float(input("Introduce un elemento de la lista:"))
    miLista.append(val)

while swapped:
    swapped = False
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped = True
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print("\nOrdenado:")
print(miLista) """

# Eliminar elementos duplicados de una lista

""" data = [1,3,2,4,7,3,2,2,1,4]
elements=[]
print(data)

for i in data:
    if i not in elements:
        elements.append(i)
print(f"Lista sin elementos repetidos: {elements}") """


# Hallar los números pares ingresados por teclado

""" def pares():
    lista=[]
    for i in range(5):
        x=int(input(f"Ingrese el número {i+1}: "))
        lista.append(x)
    print(lista)
    for par in lista:
        if par % 2==0:
            print(par)

pares() """

