# Almacena colección de datos no del mismo tipo, son inmutables, no se pueden modificar.
# Su sintaxis es através de ()

# Métodos

# Index(elemento)
# Count (Elemento)

""" a= "Negro"
ejemplo= (1,a,"hola")
print(ejemplo) """

# Definir varias tuplas e imprimir sus elementos

""" tupla=(1, 2, 3)
fecha=(25, "Diciembre", 2016)
punto=(10, 2)
persona=("Rodriguez", "Pablo", 43, [2,4,5,6,], {"uno":1})
print(tupla)
print(fecha)
print(punto)
print(persona) """

# Se pueden crear tuplas sin parentesis, tuple packing

""" numeros= 1,2,3,4,5
elementos= 3, "a", 8, 7.2, "hola"
tup1= 1, ["a", "b", "c", "d"], 8.5, "hola"
print(numeros)
print(elementos)
print(tup1) """

# Desarrollar una función que solicite la carga del día, mes y año, y almacene dichos datos en una tupla que luego debe retornar. La segunda función a implementar debe recibir una tupla con la fecha yv mostrarla por pantalla

""" def cargar_fecha():
    dd=input("Ingrese el día: ")
    month=input("Ingrese el mes: ")
    year=input("Ingrese el año: ")
    return (dd,month,year)

def imprimir_fecha(fecha):
    print(fecha[0], fecha[1], fecha[2], sep="/")

fecha=cargar_fecha()
imprimir_fecha(fecha) """

""" # acceder a los elementos de una tupla
tupla = ('a', 'b', 'd') # Primer elemento de la tupla. Índice 0 print(tupla[0])
# Segundo elemento de la tupla. Índice 1 print(tupla[1])
print(tupla) 
print("********************************")
# Acceso a los elementos usando un índice negativo
print("Acceso a los elementos usando un índice negativo")
bebidas = ('agua', 'café', 'batido', 'sorbete')
print(bebidas)
print(bebidas[-1])
print(bebidas[-3])

# Acceso a un subconjunto de elementos
print("Acceso a un subconjunto de elementos")
vocales = 'a', 'e', 'i', 'o', 'u'
print(vocales)
print("Elementos desde el índice 2 hasta el índice 3-1")
print(vocales[2:3])
# Elementos desde el índice 2 hasta el índice 3-1
print("Elementos desde el 2 hasta el índice 4-1")
vocales[2:4] # Elementos desde el 2 hasta el índice 4-1
print("Todos los elementos")
vocales[:] # Todos los elementos
print("Elementos desde el índice 1")
vocales[1:] # Elementos desde el índice 1 print("Elementos hasta el índice 3-1")
vocales[:3] # Elementos hasta el índice 3-1  """

# Recorrer tupla usando un for

""" tupla=(2, 3, 4, "Hola", 8)
for i in tupla:
    print(i) """

# Definir una tupla con tres valores enteros. Convertir el contenido de la tupla a tipo lista. Modificar la lista y luego convertir la lista en tupla.

""" fechatupla1=(25, 12, 2016)
print("Imprimimos la primer tupla")
print(fechatupla1)
fechalista=list(fechatupla1)  # Funcióm para crear una lista
print("Imprimimos la lista que se le copio la tupla anterior")
print(fechalista) 
fechalista[0]=31  # Valor que modifica la lista en la posición 0
print("Imprimimos la lista ya modificada") 
print(fechalista)
fechatupla2=tuple(fechalista)  # Función para crear una tupla
print("Imprimimos la segunda tupla que se le copio la lista")
print(fechatupla2) """


# Escribir un programa que almacene en una tupla los siguientes precios: 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios

""" tup= (50, 75, 46, 22, 80, 65, 8)
mayor=max(tup)
menor=min(tup)
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}") """

""" tup= (50, 75, 46, 22, 80, 65, 8)
mayor= tup[0] # Posición en la tupla que se compara con todas las demas en el ciclo for
menor= tup[0]

for i in tup:
    if i < menor:
        menor= i
    elif i > mayor:
        mayor= i
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}") 
"""