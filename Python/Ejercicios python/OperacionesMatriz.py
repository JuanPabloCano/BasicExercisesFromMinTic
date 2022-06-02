# Escribe un programa que lea dos matrices de la misma longitud y permita realizar las siguientes operaciones: Suma, Resta y Multiplicación por escalar. Reusa el código del punto anterior para leer las matrices e imprimir el resultado

import numpy as np

a= [2,0,5,8]
b= [1,3,7,4]

x= np.array(a)
z= np.array(b)

print(x)
print(z)

s= np.add(x,z)
r= np.subtract(x,z)
m= np.multiply(x,z)

print(f"La suma de los elementos de ambas matrices es: \n{s}")
print(f"La resta de los elementos de ambas matrices es: \n{r}")
print(f"La multiplicación de los elementos de ambas matrices es: \n{m}")