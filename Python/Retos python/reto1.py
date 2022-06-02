import sys
import random
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

# Primera parte del Login, usuario y contraseña con el código del curso 51612
nombre_usuario=51612
contraseña=21615
login_list=[nombre_usuario,contraseña]
usuario=int(input("Ingrese el usuario: "))
if usuario != login_list[0]:
    print("ERROR")
    sys.exit()
else:
    password=int(input("Ingrese la contraseña: "))
    if password != login_list[1]:
        print("ERROR")
        sys.exit()
        
"""Segunda parte del Login, hay que generar un captcha con números y operaciones aritmeticas, cuyo resultado me permita
ingresar al sistema o me notifique un error"""

numero1=612
lista_operaciones=[(6-5)//1, 6*1-5, (6//1)-5]  # Lista con las operaciones para hallar el número 2 del captcha

# Se utiliza random.choice para escoger un valor al azar de la variable seleccionada
captcha=int(input("¿Cuál es el resultado de la siguiente operación?\n"+ str(numero1)+ "+"+ str(random.choice(lista_operaciones))+"= "))
resultado_captcha=613
if captcha == resultado_captcha:
    print("Sesión iniciada")
    sys.exit()
else:
    print("ERROR")

# Segunda parte del reto, continuar con el login y desplegar el menú de opciones
