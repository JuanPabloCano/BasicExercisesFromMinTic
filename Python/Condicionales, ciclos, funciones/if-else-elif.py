""=="" #igual que
"!=" #distinto que
"">"" #mayor que
"<" #menor que
"">="" #mayor o igual que
"<=" #menor o igual que


# Ingresar el sueldo de una persona,si este supera 3000 dolares imprimir en pantalla que debe abonar impuestos

sueldo=int(input("Ingrese cual es el sueldo \n"))
if sueldo>3000:
    print("Debe pagar impuestos")
else:
    print("No debe pagar impuestos")

"""Calcular el valor promedio de un mercado, si el valor supera los 500 mil pesos, decir que está muy caro, si está entre
250 mil y 500 mil, está en un valor exacto, si vale menos de 250 mil, está muy barato  """

valorcompra1= float(input("Ingrese el primer valor:"))
valorcompra2= float(input("Ingrese el segundo valor:"))
valorcompra3= float(input("Ingrese el tercer valor:"))
valorcompra4= float(input("Ingrese el cuarto valor"))
valorcompra5= float(input("Ingrese el quinto valor:"))
valortotal= (valorcompra1 + valorcompra2 + valorcompra3 + valorcompra4 + valorcompra5)/ 5
if valortotal> 500000:
    print("Costoso")
elif valortotal>= 250000:
        print("Asequible")
else:
    if valortotal<= 250000:
        print("Barato")


# Elif significa sino, si. Si las condiciones anteriores no son verdaderas, entonces intenta esta.

""" Selecciona en un exámen que la respuesta correcta sea la B """

respuesta1= ("a") 
respuesta2= ("b") 
respuesta3= ("c") 
respuesta4= ("d")
respuestacorrecta= input("Respuesta")
if respuestacorrecta== "a":
    print("Incorrecto")
elif respuestacorrecta== "d":
    print("Incorrecto")
elif respuestacorrecta== "c":
    print("Incorrecto")
else:
    respuestacorrecta== "b"
    print("Correcto")

# Desarrolla un programa que funcione como una alcancía, que pregunte si quiere continuar ahorrando






























