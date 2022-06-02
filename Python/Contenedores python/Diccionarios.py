# La estructura de datos tipo diccionario utiliza una clave para acceder a un valor. Puede ser un entero, float, string, tupla, etc.
# El diccionario es mutable, se pueden agregar elementos, modificarlos y borrarlos.
# El diccionario define una relación uno a uno entre {claves y valores}

# Métodos

# Dict- Sirve para crear diccionarios
# Get- sirve para extraer el valor correspondiente al valor
# Keys- obtiene las claves
# Setdefault - devuelve el valor de la clave si ya existe, en caso contrario le asigna el valor que se pasa como segundo argumento. Si no se especifica el segundo argumento, per defecto sería None
# Copy()- copia un diccionario
# Update(diccionario)- concatena diccionarios
# Has_keys(clave)- muestra si una clave existe en un diccionario
# Iteritems() o items()- devuelve la clave y el valor de un diccionario
# Values- obtiene los valores de un diccionario
# D- modifica los elementos de un diccionario
# Pop- elimina un elemento
# Popitem- Elimina el último elemento del diccionario
# Clear- elimina un diccionario

# Ejemplo

""" productos= {"manzanas":39,"peras":32,"lechuga":17}
print(productos) """

""" diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }
for i in diccionario:
    print(i, ":", diccionario[i])
 """
# Crear un diccionario que permita almacenar 5 articulos, utilizar como clave el nombre del producto y como valor el precio del mismo
# 1- Imprimir en forma completa el diccionario
# 2- Imprimir solo los artículos con precio superior a 100

""" def cargar(): 
    productos={} 
    for x in range(5): 
        nombre=input("Ingrese el nombre del producto: ")
        precio=int(input("Ingrese el precio: "))
        productos[nombre]=precio # diccionario[clave] = valor 
    return productos 

def imprimir(productos): 
    print("Listado de todos los articulos") 
    for nombre in productos:
        print(f"El producto {nombre} tiene un precio de: {productos[nombre]} pesos") 

def imprimir_mayor100(productos): 
    print("Listado de articulos con precios mayores a 1000") 
    for nombre in productos: 
        if productos[nombre]>1000: print(nombre)

# bloque principal 

productos=cargar()
imprimir(productos)
imprimir_mayor100(productos) """

# En el bloque principal del programa definir un diccionario que almacene los nombres de paises como clave y como valor la cantidad de habitantes. Implementar una función para mostrar cada clave y valor.

# 1- Diccionario con nombres de paises como clave y valor cantidad de habitantes
# 2- Implmentar una función para mostrar clave y valor
# 3- Indicar el país con mayor población

""" import operator

def cargar_paises():
    paises={}
    for i in range(3):
        pais=input("Ingrese el nombre del país: ")
        habitantes= int(input("Ingrese la cantidad de habitantes: "))
        paises[pais]= habitantes

    return paises

def pais_mayor_poblacion(paises): 
    pais_mayor= max(paises.items(), key=operator.itemgetter(1))[0]  # Metódo para hallar el valor máximo de un diccionario
    print(f"El país con el mayor número de habitantes es: {pais_mayor}")

paises=cargar_paises()
pais_mayor_poblacion(paises) """

# Segunda forma para hallar el valor máximo de un diccionario

""" import operator

def cargar_paises():
    paises={}
    for i in range(3):
        pais=input("Ingrese el nombre del país: ")
        habitantes= int(input("Ingrese la cantidad de habitantes: "))
        paises[pais]= habitantes

    return paises

def pais_mayor_poblacion(paises): 
    pais_mayor= max(paises, key=paises.get)  # Metódo para hallar el valor máximo de un diccionario de otra forma
    print(f"El país con el mayor número de habitantes es: {pais_mayor}")

paises=cargar_paises()
pais_mayor_poblacion(paises)  """


# Desarrollar una aplicación que nos permita crear un diccionario inglés/castellano. La clave es es la palabra en inglés y el valor es la palabra en español. Crear las siguientes funciones:
# 1- Cargar el diccionario
# 2- Listado completo del diccionario
# 3- Ingresar por teclado una palabra en inglés y si existe en el diccionario mostrar su traducción

import os

# Función de entrada para las palabras en inglés y español

""" def cargar_diccionario():   
    diccionario={}
    continuar= "s"
    while continuar=="s":
        espa=input("Ingrese palabra en español: ")
        ing=input("Ingrese palabra en inglés: ")
        diccionario[ing]=espa
        continuar=input("Desea agregar otra palabra? s/n: ")
    else:
        if continuar=="n":
            bienvenida_principal()
    diccionario[ing]=espa
    return diccionario

# Función para enlistar el diccionario

def listado_completo_diccionario(diccionario):
    print("Listado completo de diccionario")
    for ingles in diccionario:
        print(ingles, diccionario[ingles])

# Función para consultar las palabras en el diccionario

def consulta_palabra(diccionario):
    palabra=input("Ingrese la palabra que desea buscar\n")
    if palabra in diccionario:
        print(diccionario.get(palabra, "La palabra ingresada significa: ", diccionario))

# Función para el menú principal

def bienvenida_principal():
    os.system("cls")
    diccionario={}
    print("Bienvenido a su diccionario Inglés/Español")
    print("Que desea hacer?")
    palabras=["Añadir palabra al diccionario", "Buscar palabra", "Ver el listado completo del diccionario"]
    print("",str("1."),palabras[0],"\n", 
    str("2."),palabras[1],"\n",
    str("3."),palabras[2],"\n")
    menu=int(input("Seleccione una opción: "))
    if menu==1:
        cargar_diccionario()
    elif menu==2:
        consulta_palabra(diccionario)
    elif menu==3:
        listado_completo_diccionario(diccionario)

bienvenida_principal()  """

