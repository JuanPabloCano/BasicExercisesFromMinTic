# Realice un programa que arroje el numero mayor, el menor y el medio

""" Esta sería una forma de hacerlo con condicionales If, Elif y Else; el código se hace muy largo, hay que mejorar """

mayor,medio,menor=0,0,0
num1= int(input("Ingrese primer numero: "))
num2= int(input("Ingrese segundo numero: "))
num3= int(input("Ingrese tercer numero: "))
if num1>num2 and num1>num3:
    mayor=num1
elif num2>num1 and num2>num3:
    mayor=num2
else:
    mayor=num3
if num1<num2 and num1<num3:
    menor=num1
elif num2<num1 and num2<num3:
    menor=num2
else:
    menor=num3
if num1>num2 and num1<num3:
    medio=num1
elif num1<num2 and num2<num3:
    medio=num2
elif num1<num3 and num2>num3:
    medio=num3
print("Numero mayor: ", str(mayor))
print("Numero menor: ", str(menor)) 
print("Numero medio: ", str(medio))

""" Otra forma de hacerlo sería con el for in range; append anexa valores a la lista seleccionada; {}.format
agrega valores seguidos del .format directamente a los corchetes; import statistics.median me arroja la mediana de
la lista seleccionada."""

import statistics
num=int(input("Cuantos numeros quiere introducir? "))
listaN= []
for i in range(num):
    valor= int(input("Escriba un numero",))
    listaN.append(valor)
print("El numero mayor es: {}".format(max(listaN)))
print("El numero menor es: {}".format(min(listaN)))
print("El numero de la mitad es:", statistics.median(listaN)) # Función para hallar la mediana

