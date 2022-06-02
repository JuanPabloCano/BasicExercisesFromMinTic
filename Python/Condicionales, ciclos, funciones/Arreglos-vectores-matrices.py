# Una matriz es una estructura de datos que almacena valores del mismo tipo de datos
# Los arreglos(vecotres) son listas de una o más dimensiones donde sus elementos son del mismo tipo( usualmente númerico)
# NumPy: Numerical python. Permite trabajar con vectores y matrices (Matemáticas, machine learning, etc.)
# NumPy ocupa menos memoria de las listas, es más rápido en términos de ejecución
# Sintaxis= np.array: Indica que son datos con estructura tipo arreglo

import numpy as np

""" a=np.array([2,3,4]) # Array unidimensional

b=np.array([[2,5,1],[6,5,3],[9,8,2]]) # Array multidimensional

print("1D Array")
print(a)
print()
print("2D Array")
print(b) """

# Crea una matriz vacía
""" vacia=np.empty((3,2))
print(vacia)
"""

# Método unos, ceros, aleatoria

# Crear un a matriz de unos - 3 filas y 4 columnas

""" print("Crear un a matriz de unos - 3 filas y 4 columnas") 
unos = np.ones((3,4)) 
print(unos)
print()
# Crear un a matriz de ceros - 4 filas y 4 columnas
print("Crear un a matriz de ceros - 4 filas y 4 columnas")
ceros = np.zeros((4,4))
print(ceros)
print()
# Crear un a matriz de aleatoria - 3 filas y 4 columnas
print("Crear un a matriz de aleatoria - 2 filas y 3 columnas")
aleatoria = np.random.random((2,3))
print(aleatoria) """

# Método full: Llena la matriz con el número que se requiera

""" full= np.full((2,2),8)
print(full)
"""
# Método shape: Indica cuantas filas y cuantas columnas

""" a=np.array([2,3,4]) # Arrays Unidimensionales: Vectores 
b=np.array([[2,5,1],[6,5,3],[9,8,2],[9,8,2]]) # Arrays Multidimensionales o Matrices # Nos indica cuantas filas y columnas tiene el array 
print("filas y columnas array a")
print(a.shape)
print(a)
print()
print("filas y columnas array b")
print(b.shape)
print(b)
"""
# El método size: Indica cuantos elementos hay en el arreglo
# se nombre nd por convencion  
""" a=np.array([2,3,4]) #Arrays Unidimensionales: Vectores
b=np.array([[2,5,1],[6,5,3],[9,8,2]]) #Arrays Multidimensionales o Matrices
print("1D Array")
print(a)
print()
print("2D Array")
print(b)
print("Numero de elementos en a", a.size)
print("Numero de elementos en b", b.size)
"""
# El método dot: sirve para multiplicar matrices

# se nombre nd por convencion
""" a = np.array([[-2,-6],[-4,-3],[5,0],[4,-6]])
b = np.array([[2,-2,2],[-2,0,-3]])
print("Matriz A")
print(a)
print()
print("Matriz B")
print(b)
print()
print("La multiplicacion es A * B:")
print(a.dot(b))
"""
# Se puede acceder a los elementos de una matriz mediante un índice []

# Matriz unidimensional

""" a=np.array([2,4,6,8,10])
print("a[0-*", a[0]) # Primer elemento
print("a[0-*", a[2]) # Tercer elemento
print("a[0-*", a[-1]) # Primer elemento a la inversa
"""

# Matriz multidimensional

""" a= np.array([[1,4,5,12],
    [-5,8,9,0],
    [-6,7,11,19]])
print(a)
print("A[0][0]-", a[0][0]) # Primer elemento de la primera fila
print("A[1][2]-", a[1][2]) # Tercer elemento de la segunda fila
print("A[-1][-1]-", a[-1][-1]) # ültimo elemento de la última fila """

# Accediendo a las columnas de una matriz

""" a= np.array([[1,4,5,12],
    [-5,8,9,0],
    [-6,7,11,19]])
print("A[:,0]=", a[:,0]) # Primera columna
print("A[:,3]=", a[:,3]) # Cuarta columna
print("A[:,-1]=", a[:,-1]) # última columna """

# Porcionar una matriz unidimenisional

""" letters= np.array([1,3,5,7,9,7,5])
print(letters[2:5]) # Del tercero al quinto elemento
print(letters[:-5]) # Del primero al cuarto elemento
print(letters[5:]) # Del sexto al último elemento
print(letters[:]) # Del primero al último elemento
print(letters[::-1]) # Reverso de la lista
"""

# Convertir lista en arreglo

""" tempC= [10,12,15,23,25,35,26] # Lista de temperaturas
arreglo_temp= np.array(tempC) # Se pasan los datos de la lista al arreglo
print(f"La lista de temperaturas es: {tempC}")
print(f"Se muestran los datos guardados en el arreglo unidimensional: {arreglo_temp}") """

# Operaciones con array

""" r= [10,12,15,23,25,35,26,44,55,88,100,56,89]

oper= np.array(r)
print(f"Multiplicando cada dato x 10: {oper*10}")
print()

for i in range(0, len(oper)-1):  # El -1 se utiliza para que abarque todos los datos de la lista/arreglo desde el cero
    print(f"Valor antes de multiplicar: {oper[i+1]}, valor multiplicado x2: {oper[i+1]*2}")
"""    

