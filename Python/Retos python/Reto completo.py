import sys,os,random,time,math

""" Definición de variables y estructura de datos """

opciones_menu = ["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo","Elegir opción de menú favorita","Cerrar sesión"]
nombre_usuario=51612
contraseña=21615
login_list=(nombre_usuario,contraseña) # Lista que almacena las dos variables necesarias para el ingreso al sistema
coordinate_list=[[], [], []] # Lista vacía para las coordenadas de los 3 sitios que más se frecuentan
flag = 0 # Variable para el control del ingreso de datos de las coordenadas
#  orden de los datos lat, log y usuarios promedios
wifi_zones= [[6.124,-75.946,1035],[6.125,-75.966,109],[6.135,-75.976,31],[6.144,-75.836,151]]
cl_wifizones= [[],[],[],[]] # Closest wifi zones
dic_info= {}
new_coordinate_op= None

""" Bloques de funciones """

def update_wifi_records_from_file(dic_info):
    print("Diccionario Informacion")
    print("Actualizar registros de zonas wifi desde archivo")
    print()
    print(dic_info)
    print()
    print("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal")
    zero= int(input())
    if zero == 0:
        return
    else:
        exit()

def save_file_with_nearby_loc(flag, dic_info, new_coordinate_op):
    os.system("cls")
    print("Guardar archivo con ubicación cercana")
    if flag == 0:
        print("Error de alistamiento")
        exit()
    else:
        if new_coordinate_op not in (1,2,3):
            print("Error de alistamiento")
            exit()
        else:
            print("Diccionario de información")
            print()
            print(dic_info)
            print()
            print("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal")
            c= int(input())
            if c == 0:
                return
            else:
                if c == 1:
                    print("Exportando archivo")
                    exit()

def coordinate_output(coordinate_list):
    os.system('cls') 
    for x in range(3):
        print(f"Coordenada [latitud,longitud] {x+1} : {coordinate_list[x]}") 

def wifi_distance(location_op, coordinate_list, wifi_zones, cl_wifizones):
    r=6371  # km (Radio de la Tierra)
    Latitude2 = coordinate_list[location_op-1][0]
    lenght2 = coordinate_list[location_op-1][1]

    for i in range(4):
        latitude1= wifi_zones[i][0]
        lenght1= wifi_zones[i][1]
        # calculo los deltas
        del_lat = math.radians((Latitude2 - latitude1))
        del_lon = math.radians((lenght2 - lenght1))
        x = math.sin(del_lat/2) * math.sin(del_lat/2) + math.cos(math.radians(latitude1)) * math.cos(math.radians(Latitude2)) * math.sin(del_lon/2) * math.sin(del_lon/2)
        z = 2 * math.atan2(math.sqrt(x), math.sqrt(1-x))
        # calculo la distancia
        distance = (r * z)*1000  # se pasa a metros, 1 km = 1000 mts
        cl_wifizones[i]=[latitude1,lenght1,round(distance),wifi_zones[i][2],i]

def distance_ordering(cl_wifizones, wifi_zones):
    for x in range(4):
        for j in range(4):
            if cl_wifizones[x][2] < cl_wifizones[j][2]:
                cl_wifizones[x], cl_wifizones[j]= cl_wifizones[j], cl_wifizones[x]
    print()
    print("Zonas wifi cercanas con menos usuarios")
    for i in range(2):
        print(f"La zona wifi {i+1}: ubicada en [{cl_wifizones[x][0]},{cl_wifizones[x][1]}] a {cl_wifizones[x][2]} metros, tiene en promedio {cl_wifizones[x][3]}")

def closest_wifiZone_location(flag, coordinate_list, wifi_zones, cl_wifizones, dic_info):
    if flag == 0:
        print("Error sin registro de coordenadas")
        exit()
    else:
        os.system('cls')
        coordinate_output(coordinate_list)  
        print("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión")
        new_coordinate_op= int(input())
        if new_coordinate_op not in (1,2,3):
            print("Error ubicación")
            exit()
        else:
            os.system('cls')    
            print(f"coordenada [latitud,longitug] {new_coordinate_op} : {coordinate_list[new_coordinate_op-1]}") 
            wifi_distance(new_coordinate_op,coordinate_list,wifi_zones,cl_wifizones)
            distance_ordering(cl_wifizones,wifi_zones)  
            print("Elija 1 o 2 para recibir indicaciones de llegada")
            arrive_op = int(input()) # opcion de llegada
            if arrive_op not in (1,2):
                print("Error zona wifi")
                exit()
            else:
                
                print()
                bus = 16.67
                auto = 20.83 
                print("Para llegar a la zona wifi dirigirse primero al sur y luego hacia el oriente")
                bus_time = (cl_wifizones[arrive_op-1][2])/ bus
                car_time = (cl_wifizones[arrive_op-1][2])/ auto
                print(f"Tiempo promedio en bus: {round(bus_time)} m/s")
                print(f"Tiempo promedio en auto: {round(car_time)} m/s")
                # Se llama al diccionario vacío para que se ingresen los datos solicitados mediante el llamado de la variable que seleccionó la coordenada
                dic_info = {"actual":coordinate_list[new_coordinate_op-1],
                            "zonawifi1":[cl_wifizones[arrive_op-1][0],cl_wifizones[arrive_op-1][1],cl_wifizones[arrive_op-1][3]],
                            "recorrido":[cl_wifizones[arrive_op-1][2],"bus",bus_time]}
            return_menu = int(input("Presione 0 para salir: "))
            if (return_menu == 0):
                return dic_info, new_coordinate_op
            else:
                exit()

def coordinate(coordinate_list): # Función para determinar si la coordenada está más hacia el sur, este u oeste, además halla el promedio de las latitudes y longitudes

    lat= [coordinate_list[0][0],coordinate_list[1][0], coordinate_list[2][0]]
    le=[coordinate_list[0][1], coordinate_list[1][1], coordinate_list[2][1]]
    average_lat,average_le =  sum(lat)/3, sum(le)/3
    north, south = lat.index(max(lat)), lat.index(min(lat))
    oriente, occidente = le.index(max(le)), le.index(min(le))
    return average_lat, average_le, north, south, oriente, occidente

# Función para cambiar la contraseña

def password_change(login_list):
    os.system("cls")
    confirm_password=int(input("Confirme la contraseña actual: "))
    if confirm_password == login_list[1]:
        new_password=int(input("Ingrese la nueva contraseña: "))
        if new_password == login_list[1]:
            print("La nueva contraseña no puede ser igual a la contraseña actual")
            time.sleep(1)
        else:
            login_list[1]=new_password
            time.sleep(1)
    else:
        print("Error")
        exit()

# Función para desplegar las opciones del menú

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

# Función para el ingreso y actualización de las coordenadas

def current_coordinate_input(coordinate_list, flag):

    if flag == 0:
        print("Ingresar las coordenadas de los tres sitios que más frecuenta (trabajo, casa, parque)")
        for i in range(3):
            latitude=float(input(f"Ingrese la latitud {i+1}: "))
            if latitude != 0 or latitude !="":
                if (latitude < 6.077 or latitude > 6.284):
                    print("Error coordenada")
                    exit()
                else:
                    lenght=float(input(f"Ingrese la longitud {i+1}: "))
                    if lenght !=0 or lenght != "":
                        if lenght < (-76.049) or lenght > (-75.841):
                            print("Error coordenada")
                            exit()
                        else:
                            coordinate_list[i]=[latitude, lenght]
                            time.sleep(1)
                    else:
                        print("Error")        
                        exit()
            else:
                print("Error")
                exit()
    else:
        coordinate_output(coordinate_list)
        average_lat, average_le, north, south, oriente, occidente=coordinate(coordinate_list)
        print(f"La coordenada {north+1} es la que esta mas al norte")
        print(f"La coordenada {oriente+1} es la que está más al oriente")
        print("Presione 1,2 o 3 para actualizar la respectiva coordenada")
        print("presione 0 para regresar al menu")
        new_coordinate_op= int(input())
        
        if new_coordinate_op not in (1,2,3):
            print("Error actualización")
            exit()
        else:
            if new_coordinate_op== 0:
                return
            else:
                latitud=float(input(f"Ingrese la latitud {new_coordinate_op}: "))
                if (latitud !=0) or (latitud!=""):
                    if (latitud < 6.077 or latitud > 6.284):
                        print("Error coordenada")
                        exit()
                    else:
                        longitud=float(input(f"Ingrese la longitud {new_coordinate_op}: "))
                        if (latitud !=0) or (latitud!=""):
                            if (longitud < -76.049 or longitud > -75.841):
                                print("Error coordenada")
                                exit()
                            else:
                                coordinate_list[new_coordinate_op-1]= [latitud,longitud]
                                time.sleep(2)
                        else:
                            print("Error")
                            exit()
                else:
                    print("Error")
                    exit()
    flag = 1
    return flag

# Función para desarrollar la opción favorita

def opcion_favorita(opciones_menu):  # Función para seleccionar la opción favorita
    sel_favorita = int(input("Seleccione opción favorita: "))

    if (sel_favorita >= 1 and sel_favorita <=5):
        adv = int(input("Para confirmar por favor responda: De muchos hijos que somos, el primero yo nací, pero soy el menor de todos. ¿Cómo puede ser así?: "))
        if (adv == 1):
            adv2 = int(input("Para confirmar por favor responda: Cuenta las manos o cuenta los pies y sabrás que número es: ")) # Variable para identificar las adivinanzas
            if (adv2 == 2):
                os.system("cls")      
                opciones_menu[0], opciones_menu[(sel_favorita-1)]= opciones_menu[(sel_favorita-1)], opciones_menu[0] # Forma para reordenar la opción favorita del menú                
            else:
                print("Error")
        else:
            print("Error")
    else:
        print("Error")
        exit()


def reto_2(login_list, coordinate_list, flag, dic_info,new_coordinate_op):
    contador_intentos = 0 # Variable contador para controlar el número de intentos fallidos
    seleccion_menu = 1 # Comienza en 1 para entrar por primera vez al bucle
    ref= "" # Variable vacía para que no genere error al modificar la posición de las opciones del menú

    # ciclo repetitivo para controlar el menu
    while (seleccion_menu != 7 and contador_intentos !=3): 
        seleccion_menu = opciones(opciones_menu)
        if (seleccion_menu > 7) or (seleccion_menu <= 0): # controlo que las opciones del menu esten entre 1 y 7
            contador_intentos +=1
            print("Error")
        else:
            ref=opciones_menu[seleccion_menu-1]

        if ref == "Cambiar contraseña":
            login_list= password_change(login_list)

        if ref == "Ingresar coordenadas actuales":
            flag= current_coordinate_input(coordinate_list,flag)

        if ref == "Ubicar zona wifi más cercana":
            dic_info, new_coordinate_op= closest_wifiZone_location(flag, coordinate_list, wifi_zones, cl_wifizones, dic_info)
        
        if ref == "Guardar archivo con ubicación cercana":
            save_file_with_nearby_loc(flag, dic_info, new_coordinate_op)      

        if ref == "Actualizar registros de zonas wifi desde archivo":
            update_wifi_records_from_file(dic_info)

        if seleccion_menu == 6: 
            seleccion_menu = opcion_favorita(opciones_menu) 
            os.system('cls')

        if (seleccion_menu == 7):
            print("Hasta pronto")
            exit() 

# Desarrollo del cuerpo del login del programa, parte principal

def reto_1(login_list, coordinate_list, flag, dic_info, new_coordinate_op):
    os.system("cls")
    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
    # Primera parte del Login, usuario y contraseña con el código del curso 51612
    usuario=int(input("Ingrese el usuario: "))
    if usuario != login_list[0]:
        print("ERROR")
        sys.exit()
    else:
        password=int(input("Ingrese la contraseña: "))
        if password != login_list[1]:
            print("ERROR")
            sys.exit()

    """Segunda parte del Login, hay que generar un captcha con números y operaciones aritmeticas, cuyo resultado me permita ingresar al sistema o me notifique un error"""
    
    numero1=612
    lista_operaciones=[(6-5)//1, 6*1-5, (6//1)-5]  # Lista con las operaciones para hallar el número 2 del captcha
    # Se utiliza random.choice para escoger un valor al azar de la variable seleccionada
    captcha=int(input("¿Cuál es el resultado de la siguiente operación?\n"+ str(numero1)+ "+"+ str(random.choice(lista_operaciones))+"= "))
    resultado_captcha=613
    if captcha == resultado_captcha:

        print("Sesión iniciada")
        reto_2(login_list, coordinate_list, flag, dic_info, new_coordinate_op)

    else:
        print("Error")
        exit()


reto_1(login_list, coordinate_list, flag, dic_info, new_coordinate_op)