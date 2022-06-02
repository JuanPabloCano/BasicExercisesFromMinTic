import os

# Primera parte del programa, organizar las opciones del menú mediante un parámetro

def opciones(opciones_menu):
    os.system("cls")
    print("")
    print("",str("1."),opciones_menu[0],"\n", 
    str("2."),opciones_menu[1],"\n",
    str("3."),opciones_menu[2],"\n",
    str("4."),opciones_menu[3],"\n",
    str("5."),opciones_menu[4],"\n",
    str("6."),opciones_menu[5],"\n",
    str("7."),opciones_menu[6],"\n")
    seleccion_menu = int(input("Elija una opción: "))
    return seleccion_menu

# Función para desarrollar la opción favorita

def opcion_favorita(opciones_menu):  # Función para seleccionar la opción favorita
    sel_favorita = int(input("Seleccione opción favorita: "))

    if (sel_favorita >= 1 and sel_favorita <=5):
        adv = int(input("Para confirmar por favor responda: De muchos hijos que somos, el primero yo nací, pero soy el menor de todos. ¿Cómo puede ser así?: "))
        if (adv == 1):
            adv2 = int(input("Para confirmar por favor responda: Cuenta las manos o cuenta los pies y sabrás que número es: ")) # Variable para identificar las adivinanzas
            if (adv2 == 2):
                os.system("cls")      
                # aux = opciones_menu[0]
                opciones_menu[0], opciones_menu[(sel_favorita-1)]= opciones_menu[(sel_favorita-1)], opciones_menu[0]
                # opciones_menu[(sel_favorita-1)]= aux
            else:
                print("Error")
        else:
            print("Error")
    else:
        print("Error")
        exit()

# Desarrollo del cuerpo del programa con el bucle y los condicionales 

def reto_2():
    opciones_menu = ["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo","Elegir opción de menú favorita","Cerrar sesión"]
    contador_intentos = 0 # Variable contador para controlar el número de intentos fallidos
    seleccion_menu = 1 # Comienza en 1 para entrar por primera vez al bucle
    
    # ciclo repetitivo para controlar el menu
    while (seleccion_menu != 7 and contador_intentos !=3): 
        seleccion_menu = opciones(opciones_menu)
        if (seleccion_menu > 7) or (seleccion_menu <= 0): # controlo que las opciones del menu esten entre 1 y 7
            contador_intentos +=1
            print("Error")
            
        if seleccion_menu == 1:
            print(f"Usted ha elegido la opción {seleccion_menu}") 
            exit()
        
        if seleccion_menu == 2:
            print(f"Usted ha elegido la opción {seleccion_menu}") 
            exit()

        if seleccion_menu == 3:
            print(f"Usted ha elegido la opción {seleccion_menu}") 
            exit()

        if seleccion_menu == 4:
            print(f"Usted ha elegido la opción {seleccion_menu}") 
            exit()
        
        if seleccion_menu == 5:
            print(f"Usted ha elegido la opción {seleccion_menu}") 
            exit()

        if seleccion_menu == 6: 
            seleccion_menu = opcion_favorita(opciones_menu) 
            os.system('cls')

        if (seleccion_menu == 7):
            print("Hasta pronto")
            exit() 

reto_2()