import os

# Método open() para abrir un archivo
# "r" : solo lectura
# "r+" : lectura y escritura
# "w" : sobreescribir
# "a" : Permite escribire, conservar los datos
# "a+" : Permite escribire y leer, conservar los datos
# encoding="utf8" (caracteres especiales del español)

archivo=open(r"C:\Users\Usuario\Desktop\JP\Fundamentos de programación 1 Python\Archivos\Ejemplo.txt") # Se utiliza la letra r para que no haya un error

print("*************************")
print()
print("metodo.read()")
print()
print(archivo.read()) # El método read sirve para leer un archivo en su totalidad, si es muy extenso se leería una parte

