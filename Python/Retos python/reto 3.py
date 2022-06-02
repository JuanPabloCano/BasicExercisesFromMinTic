import os,time

nombre_usuario=51612
contraseña=21615
login_list=[nombre_usuario,contraseña]
coordinate_list=[[], [], []] # Lista vacía para las coordenadas de los 3 sitios que más se frecuentan

# Función para cambiar la contraseña
def password_change(login_list):
    os.system("cls")
    confirm_password=int(input("Confirme la contraseña actual: "))
    if confirm_password == login_list[1]:
        new_password=int(input("Ingrese la nueva contraseña: "))
        if new_password == login_list[1]:
            print("La nueva contraseña no puede ser igual a la contraseña actual")
            time.sleep(2)
        else:
            login_list[1]=new_password
            time.sleep(2)
    else:
        print("Error")
        exit()

# Función para el desarrollo del ingreso y actualización de las coordenadas en una matriz

def current_coordinate_input(coordinate_list):
    os.system("cls")
    if len(coordinate_list[0]) == 0: # Inicia en 0 porque es la primera vez que se ingresan los datos al sistema, utiliza len para corroborar que la lista esté vacía en la posición 0
        print("Ingresar las coordenadas de los tres sitios que más frecuenta (trabajo, casa, parque)")
        for i in range(3):
            latitude=float(input(f"Ingrese la latitud {i+1}: "))
            if (latitude < 6.077 or latitude > 6.284):
                print("Error coordenada")
                exit()
            else:
                lenght=float(input(f"Ingrese la longitud {i+1}: "))
                if (lenght < -76.049 or lenght > -75.841):
                    print("Error coordenada")
                    exit()
                else:
                    coordinate_list[i]=[latitude, lenght]
                    time.sleep(1)
    else:
        for i in range(3):
            print(f"Coordenada [Latitud, Longitud] {i+1} : {coordinate_list[i]}")
        lat= [coordinate_list[0][0],coordinate_list[1][0], coordinate_list[2][0]]
        le=[coordinate_list[0][1], coordinate_list[1][1], coordinate_list[2][1]]
        average_lat, average_le = sum(lat)/3, sum(le)/3

        north, south = lat.index(max(lat)), lat.index(min(lat))
        oriente, occidente = le.index(max(le)), le.index(min(le))
        print(f"La coordenada {oriente+1} es la que esta mas al oriente")
        print(f"Coordenada promedio de todos los puntos: latitud {average_lat}, longitud {average_le}")
        print("Presione 1,2 o 3 para actualizar la respectiva coordenada")
        print("presione 0 para regresar al menu")
        new_coordinate= int(input())
        if (new_coordinate == 0 or new_coordinate== ""):
            return
        else:
            if new_coordinate== 1 or new_coordinate==2 or new_coordinate==3:
                latitud=float(input("Ingrese la latitud: "))
                longitud=float(input("Ingrese la longitud: "))
                if (latitud < 6.077 or latitud > 6.284) and (longitud < -76.049 or longitud > -75.841):
                    print("Error coordenada")
                    exit()
                else:
                    coordinate_list[new_coordinate-1][0]= latitud
                    coordinate_list[new_coordinate-1][1]= longitud
            else:
                print("Error actualización")
                exit()

password_change(login_list)
current_coordinate_input(coordinate_list)