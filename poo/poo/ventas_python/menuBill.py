from components import Menu,Valida
from utilities import borrarPantalla,gotoxy,marco_lateral,mensaje,marco_inferior
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color,white_color,light_blue_color
from clsJson import JsonFile
from company  import Company
from customer import RegularClient,VipClient
from sales import Sale
from product  import Product
from iCrud import ICrud
import datetime
import time,os
from functools import reduce

path, _ = os.path.split(os.path.abspath(__file__))
# Procesos de las Opciones del Menu Facturacion
class CrudClients(ICrud):
    def create(self):
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
        gotoxy(60,2);print(cyan_color+"New client"+reset_color)
        gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
        gotoxy(2,2);print(green_color+"██"+reset_color)
        gotoxy(2,2);print(green_color+"██"+reset_color)
        gotoxy(130,2);print(green_color+"██"+reset_color)
        gotoxy(130,3);print(green_color+"██"+reset_color)
        gotoxy(2,3);print(green_color+"██"+reset_color)
        for i in range(4,30):
            gotoxy(2,i);print(green_color+"██"+reset_color)
            gotoxy(130,i);print(green_color+"██"+reset_color)
            
        gotoxy(2,30);print(green_color+"██"*65+reset_color)   
        gotoxy(10,4);print(f'{green_color}Elija el tipo de cliente a registrar:{reset_color}')
        gotoxy(10,6);print(f'1. Regular client{reset_color}')
        gotoxy(10,8);print(f'{yellow_color}2. ✨VIP client✨{reset_color}')
        gotoxy(60,9);print(f'{red_color}Ingrese 9 para salir.{reset_color}')
        gotoxy(2,11);print(green_color+"▄▄"*65+reset_color)
        gotoxy(10,10);tipo_cliente =input(f'{green_color}Tipo cliente: {reset_color}')
        

        if tipo_cliente == "9":
            gotoxy(45,20);print(f"{red_color} Regresando al menu Clientes... {reset_color}")
            time.sleep(2)

        elif tipo_cliente == "1":
            gotoxy(10,9);print(' '*100)
            gotoxy(10,14);print(purple_color+"DNI:"+reset_color)
            tipo = "Regular"
            while True:
                dni = validar.validar_cedula("Error: DNI inválido o incompleto", 15, 14)
                if len(dni) == 10 and validar.es_cedula_valida(dni):
                    break  # Sale del bucle si el DNI es válido
                gotoxy(15,14);print(red_color+"Error: DNI inválido o incompleto."+reset_color)
                time.sleep(2)
            json_file = JsonFile(path+'/archivos/clients.json')
            client_existe = json_file.find("dni",dni)

            if client_existe:
                gotoxy(50, 21)
                print(yellow_color+"Cliente ya existe!!"+reset_color)
                for i in range(3, 0, -1):
                    gotoxy(50, 23);print(f"{green_color} Espere {i} segundos... {reset_color}", end="\r")
                    time.sleep(1)
                self.create()
            else:
                gotoxy(10, 16);print(purple_color+"Nombre Completo:"+reset_color)
                first_name = validar.solo_letras( "Error: Solo letras", 26, 16).capitalize()
                gotoxy(10, 18);print(purple_color+"Apellido Completo:"+reset_color)
                last_name = validar.solo_letras( "Error: Solo letras", 30, 18).capitalize()
                gotoxy(10, 20);card = input(purple_color+"Tarjeta: "+reset_color).capitalize()
                gotoxy(10, 22);address= input(purple_color+"address: "+reset_color).capitalize()
                gotoxy(10, 24);print(f"{purple_color} Phone: {reset_color} ")
                phone = validar.validacion_telefono("Error: número incompleto", 18, 24).capitalize()
                client = RegularClient(first_name, last_name, dni, card,address,phone,tipo)
                gotoxy(50, 20);procesar = input(red_color+"¿Está seguro de grabar el cliente? (s/n): "+reset_color).lower()
                gotoxy(92, 20);print(green_color+"✔"+reset_color)

                if procesar == "s":
                    clients = json_file.read()
                    data = client.getJson()
                    clients.append(data)
                    json_file.save(clients)
                    gotoxy(50,23);print(yellow_color+"😊 Client Grabado satisfactoriamente 😊"+reset_color)
                    for i in range(3, 0, -1):
                        gotoxy(50, 25);print(f"{green_color} Regresando al menú Espere {i} segundos... {reset_color}", end="\r")
                        time.sleep(2)

                else:
                    gotoxy(50,23);print(red_color+"🤣 Client Cancelado 🤣"+reset_color)
                    for i in range(3, 0, -1):
                        gotoxy(50, 25);print(f"{green_color} Regresando al menú Espere {i} segundos... {reset_color}", end="\r")
                        time.sleep(2)
                    borrarPantalla()
                    menu_clients.menu()
                
        elif tipo_cliente == "2":
            tipo = "VIP"
            gotoxy(10,9);print(' '*100)
            gotoxy(10,14);print(purple_color+"DNI:"+reset_color)
            while True:
                dni = validar.validar_cedula("Error: DNI inválido o incompleto", 15, 14)
                if len(dni) == 10 and validar.es_cedula_valida(dni):
                    break  # Sale del bucle si el DNI es válido
                gotoxy(15,14);print(red_color+"Error: DNI inválido o incompleto."+reset_color)
                time.sleep(2)
            json_file = JsonFile(path+'/archivos/clients.json')
            client_existe = json_file.find("dni",dni)
            if  client_existe:
                gotoxy(50, 21)
                print(yellow_color+"Cliente ya existe!!"+reset_color)
                for i in range(3, 0, -1):
                    gotoxy(50, 23);print(f"{green_color} Espere {i} segundos... {reset_color}", end="\r")
                    time.sleep(1)
                self.create()
                
            else:
                gotoxy(10, 16);print(purple_color+"Nombre Completo:"+reset_color)
                first_name = validar.solo_letras( "Error: Solo letras", 26, 16).capitalize()
                gotoxy(10, 18);print(purple_color+"Apellido Completo:"+reset_color)
                last_name = validar.solo_letras( "Error: Solo letras", 30, 18).capitalize()
                gotoxy(10, 20);card = input(purple_color+"Tarjeta: "+reset_color).capitalize()
                gotoxy(10, 22);address= input(purple_color+"address: "+reset_color).capitalize()
                gotoxy(10, 24);print(f"{purple_color} Phone: {reset_color} ")
                phone = validar.validacion_telefono("Error: número incompleto", 18, 24).capitalize()
                
                gotoxy(10, 26);valor = int(input(purple_color+"Valor: "+reset_color))
                client = VipClient(first_name, last_name, dni,address,phone,tipo)

                client.limit = valor if valor else None

                gotoxy(10, 20);procesar = input(red_color+"Esta seguro de grabar el Client(s/n): "+reset_color).lower()
                gotoxy(52, 20);print(green_color+"✔"+reset_color)

                if procesar == "s":
                    clients = json_file.read()
                    data = client.getJson()
                    clients.append(data)
                    json_file.save(clients)
                    gotoxy(50,23);print(yellow_color+"😊 Client Grabado satisfactoriamente 😊"+reset_color)
                    for i in range(3, 0, -1):
                        gotoxy(50, 25);print(f"{green_color} Regresando al menú Espere {i} segundos... {reset_color}", end="\r")
                        time.sleep(2)

                    borrarPantalla()
                   
                else:
                    gotoxy(50,23);print(red_color+"🤣 Client Cancelado 🤣"+reset_color)
                    for i in range(3, 0, -1):
                        gotoxy(50, 25);print(f"{green_color} Regresando al menú Espere {i} segundos... {reset_color}", end="\r")
                        time.sleep(2)
                    borrarPantalla()
                    menu_clients.menu()
                
        else  :
            gotoxy(50, 20)
            print(yellow_color+"Opcion incorrecta "+reset_color)
            for i in range(3, 0, -1):
                gotoxy(50, 23);print(f"{green_color} Espere {i} segundos... {reset_color}", end="\r")
                time.sleep(1)
            self.create()

    def update(self):
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(light_blue_color+"▄▄"*65+reset_color)
        gotoxy(60,2);print(yellow_color+"New client"+reset_color)
        gotoxy(2,3);print(light_blue_color+"▄▄"*65+reset_color)
        gotoxy(2,2);print(green_color+"██"+reset_color)
        gotoxy(2,3);print(green_color+"██"+reset_color)
        gotoxy(130,2);print(green_color+"██"+reset_color)
        gotoxy(130,3);print(green_color+"██"+reset_color)
        gotoxy(2,3);print(green_color+"██"+reset_color)
        for i in range(4,30):
            gotoxy(2,i);print(green_color+"██"+reset_color)
            gotoxy(130,i);print(green_color+"██"+reset_color)
            
        gotoxy(2,30);print(green_color+"██"*65+reset_color)
        gotoxy(7, 6);print(f'{yellow_color}Desea salir presione 9 si no 0 para continuar:{reset_color}')
        gotoxy(53, 6);opcion= input()
        gotoxy(7, 6);print(" "*50)
       
        if int(opcion) == 9:
            gotoxy(45,20);print(f"{red_color} Regresando al menu Clientes... {reset_color}")
            time.sleep(2)
            
            
        elif int(opcion) == 0:
            
            while True:
                gotoxy(7, 6); print(f"\033[33mIngrese el DNI del cliente: \033[0m")
                dni = validar.validar_cedula("Error: DNI inválido o incompleto", 35, 6)
                if len(dni) == 10 and validar.es_cedula_valida(dni):
                    json_file = JsonFile(path+'/archivos/clients.json')
                    clientes = json_file.find("dni",dni)
                    if not clientes:
                        gotoxy(40, 15); print("\033[31mIngresa la ID correcta Por Favor!\033[0m")
                        for i in range(5, 0, -1):
                            gotoxy(40, 16); print(f"\033[31mEspere {i} segundos...\033[0m", end="\r")
                            time.sleep(1)
                    else:
                        borrarPantalla()
                        for client in  clientes:
                            gotoxy(25,8);print(cyan_color+"█"*35+reset_color)
                            gotoxy(60,8);print(green_color+"█"*35+reset_color)
                            for i in range(8,19):
                                gotoxy(25,i);print(green_color+"██"+reset_color)
                                gotoxy(95,i);print(green_color+"██"+reset_color)
                            gotoxy(25,18);print(green_color+"█"*35+reset_color)
                            gotoxy(60,18);print(cyan_color+"█"*35+reset_color)
                            menu_main = Menu(f"{yellow_color}Actualizacion de datos del cliente:  {client['nombre']}{reset_color}",["1) Direccion","2) Telefono","3) Salir"],45,10)
                            opc = menu_main.menu()    
                            if opc == "1":
                                borrarPantalla()
                                gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
                                gotoxy(60,2);print(cyan_color+"ACTUALIZACION DE DATOS"+reset_color)
                                gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
                                gotoxy(2,2);print(green_color+"██"+reset_color)
                                gotoxy(130,2);print(green_color+"██"+reset_color)
                                gotoxy(130,3);print(green_color+"██"+reset_color)
                                gotoxy(2,3);print(green_color+"██"+reset_color)
                                for i in range(4,30):
                                    gotoxy(2,i);print(green_color+"██"+reset_color)
                                    gotoxy(130,i);print(green_color+"██"+reset_color)
                                gotoxy(2,30);print(green_color+"██"*65+reset_color)    
                                
                                gotoxy(8,5);print(cyan_color+"Datos actuales del cliente:"+reset_color)
                                print("\n")
                                gotoxy(8,7);print(f"{yellow_color}DNI:{reset_color}")
                                gotoxy(8,9);print(client['dni'])
                                gotoxy(30,7);print(f"{yellow_color}NOMBRE:{reset_color}")
                                gotoxy(30,9);print(client['nombre'])
                                gotoxy(52,7);print(f"{yellow_color}APELLIDO:{reset_color}")
                                gotoxy(52,9);print(client['apellido'])
                                gotoxy(74,7);print(f"{yellow_color}VALOR:{reset_color}")
                                gotoxy(74,9);print(client['valor'])
                                gotoxy(96,7);print(f"{yellow_color}DIRECCION:{reset_color}")
                                gotoxy(96,9);print(client['adress'])
                                gotoxy(118,7);print(f"{yellow_color}TELEFONO:{reset_color}")
                                gotoxy(118,9);print(client['phone'])
                                gotoxy(50,25);update_choice = input(f"{red_color}¿Desea modificar la dirección? (s/n): {reset_color}").lower()
                                borrarPantalla()
                                if update_choice == "s":
                                    gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
                                    gotoxy(60,2);print(cyan_color+"ACTUALIZACION DE DATOS"+reset_color)
                                    gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
                                    gotoxy(2,2);print(green_color+"██"+reset_color)
                                    gotoxy(2,2);print(green_color+"██"+reset_color)
                                    gotoxy(130,2);print(green_color+"██"+reset_color)
                                    gotoxy(130,3);print(green_color+"██"+reset_color)
                                    gotoxy(2,3);print(green_color+"██"+reset_color)
                                    gotoxy(2,3);print(green_color+"██"+reset_color)
                                    for i in range(4,30):
                                        gotoxy(2,i);print(green_color+"██"+reset_color)
                                        gotoxy(130,i);print(green_color+"██"+reset_color)
                                        
                                    gotoxy(2,30);print(green_color+"██"*65+reset_color)  
                                    gotoxy(8,5);print(cyan_color+"Datos actuales del cliente:"+reset_color)
                                    print("\n")
                                    gotoxy(8,7);print(f"{yellow_color}DNI:{reset_color}")
                                    gotoxy(8,9);print(client['dni'])
                                    gotoxy(30,7);print(f"{yellow_color}NOMBRE:{reset_color}")
                                    gotoxy(30,9);print(client['nombre'])
                                    gotoxy(52,7);print(f"{yellow_color}APELLIDO:{reset_color}")
                                    gotoxy(52,9);print(client['apellido'])
                                    gotoxy(74,7);print(f"{yellow_color}VALOR:{reset_color}")
                                    gotoxy(74,9);print(client['valor'])
                                    gotoxy(96,7);print(f"{yellow_color}DIRECCION:{reset_color}")
                                    gotoxy(118,7);print(f"{yellow_color}TELEFONO:{reset_color}")
                                    gotoxy(118,9);print(client['phone'])
                                    gotoxy(96,9);print(" "*10)
                                    gotoxy(96,9);new_address = input()
                                    client['adress'] = new_address
                                    json_file.update('dni', clientes[0]['dni'], client)
                                    gotoxy(50,25);print(cyan_color+"Dirección actualizada correctamente."+reset_color)
                                    time.sleep(3)
                                    self.update()
                                
                                else:
                                    gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
                                    gotoxy(60,2);print(cyan_color+"ACTUALIZACION DE DATOS"+reset_color)
                                    gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
                                    gotoxy(2,2);print(green_color+"██"+reset_color)
                                    gotoxy(2,2);print(green_color+"██"+reset_color)
                                    gotoxy(130,2);print(green_color+"██"+reset_color)
                                    gotoxy(130,3);print(green_color+"██"+reset_color)
                                    gotoxy(2,3);print(green_color+"██"+reset_color)
                                    gotoxy(2,3);print(green_color+"██"+reset_color)
                                    for i in range(4,30):
                                        gotoxy(2,i);print(green_color+"██"+reset_color)
                                        gotoxy(130,i);print(green_color+"██"+reset_color)
                                    gotoxy(2,30);print(green_color+"██"*65+reset_color)  
                                    gotoxy(8,5);print(cyan_color+"Datos actuales del cliente:"+reset_color)
                                    print("\n")
                                    gotoxy(8,7);print(f"{yellow_color}DNI:{reset_color}")
                                    gotoxy(8,9);print(client['dni'])
                                    gotoxy(30,7);print(f"{yellow_color}NOMBRE:{reset_color}")
                                    gotoxy(30,9);print(client['nombre'])
                                    gotoxy(52,7);print(f"{yellow_color}APELLIDO:{reset_color}")
                                    gotoxy(52,9);print(client['apellido'])
                                    gotoxy(74,7);print(f"{yellow_color}VALOR:{reset_color}")
                                    gotoxy(74,9);print(client['valor'])
                                    gotoxy(96,7);print(f"{yellow_color}DIRECCION:{reset_color}")
                                    gotoxy(96,9);print(client['adress'])
                                    gotoxy(118,7);print(f"{yellow_color}TELEFONO:{reset_color}")
                                    gotoxy(118,9);print(client['phone'])
                                    gotoxy(50,25);print(f"{cyan_color}🫣 No se modificó la direccion. 🫣{reset_color}")
                                    time.sleep(3)
                                    self.update()
                            elif opc == "2":
                                borrarPantalla()
                                gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
                                gotoxy(60,2);print(cyan_color+"ACTUALIZACION DE DATOS"+reset_color)
                                gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
                                gotoxy(2,2);print(green_color+"██"+reset_color)
                                gotoxy(2,2);print(green_color+"██"+reset_color)
                                gotoxy(130,2);print(green_color+"██"+reset_color)
                                gotoxy(130,3);print(green_color+"██"+reset_color)
                                gotoxy(2,3);print(green_color+"██"+reset_color)
                                for i in range(4,30):
                                    gotoxy(2,i);print(green_color+"██"+reset_color)
                                    gotoxy(130,i);print(green_color+"██"+reset_color)
                                    
                                gotoxy(2,30);print(green_color+"██"*65+reset_color)  
                                gotoxy(2,3);print(green_color+"██"+reset_color)
                                gotoxy(8,5);print(cyan_color+"Datos actuales del cliente:"+reset_color)
                                print("\n")
                                gotoxy(8,7);print(f"{yellow_color}DNI:{reset_color}")
                                gotoxy(8,9);print(client['dni'])
                                gotoxy(30,7);print(f"{yellow_color}NOMBRE:{reset_color}")
                                gotoxy(30,9);print(client['nombre'])
                                gotoxy(52,7);print(f"{yellow_color}APELLIDO:{reset_color}")
                                gotoxy(52,9);print(client['apellido'])
                                gotoxy(74,7);print(f"{yellow_color}VALOR:{reset_color}")
                                gotoxy(74,9);print(client['valor'])
                                gotoxy(96,7);print(f"{yellow_color}DIRECCION:{reset_color}")
                                gotoxy(96,9);print(client['adress'])
                                gotoxy(118,7);print(f"{yellow_color}TELEFONO:{reset_color}")
                                gotoxy(118,9);print(client['phone'])
                                
                                gotoxy(50,25);update_choice = input(f"{red_color}¿Desea modificar la Telefono? (s/n): {reset_color}").lower()
                                borrarPantalla()
                                if update_choice == "s":
                                    gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
                                    gotoxy(60,2);print(cyan_color+"ACTUALIZACION DE DATOS"+reset_color)
                                    gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
                                    gotoxy(2,2);print(green_color+"██"+reset_color)
                                    gotoxy(2,2);print(green_color+"██"+reset_color)
                                    gotoxy(130,2);print(green_color+"██"+reset_color)
                                    gotoxy(130,3);print(green_color+"██"+reset_color)
                                    gotoxy(2,3);print(green_color+"██"+reset_color)
                                    gotoxy(2,3);print(green_color+"██"+reset_color)
                                    for i in range(4,30):
                                        gotoxy(2,i);print(green_color+"██"+reset_color)
                                        gotoxy(130,i);print(green_color+"██"+reset_color)
                                        
                                    gotoxy(2,30);print(green_color+"██"*65+reset_color)  
                                    gotoxy(8,5);print(cyan_color+"Datos actuales del cliente:"+reset_color)
                                    print("\n")
                                    gotoxy(8,7);print(f"{yellow_color}DNI:{reset_color}")
                                    gotoxy(8,9);print(client['dni'])
                                    gotoxy(30,7);print(f"{yellow_color}NOMBRE:{reset_color}")
                                    gotoxy(30,9);print(client['nombre'])
                                    gotoxy(52,7);print(f"{yellow_color}APELLIDO:{reset_color}")
                                    gotoxy(52,9);print(client['apellido'])
                                    gotoxy(74,7);print(f"{yellow_color}VALOR:{reset_color}")
                                    gotoxy(74,9);print(client['valor'])
                                    gotoxy(96,7);print(f"{yellow_color}DIRECCION:{reset_color}")
                                    gotoxy(96,9);print(client['adress'])
                                    gotoxy(118,7);print(f"{yellow_color}TELEFONO:{reset_color}")
                                    gotoxy(118,9);print(client['phone'])
                                    gotoxy(118,9);print(" "*10)
                                    new_phone = validar.validacion_telefono("Error: número incompleto", 118, 9)
                                    client['phone'] = new_phone
                                    json_file.update('phone', clientes[0]['phone'], client)
                                    gotoxy(50,25);print(cyan_color+"Telefono actualizada correctamente."+reset_color)
                                    time.sleep(3)
                                    self.update()
                                else:
                                    gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
                                    gotoxy(60,2);print(cyan_color+"ACTUALIZACION DE DATOS"+reset_color)
                                    gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
                                    gotoxy(2,2);print(green_color+"██"+reset_color)
                                    gotoxy(2,2);print(green_color+"██"+reset_color)
                                    gotoxy(130,2);print(green_color+"██"+reset_color)
                                    gotoxy(130,3);print(green_color+"██"+reset_color)
                                    gotoxy(2,3);print(green_color+"██"+reset_color)
                                    gotoxy(2,3);print(green_color+"██"+reset_color)
                                    for i in range(4,30):
                                        gotoxy(2,i);print(green_color+"██"+reset_color)
                                        gotoxy(130,i);print(green_color+"██"+reset_color)
                                        
                                    gotoxy(2,30);print(green_color+"██"*65+reset_color)  
                                    gotoxy(8,5);print(cyan_color+"Datos actuales del cliente:"+reset_color)
                                    print("\n")
                                    gotoxy(8,7);print(f"{yellow_color}DNI:{reset_color}")
                                    gotoxy(8,9);print(client['dni'])
                                    gotoxy(30,7);print(f"{yellow_color}NOMBRE:{reset_color}")
                                    gotoxy(30,9);print(client['nombre'])
                                    gotoxy(52,7);print(f"{yellow_color}APELLIDO:{reset_color}")
                                    gotoxy(52,9);print(client['apellido'])
                                    gotoxy(74,7);print(f"{yellow_color}VALOR:{reset_color}")
                                    gotoxy(74,9);print(client['valor'])
                                    gotoxy(96,7);print(f"{yellow_color}DIRECCION:{reset_color}")
                                    gotoxy(96,9);print(client['adress'])
                                    gotoxy(118,7);print(f"{yellow_color}TELEFONO:{reset_color}")
                                    gotoxy(118,9);print(client['phone'])
                                    gotoxy(50,25);print(f"{cyan_color}🫣 No se modificó el teléfono. 🫣{reset_color}")
                                    time.sleep(3)
                                    self.update()
                            elif opc == "3":
                                self.update()
                                    
                            else  :
                                gotoxy(50, 20)
                                print(yellow_color+"Opcion incorrecta "+reset_color)
                                for i in range(3, 0, -1):
                                    gotoxy(50, 23);print(f"{green_color} Espere {i} segundos... {reset_color}", end="\r")
                                    time.sleep(1)
                            borrarPantalla()
                break

            


    def delete(self):
        validar = Valida()
        print('\033c', end='')
        gotoxy(25,8);print(cyan_color+"█"*35+reset_color)
        gotoxy(60,8);print(green_color+"█"*35+reset_color)
        for i in range(8,19):
            gotoxy(25,i);print(green_color+"██"+reset_color)
            gotoxy(95,i);print(green_color+"██"+reset_color)
        gotoxy(25,18);print(green_color+"█"*35+reset_color)
        gotoxy(60,18);print(cyan_color+"█"*35+reset_color)
        while True:
            gotoxy(48, 12); print(f"\033[33mIngrese el DNI del cliente: \033[0m")
            dni = validar.validar_cedula("Error: DNI inválido o incompleto", 53, 13)
            if len(dni) == 10 and validar.es_cedula_valida(dni):
                json_file = JsonFile(path+'/archivos/clients.json')
                clientes = json_file.find("dni",dni)
                if not clientes:
                    gotoxy(40, 15); print("\033[31mIngresa la ID correcta Por Favor!\033[0m")
                    for i in range(5, 0, -1):
                        gotoxy(40, 16); print(f"\033[31mEspere {i} segundos...\033[0m", end="\r")
                        time.sleep(1)
                if clientes:
                    borrarPantalla()
                    for client in clientes:
                        gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
                        gotoxy(60,2);print(red_color+"ELIMINACION DE CLIENTE"+reset_color)
                        gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
                        gotoxy(2,2);print(green_color+"██"+reset_color)
                        gotoxy(130,2);print(green_color+"██"+reset_color)
                        gotoxy(130,3);print(green_color+"██"+reset_color)
                        gotoxy(2,3);print(green_color+"██"+reset_color)
                        for i in range(4,30):
                            gotoxy(2,i);print(green_color+"██"+reset_color)
                            gotoxy(130,i);print(green_color+"██"+reset_color)
                        gotoxy(2,30);print(green_color+"██"*65+reset_color)    

                        gotoxy(8,5);print(cyan_color+"Datos actuales del cliente:"+reset_color)
                        print("\n")
                        gotoxy(8,7);print(f"{yellow_color}DNI:{reset_color}")
                        gotoxy(8,9);print(client['dni'])
                        gotoxy(30,7);print(f"{yellow_color}NOMBRE:{reset_color}")
                        gotoxy(30,9);print(client['nombre'])
                        gotoxy(52,7);print(f"{yellow_color}APELLIDO:{reset_color}")
                        gotoxy(52,9);print(client['apellido'])
                        gotoxy(74,7);print(f"{yellow_color}VALOR:{reset_color}")
                        gotoxy(74,9);print(client['valor'])
                        gotoxy(96,7);print(f"{yellow_color}DIRECCION:{reset_color}")
                        gotoxy(96,9);print(client['adress'])
                        gotoxy(118,7);print(f"{yellow_color}TELEFONO:{reset_color}")
                        gotoxy(118,9);print(client['phone'])
                        gotoxy(45,25);update_choice = input(f"{red_color}¿Estás seguro de eliminar este Cliente 😢? (s/n):{reset_color} ").lower()
                        while True:
                            if update_choice in ["s", "n"]:
                                break
                            else:
                                gotoxy(40, 15);print("Seleccione una opción válida.")
                        if update_choice == "s":
                            json_file.delete_by_id_or_dni('dni', dni)
                            gotoxy(45,27);print(f"{red_color}Cliente eliminado correctamente.{reset_color}")
                            time.sleep(3)
                            self.delete()
                        elif update_choice == "n":
                            gotoxy(45,27);print(f"{yellow_color}Gracias por no eliminar al cliente TQM❤️{reset_color}")
                            time.sleep(3)
            break                
            


    def consult(self):
        borrarPantalla()
        line = 10
        gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
        gotoxy(60,2);print(yellow_color+"Consulta de cliente"+reset_color)
        gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
        gotoxy(2,2);print(green_color+"██"+reset_color)
        gotoxy(130,2);print(green_color+"██"+reset_color)
        gotoxy(130,3);print(green_color+"██"+reset_color)
        gotoxy(2,3);print(green_color+"██"+reset_color)
        for i in range(4,30):
            gotoxy(2,i);print(green_color+"██"+reset_color)
            gotoxy(130,i);print(green_color+"██"+reset_color)
        gotoxy(2,30);print(green_color+"██"*65+reset_color) 
        gotoxy(8,5);print(red_color+"Datos actuales del cliente:"+reset_color)
        print("\n")  
        gotoxy(8,7);clientes = input(f"{yellow_color}Ingrese la identificacion del cliente (deje en blanco para mostrar todos):{reset_color} ")
        if clientes.strip() == '':
            # Mostrar todos los clientes
            json_file = JsonFile(path+'/archivos/clients.json')
            clientes = json_file.read()
            borrarPantalla()
            gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
            gotoxy(60,2);print(yellow_color+"Consulta de cliente"+reset_color)
            gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
            gotoxy(2,2);print(green_color+"██"+reset_color)
            gotoxy(130,2);print(green_color+"██"+reset_color)
            gotoxy(130,3);print(green_color+"██"+reset_color)
            gotoxy(2,3);print(green_color+"██"+reset_color)
            for i in range(4,30):
                gotoxy(2,i);print(green_color+"██"+reset_color)
                gotoxy(130,i);print(green_color+"██"+reset_color)
            gotoxy(2,30);print(green_color+"██"*65+reset_color) 
            gotoxy(8,5);print(red_color+"Datos actuales del cliente:"+reset_color)
            print("\n")  

            gotoxy(8,7);print(f"{yellow_color}DNI:{reset_color}")
            gotoxy(25,7);print(f"{yellow_color}NOMBRE:{reset_color}")
            gotoxy(40,7);print(f"{yellow_color}APELLIDO:{reset_color}")
            gotoxy(55,7);print(f"{yellow_color}VALOR:{reset_color}")
            gotoxy(70,7);print(f"{yellow_color}DIRECCION:{reset_color}")
            gotoxy(90,7);print(f"{yellow_color}TELEFONO:{reset_color}")
            gotoxy(110,7);print(f"{yellow_color}Cliente:{reset_color}")
            for client in clientes:
                gotoxy(8,line);print(client['dni'])
                gotoxy(25,line);print(client['nombre'])
                gotoxy(40,line);print(client['apellido'])
                gotoxy(55,line);print(client['valor'])
                gotoxy(70,line);print(client['adress'])
                gotoxy(90,line);print(client['phone'])
                gotoxy(110,line);print(client['tipoclient'])
                line += 2
        elif clientes.isdigit():  # Verificar que la entrada sea numérica
            json_file = JsonFile(path+'/archivos/clients.json')
            cliente = json_file.find("dni", clientes)
            if cliente:
                cliente_info = cliente[0]  # Acceder al primer elemento de la lista
                borrarPantalla()
                gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
                gotoxy(60,2);print(yellow_color+"Consulta de cliente"+reset_color)
                gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
                gotoxy(2,2);print(green_color+"██"+reset_color)
                gotoxy(130,2);print(green_color+"██"+reset_color)
                gotoxy(130,3);print(green_color+"██"+reset_color)
                gotoxy(2,3);print(green_color+"██"+reset_color)
                for i in range(4,30):
                    gotoxy(2,i);print(green_color+"██"+reset_color)
                    gotoxy(130,i);print(green_color+"██"+reset_color)
                gotoxy(2,30);print(green_color+"██"*65+reset_color) 
                gotoxy(8,5);print(red_color+"Datos actuales del cliente:"+reset_color)
                print("\n")  

                gotoxy(8,7);print(f"{yellow_color}DNI:{reset_color}")
                gotoxy(25,7);print(f"{yellow_color}NOMBRE:{reset_color}")
                gotoxy(40,7);print(f"{yellow_color}APELLIDO:{reset_color}")
                gotoxy(55,7);print(f"{yellow_color}VALOR:{reset_color}")
                gotoxy(70,7);print(f"{yellow_color}DIRECCION:{reset_color}")
                gotoxy(90,7);print(f"{yellow_color}TELEFONO:{reset_color}")
                gotoxy(110,7);print(f"{yellow_color}Cliente:{reset_color}")
                
                gotoxy(8,line);print(f'{cliente_info['dni']}')
                gotoxy(25,line);print(f'{cliente_info['nombre']}')
                gotoxy(40,line);print(f'{cliente_info['apellido']}')
                gotoxy(55,line);print(f'{cliente_info['valor']}')
                gotoxy(70,line);print(f'{cliente_info['adress']}')
                gotoxy(90,line);print(f'{cliente_info['phone']}')
                gotoxy(110,line);print(f'{cliente_info['tipoclient']}')
            else:
                print("No se encontró esa identificación.")
                print("Ingresa la identificación correcta, por favor.")
                for i in range(5, 0, -1):
                    print(f"Espere {i} segundos...", end="\r")
                    time.sleep(1)
        else:
            gotoxy(85,7);print("Error: Identificacion inválida.")
            time.sleep(2)
        
            self.consult()
        
        gotoxy(45,4+line);x= input(f"{red_color}Presione una tecla para continuar...{reset_color}")







class CrudProducts(ICrud):
    def create(self):
        validar = Valida()
        # Cargar datos del JSON para verificar ID existente
        json_file = JsonFile(path + '/archivos/products.json')
        existing_ids = [product["id"] for product in json_file.read()]  # Obtener todas las IDs existentes
        existing_product = [product["descripcion"] for product in json_file.read()]  # Obtener todos los nombres de productos existentes
        
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
        gotoxy(60,2);print(cyan_color+"Nuevo Producto"+reset_color)
        gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
        gotoxy(2,2);print(green_color+"██"+reset_color)
        gotoxy(2,2);print(green_color+"██"+reset_color)
        gotoxy(130,2);print(green_color+"██"+reset_color)
        gotoxy(130,3);print(green_color+"██"+reset_color)
        gotoxy(2,3);print(green_color+"██"+reset_color)
        for i in range(4,30):
            gotoxy(2,i);print(green_color+"██"+reset_color)
            gotoxy(130,i);print(green_color+"██"+reset_color)
            
        gotoxy(2,30);print(green_color+"██"*65+reset_color)  
        gotoxy(8,7);print(f"{yellow_color}ID:{reset_color}")
        id = validar.id_existe(existing_ids, "Error: ID invalido o existente", 8, 9)  # Verificar ID existente
        gotoxy(30,7);print(f"{yellow_color}Descripcion:{reset_color}")
        descripcion = validar.nombre_existe(existing_product, "Error: Ya existe ese nombre de producto", 30, 9)
        gotoxy(52,7);print(f"{yellow_color}Precio:{reset_color}")
        precio = validar.solo_numeros("Error: Solo números", 52, 9)
        gotoxy(74,7);print(f"{yellow_color}Stock:{reset_color}")
        stock = validar.solo_numeros("Error: Solo números", 74, 9)
        
        gotoxy(50, 25); print(red_color + "¿Está seguro de grabar el producto? (s/n):")
        gotoxy(95, 25);procesar = input().lower()
        if procesar == "s":
            product_data = {
                "id": int(id),
                "descripcion": descripcion,
                "precio": float(precio),
                "stock": int(stock)
            }
            json_data = json_file.read()  # Leer los datos del archivo JSON
            json_data.append(product_data)  # Agregar el nuevo producto a los datos existentes
            json_data.sort(key=lambda x: x["id"])  # Ordenar la lista de productos por ID
            json_file.save(json_data)  # Escribir los datos actualizados de nuevo al archivo JSON
            gotoxy(50, 27);print(f"{yellow_color}Producto registrado exitosamente.{reset_color}")
        else:
            gotoxy(50,27);print(f"🤣{yellow_color} Producto Cancelado 🤣{reset_color}")
        time.sleep(2)
        
        
        
        
        
        
    def update(self):
        validar = Valida()
        json_file = JsonFile(path + '/archivos/products.json')
        existing_ids = [str(product["id"]) for product in json_file.read()]  # Convert IDs to strings for comparison
        print('\033c', end='')
        gotoxy(2,1);print(light_blue_color+"▄▄"*65+reset_color)
        gotoxy(60,2);print(yellow_color+"Actualizar Producto"+reset_color)
        gotoxy(2,3);print(light_blue_color+"▄▄"*65+reset_color)
        gotoxy(2,2);print(green_color+"██"+reset_color)
        gotoxy(2,3);print(green_color+"██"+reset_color)
        gotoxy(130,2);print(green_color+"██"+reset_color)
        gotoxy(130,3);print(green_color+"██"+reset_color)
        gotoxy(2,3);print(green_color+"██"+reset_color)
        for i in range(4,30):
            gotoxy(2,i);print(green_color+"██"+reset_color)
            gotoxy(130,i);print(green_color+"██"+reset_color)
            
        gotoxy(2,30);print(green_color+"██"*65+reset_color)
        gotoxy(7, 6);print(f'{yellow_color}Desea salir presione 9 si no 0 para continuar:{reset_color}')
        gotoxy(53, 6);opcion= input()
        gotoxy(7, 6);print(" "*50)
    
        if int(opcion) == 9:
            gotoxy(45,20);print(f"{red_color} Regresando al menu Producto... {reset_color}")
            time.sleep(2)
            borrarPantalla()
            
        elif int(opcion) == 0:
            while True:
                gotoxy(7, 6); print(f"\033[33mIngrese el ID del producto: \033[0m")
                product_id = validar.id_existe_producto(existing_ids, "Error: ID inválido o incompleto", 35, 6)
                
                # Ensure product_id is a string
                product_id_str = str(product_id)
                
                # Check if the string consists of digits
                product_id_int = int(product_id_str) if product_id_str.isdigit() else None

                json_file = JsonFile(path+'/archivos/products.json')  # Assuming the path to your products JSON file
                products = json_file.find("id", product_id_int)
                
                if not products:
                    gotoxy(40, 15); print("\033[31mProducto no encontrado. Ingresa un ID válido.\033[0m")
                    for i in range(5, 0, -1):
                        gotoxy(40, 16); print(f"\033[31mEspere {i} segundos...\033[0m", end="\r")
                        time.sleep(1)
                    self.update()
                else:
                    borrarPantalla()
                    for product in products:
                        gotoxy(25,8);print(cyan_color+"█"*35+reset_color)
                        gotoxy(60,8);print(green_color+"█"*35+reset_color)
                        for i in range(8,19):
                            gotoxy(25,i);print(green_color+"██"+reset_color)
                            gotoxy(95,i);print(green_color+"██"+reset_color)
                        gotoxy(25,18);print(green_color+"█"*35+reset_color)
                        gotoxy(60,18);print(cyan_color+"█"*35+reset_color)
                        menu_main = Menu(f"{yellow_color}Actualizacion de datos del cliente:  {product['descripcion']}{reset_color}",["1) Precio","2) Stock","3) Salir"],45,10)
                        opc = menu_main.menu()    
                        if opc == "1":
                            borrarPantalla()
                            gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
                            gotoxy(60,2);print(cyan_color+"ACTUALIZACION DE PRODUCTO"+reset_color)
                            gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
                            gotoxy(2,2);print(green_color+"██"+reset_color)
                            gotoxy(130,2);print(green_color+"██"+reset_color)
                            gotoxy(130,3);print(green_color+"██"+reset_color)
                            gotoxy(2,3);print(green_color+"██"+reset_color)
                            for i in range(4,30):
                                gotoxy(2,i);print(green_color+"██"+reset_color)
                                gotoxy(130,i);print(green_color+"██"+reset_color)
                            gotoxy(2,30);print(green_color+"██"*65+reset_color)    
                                
                            gotoxy(8,5);print(cyan_color+"Datos actuales del cliente:"+reset_color)
                            print("\n")
                            gotoxy(8,7);print(f"{yellow_color}ID:{reset_color}")
                            gotoxy(8,9);print(product['id'])
                            gotoxy(30,7);print(f"{yellow_color}DESCRIPCION:{reset_color}")
                            gotoxy(30,9);print(product['descripcion'])
                            gotoxy(52,7);print(f"{yellow_color}PRECIO:{reset_color}")
                            gotoxy(52,9);print(product['precio'])
                            gotoxy(74,7);print(f"{yellow_color}STOCK:{reset_color}")
                            gotoxy(74,9);print(product['stock'])
                            
                            gotoxy(50,25);update_choice = input(f"{red_color}¿Desea modificar el precio? (s/n): {reset_color}").lower()
                            borrarPantalla()
                            if update_choice == "s":
                                gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
                                gotoxy(60,2);print(cyan_color+"ACTUALIZACION DE PRODUCTO"+reset_color)
                                gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
                                gotoxy(2,2);print(green_color+"██"+reset_color)
                                gotoxy(2,2);print(green_color+"██"+reset_color)
                                gotoxy(130,2);print(green_color+"██"+reset_color)
                                gotoxy(130,3);print(green_color+"██"+reset_color)
                                gotoxy(2,3);print(green_color+"██"+reset_color)
                                gotoxy(2,3);print(green_color+"██"+reset_color)
                                for i in range(4,30):
                                    gotoxy(2,i);print(green_color+"██"+reset_color)
                                    gotoxy(130,i);print(green_color+"██"+reset_color)    
                                        
                                gotoxy(2,30);print(green_color+"██"*65+reset_color)  
                                gotoxy(8,5);print(cyan_color+"Datos actuales del cliente:"+reset_color)
                                print("\n")
                                gotoxy(8,7);print(f"{yellow_color}ID:{reset_color}")
                                gotoxy(8,9);print(product['id'])
                                gotoxy(30,7);print(f"{yellow_color}DESCRIPCION:{reset_color}")
                                gotoxy(30,9);print(product['descripcion'])
                                gotoxy(52,7);print(f"{yellow_color}PRECIO:{reset_color}")
                                
                                gotoxy(74,7);print(f"{yellow_color}STOCK:{reset_color}")
                                gotoxy(74,9);print(product['stock'])
    
                                gotoxy(52,9);print(" "*10)
                                new_precio = validar.solo_numeros("Error: solo numero", 52, 9)
                               
                                product['precio'] = float(new_precio)
                                json_file.update('id', products[0]['id'], product)
                                products_sorted = sorted(json_file.read(), key=lambda x: x['id'])
                                json_file.save(products_sorted)
                                gotoxy(50,25);print(cyan_color+"precio actualizada correctamente."+reset_color)
                                time.sleep(3)
                                self.update()
                                
                            else:
                                borrarPantalla()
                                gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
                                gotoxy(60,2);print(cyan_color+"ACTUALIZACION DE PRODUCTO"+reset_color)
                                gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
                                gotoxy(2,2);print(green_color+"██"+reset_color)
                                gotoxy(130,2);print(green_color+"██"+reset_color)
                                gotoxy(130,3);print(green_color+"██"+reset_color)
                                gotoxy(2,3);print(green_color+"██"+reset_color)
                                for i in range(4,30):
                                    gotoxy(2,i);print(green_color+"██"+reset_color)
                                    gotoxy(130,i);print(green_color+"██"+reset_color)
                                gotoxy(2,30);print(green_color+"██"*65+reset_color)    
                                    
                                gotoxy(8,5);print(cyan_color+"Datos actuales del cliente:"+reset_color)
                                print("\n")
                                gotoxy(8,7);print(f"{yellow_color}ID:{reset_color}")
                                gotoxy(8,9);print(product['id'])
                                gotoxy(30,7);print(f"{yellow_color}DESCRIPCION:{reset_color}")
                                gotoxy(30,9);print(product['descripcion'])
                                gotoxy(52,7);print(f"{yellow_color}PRECIO:{reset_color}")
                                gotoxy(52,9);print(product['precio'])
                                gotoxy(74,7);print(f"{yellow_color}STOCK:{reset_color}")
                                gotoxy(74,9);print(product['stock'])
                                gotoxy(50,25);print(f"{cyan_color}🫣 No se modificó Precio del producto. 🫣{reset_color}")
                                time.sleep(3)
                                self.update()
                        elif opc == "2":
                            borrarPantalla()
                            borrarPantalla()
                            gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
                            gotoxy(60,2);print(cyan_color+"ACTUALIZACION DE PRODUCTO"+reset_color)
                            gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
                            gotoxy(2,2);print(green_color+"██"+reset_color)
                            gotoxy(130,2);print(green_color+"██"+reset_color)
                            gotoxy(130,3);print(green_color+"██"+reset_color)
                            gotoxy(2,3);print(green_color+"██"+reset_color)
                            for i in range(4,30):
                                gotoxy(2,i);print(green_color+"██"+reset_color)
                                gotoxy(130,i);print(green_color+"██"+reset_color)
                            gotoxy(2,30);print(green_color+"██"*65+reset_color)    
                                
                            gotoxy(8,5);print(cyan_color+"Datos actuales del cliente:"+reset_color)
                            print("\n")
                            gotoxy(8,7);print(f"{yellow_color}ID:{reset_color}")
                            gotoxy(8,9);print(product['id'])
                            gotoxy(30,7);print(f"{yellow_color}DESCRIPCION:{reset_color}")
                            gotoxy(30,9);print(product['descripcion'])
                            gotoxy(52,7);print(f"{yellow_color}PRECIO:{reset_color}")
                            gotoxy(52,9);print(product['precio'])
                            gotoxy(74,7);print(f"{yellow_color}STOCK:{reset_color}")
                            gotoxy(74,9);print(product['stock'])
                            gotoxy(50,25);update_choice = input(f"{red_color}¿Desea modificar el Stock? (s/n): {reset_color}").lower()
                            borrarPantalla()
                            if update_choice == "s":
                                borrarPantalla()
                                gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
                                gotoxy(60,2);print(cyan_color+"ACTUALIZACION DE PRODUCTO"+reset_color)
                                gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
                                gotoxy(2,2);print(green_color+"██"+reset_color)
                                gotoxy(130,2);print(green_color+"██"+reset_color)
                                gotoxy(130,3);print(green_color+"██"+reset_color)
                                gotoxy(2,3);print(green_color+"██"+reset_color)
                                for i in range(4,30):
                                    gotoxy(2,i);print(green_color+"██"+reset_color)
                                    gotoxy(130,i);print(green_color+"██"+reset_color)
                                gotoxy(2,30);print(green_color+"██"*65+reset_color)    
                                    
                                gotoxy(8,5);print(cyan_color+"Datos actuales del cliente:"+reset_color)
                                print("\n")
                                gotoxy(8,7);print(f"{yellow_color}ID:{reset_color}")
                                gotoxy(8,9);print(product['id'])
                                gotoxy(30,7);print(f"{yellow_color}DESCRIPCION:{reset_color}")
                                gotoxy(30,9);print(product['descripcion'])
                                gotoxy(52,7);print(f"{yellow_color}PRECIO:{reset_color}")
                                gotoxy(52,9);print(product['precio'])
                                gotoxy(74,7);print(f"{yellow_color}STOCK:{reset_color}")
                                gotoxy(74,9);print(" "*10)
                                new_stock = validar.solo_numeros("Error: número incompleto", 74, 9)
                                product['stock'] = int(new_stock)
                                json_file.update('stock', products[0]['stock'], product)
                                products_sorted = sorted(json_file.read(), key=lambda x: x['id'])
                                json_file.save(products_sorted)
                                gotoxy(50,25);print(cyan_color+"Stock actualizada correctamente."+reset_color)
                                time.sleep(3)
                                self.update()
                            else:
                                
                                borrarPantalla()
                                gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
                                gotoxy(60,2);print(cyan_color+"ACTUALIZACION DE PRODUCTO"+reset_color)
                                gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
                                gotoxy(2,2);print(green_color+"██"+reset_color)
                                gotoxy(130,2);print(green_color+"██"+reset_color)
                                gotoxy(130,3);print(green_color+"██"+reset_color)
                                gotoxy(2,3);print(green_color+"██"+reset_color)
                                for i in range(4,30):
                                    gotoxy(2,i);print(green_color+"██"+reset_color)
                                    gotoxy(130,i);print(green_color+"██"+reset_color)
                                gotoxy(2,30);print(green_color+"██"*65+reset_color)    
                                    
                                gotoxy(8,5);print(cyan_color+"Datos actuales del cliente:"+reset_color)
                                print("\n")
                                gotoxy(8,7);print(f"{yellow_color}ID:{reset_color}")
                                gotoxy(8,9);print(product['id'])
                                gotoxy(30,7);print(f"{yellow_color}DESCRIPCION:{reset_color}")
                                gotoxy(30,9);print(product['descripcion'])
                                gotoxy(52,7);print(f"{yellow_color}PRECIO:{reset_color}")
                                gotoxy(52,9);print(product['precio'])
                                gotoxy(74,7);print(f"{yellow_color}STOCK:{reset_color}")
                                gotoxy(74,9);print(product['stock'])
                                gotoxy(50,25);print(f"{cyan_color}🫣 No se modificó el Stock. 🫣{reset_color}")
                                time.sleep(3)
                                self.update()
                        elif opc == "3":
                            self.update()                   
                        else  :
                            gotoxy(50, 20)
                            print(yellow_color+"Opcion incorrecta "+reset_color)
                            for i in range(3, 0, -1):
                                gotoxy(50, 23);print(f"{green_color} Espere {i} segundos... {reset_color}", end="\r")
                                time.sleep(1)
                            self.update()
        else  :
            gotoxy(50, 20)
            print(yellow_color+"Opcion incorrecta "+reset_color)
            for i in range(3, 0, -1):
                gotoxy(50, 23);print(f"{green_color} Espere {i} segundos... {reset_color}", end="\r")
                time.sleep(1)
            self.update()                    
                

    def delete(self):
        json_file = JsonFile(path + '/archivos/products.json')
        existing_ids = [str(product["id"]) for product in json_file.read()]
        validar = Valida()
        print('\033c', end='')
        print('\033c', end='')
        gotoxy(25,8);print(cyan_color+"█"*35+reset_color)
        gotoxy(60,8);print(green_color+"█"*35+reset_color)
        for i in range(8,19):
            gotoxy(25,i);print(green_color+"██"+reset_color)
            gotoxy(95,i);print(green_color+"██"+reset_color)
        gotoxy(25,18);print(green_color+"█"*35+reset_color)
        gotoxy(60,18);print(cyan_color+"█"*35+reset_color)
        while True:
            gotoxy(48, 12); print(f"\033[33mIngrese el ID del producto: \033[0m")
            product_id = validar.id_existe(existing_ids, "Error: ID invalido o existente", 53, 13)
            product_id_str = str(product_id)
            product_id_int = int(product_id_str) if product_id_str.isdigit() else None

            json_file = JsonFile(path+'/archivos/products.json')  # Assuming the path to your products JSON file
            products = json_file.find("id", product_id_int)
            if not products:
                gotoxy(40, 15); print("\033[31mIngresa la ID correcta Por Favor!\033[0m")
                for i in range(5, 0, -1):
                    gotoxy(56, 16); print(f"\033[31mEspere {i} segundos...\033[0m", end="\r")
                    time.sleep(1)
                self.delete()
            if products:
                borrarPantalla()
                for product in products:
                    gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
                    gotoxy(60,2);print(red_color+"ELIMINACION DE CLIENTE"+reset_color)
                    gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
                    gotoxy(2,2);print(green_color+"██"+reset_color)
                    gotoxy(130,2);print(green_color+"██"+reset_color)
                    gotoxy(130,3);print(green_color+"██"+reset_color)
                    gotoxy(2,3);print(green_color+"██"+reset_color)
                    for i in range(4,30):
                        gotoxy(2,i);print(green_color+"██"+reset_color)
                        gotoxy(130,i);print(green_color+"██"+reset_color)
                    gotoxy(2,30);print(green_color+"██"*65+reset_color)    

                    gotoxy(8,5);print(cyan_color+"Datos actuales del Producto:"+reset_color)
                    print("\n")
                    gotoxy(8,7);print(f"{yellow_color}ID:{reset_color}")
                    gotoxy(8,9);print(product['id'])
                    gotoxy(30,7);print(f"{yellow_color}DESCRIPCION:{reset_color}")
                    gotoxy(30,9);print(product['descripcion'])
                    gotoxy(52,7);print(f"{yellow_color}PRECIO:{reset_color}")
                    gotoxy(52,9);print(product['precio'])
                    gotoxy(74,7);print(f"{yellow_color}STOCK:{reset_color}")
                    gotoxy(74,9);print(product['stock'])
                        
                    gotoxy(45,25);update_choice = input(f"{red_color}¿Estás seguro de eliminar este Cliente 😢? (s/n):{reset_color} ").lower()
                    while True:
                        if update_choice in ["s", "n"]:
                            break
                        else:
                            gotoxy(40, 15);print("Seleccione una opción válida.")
                    if update_choice == "s":
                        json_file.delete_by_id_or_dni('id', product_id)
                        gotoxy(45,27);print(f"{red_color}Cliente eliminado correctamente.{reset_color}")
                        time.sleep(3)
                        self.delete()
                    elif update_choice == "n":
                        gotoxy(45,27);print(f"{yellow_color}Gracias por no eliminar al cliente TQM❤️{reset_color}")
                        time.sleep(3)
                    else:
                        print("Seleccione una opción válida.")
            break       

    def consult(self):
        borrarPantalla()
        line = 10
        validar = Valida()
        json_file = JsonFile(path + '/archivos/products.json')
        existing_ids = [str(product["id"]) for product in json_file.read()] 
        gotoxy(2, 1); print(green_color + "▄▄" * 65 + reset_color)
        gotoxy(60, 2); print(yellow_color + "Consulta de Producto" + reset_color)
        gotoxy(2, 3); print(green_color + "▄▄" * 65 + reset_color)
        gotoxy(2, 2); print(green_color + "██" + reset_color)
        gotoxy(130, 2); print(green_color + "██" + reset_color)
        gotoxy(130, 3); print(green_color + "██" + reset_color)
        gotoxy(2, 3); print(green_color + "██" + reset_color)
        for i in range(4, 30):
            gotoxy(2, i); print(green_color + "██" + reset_color)
            gotoxy(130, i); print(green_color + "██" + reset_color)
        gotoxy(2, 30); print(green_color + "██" * 65 + reset_color) 
        gotoxy(8, 5); print(red_color + "Datos actuales del Producto:" + reset_color)
        print("\n") 
        gotoxy(7, 6); print("\033[33mIngrese el ID del producto: \033[0m")
        product_id = validar.id__producto(existing_ids, "Error: ID inválido o incompleto", 35, 6)
        gotoxy(35,6);print(" "*45)
        
        if product_id is None:
            products = json_file.read()
            borrarPantalla()
            gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
            gotoxy(60,2);print(yellow_color+"Consulta de cliente"+reset_color)
            gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
            gotoxy(2,2);print(green_color+"██"+reset_color)
            gotoxy(130,2);print(green_color+"██"+reset_color)
            gotoxy(130,3);print(green_color+"██"+reset_color)
            gotoxy(2,3);print(green_color+"██"+reset_color)
            for i in range(4,30):
                gotoxy(2,i);print(green_color+"██"+reset_color)
                gotoxy(130,i);print(green_color+"██"+reset_color)
            gotoxy(2,30);print(green_color+"██"*65+reset_color) 
            gotoxy(8,5);print(red_color+"Datos actuales del Producto:"+reset_color)
            print("\n")  
            gotoxy(12,7);print(f"{yellow_color}ID:{reset_color}")
            gotoxy(30,7);print(f"{yellow_color}DESCRIPCION:{reset_color}")
            gotoxy(62,7);print(f"{yellow_color}PRECIO:{reset_color}")
            gotoxy(85,7);print(f"{yellow_color}STOCK:{reset_color}")
            for product in products:
                gotoxy(12,line);print(product['id'])
                gotoxy(30,line);print(product['descripcion'])
                gotoxy(62,line);print(product['precio'])
                gotoxy(85,line);print(product['stock'])
                line += 2
        else:
            product_id_str = str(product_id)
            product_id_int = int(product_id_str) if product_id_str.isdigit() else None
            products = json_file.find("id", product_id_int)
            if products:
                products_info = products[0]  # Acceder al primer elemento de la lista
                borrarPantalla()
                gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
                gotoxy(60,2);print(yellow_color+"Consulta de Producto"+reset_color)
                gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
                gotoxy(2,2);print(green_color+"██"+reset_color)
                gotoxy(130,2);print(green_color+"██"+reset_color)
                gotoxy(130,3);print(green_color+"██"+reset_color)
                gotoxy(2,3);print(green_color+"██"+reset_color)
                for i in range(4,30):
                    gotoxy(2,i);print(green_color+"██"+reset_color)
                    gotoxy(130,i);print(green_color+"██"+reset_color)
                gotoxy(2,30);print(green_color+"██"*65+reset_color) 
                gotoxy(8,5);print(red_color+"Datos actuales del cliente:"+reset_color)
                print("\n")  

                gotoxy(12,7);print(f"{yellow_color}ID:{reset_color}")
                gotoxy(30,7);print(f"{yellow_color}DESCRIPCION:{reset_color}")
                gotoxy(62,7);print(f"{yellow_color}PRECIO:{reset_color}")
                gotoxy(85,7);print(f"{yellow_color}STOCK:{reset_color}")
                
                gotoxy(12,line);print(products_info['id'])
                gotoxy(30,line);print(products_info['descripcion'])
                gotoxy(62,line);print(products_info['precio'])
                gotoxy(85,line);print(products_info['stock'])

        gotoxy(45,4+line);x = input(f"{red_color}Presione una tecla para continuar...{reset_color}")



class CrudSales(ICrud):
    def create(self):
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"██"*65+reset_color)
        for i in range(2,11):
            gotoxy(2,i);print(green_color+"██"+reset_color)
            
            gotoxy(130,i);print(green_color+"██"+reset_color)
        gotoxy(2,30);print(green_color+"██"*65+reset_color)
        gotoxy(60,2);print(cyan_color+"Registro de Venta"+reset_color)
        gotoxy(45,3);print(yellow_color+Company.get_business_name()+reset_color)
        
        gotoxy(10,5);print(f"{cyan_color}Factura#:F0999999 {' '*3} {reset_color}")
        gotoxy(45,5);print(f"Fecha:{datetime.datetime.now()}")
        gotoxy(100,5);print(cyan_color+"Subtotal:"+reset_color)
        gotoxy(100,6);print(cyan_color+"Decuento:"+reset_color)
        gotoxy(100,7);print(cyan_color+"Iva     :"+reset_color)
        gotoxy(100,9);print(cyan_color+"Total   :"+reset_color)
        gotoxy(15,7);print(cyan_color+"Cedula:"+reset_color)
        dni=validar.solo_numeros("Error: Solo numeros",23,7)
        json_file = JsonFile(path+'/archivos/clients.json')
        client = json_file.find("dni",dni)
        if not client:
            gotoxy(35,6);print(f"{yellow_color}Cliente no existe{reset_color}")
            return
        client = client[0]
        cli = RegularClient(client["nombre"],client["apellido"], client["dni"], card=True)
        sale = Sale(cli)
        gotoxy(45,7);print(cli.fullName())
        gotoxy(4,11);print(green_color+"*"*127+reset_color)
        gotoxy(5,13);print(yellow_color+"Linea"+reset_color)
        gotoxy(18,13);print(yellow_color+"Id_Articulo"+reset_color)
        gotoxy(36,13);print(yellow_color+"Descripcion"+reset_color)
        gotoxy(54,13);print(yellow_color+"Precio"+reset_color)
        gotoxy(72,13);print(yellow_color+"Cantidad"+reset_color)
        gotoxy(90,13);print(yellow_color+"Subtotal"+reset_color)
        gotoxy(108,13);print(yellow_color+"n->Terminar Venta)"+reset_color)
        # detalle de la venta
        follow ="s"
        line=2
        contador = 1
        while follow.lower()=="s":
            gotoxy(7,13+line);print(contador)
            gotoxy(15,13+line)
            id=int(validar.solo_numeros("Error: Solo numeros",18,13+line))
            json_file = JsonFile(path+'/archivos/products.json')
            prods = json_file.find("id",id)
            if not prods:
                gotoxy(18,13+line);print("Producto no existe"),
                time.sleep(2)
                gotoxy(18,13+line);print(" "*25)

            else:
                prods = prods[0]
                product = Product(prods["id"],prods["descripcion"],prods["precio"],prods["stock"])
                gotoxy(36,13+line);print(product.descrip)
                gotoxy(54,13+line);print(product.preci)
                gotoxy(72,13+line);qyt=int(validar.solo_numeros("Error:Solo numeros",72,13+line))
                gotoxy(90,13+line);print(product.preci*qyt)
                sale.add_detail(product,qyt)
                gotoxy(112,9);print(round(sale.subtotal,2))
                gotoxy(112,5);print(round(sale.discount,2))
                gotoxy(112,6);print(round(sale.iva,2))
                gotoxy(112,7);print(round(sale.total,2))
                gotoxy(112,13+line);follow=input() or "s"
                gotoxy(112,13+line);print(green_color+"✔"+reset_color)
                gotoxy(2,14+line);print(green_color+"*"*130+reset_color)
                line += 2
                contador +=1

        gotoxy(45,14+line);print(red_color+"Esta seguro de grabar la venta(s/n):")
        gotoxy(82,14+line);procesar = input().lower()
        if procesar == "s":
            gotoxy(45,16+line);print("😊 Venta Grabada satisfactoriamente 😊"+reset_color)
            # print(sale.getJson())
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            ult_invoices = invoices[-1]["factura"]+1
            data = sale.getJson()
            data["factura"]=ult_invoices
            invoices.append(data)
            json_file = JsonFile(path+'/archivos/invoices.json')
            json_file.save(invoices)
        else:
            gotoxy(45,16+line);print("🤣 Venta Cancelada 🤣"+reset_color)
        time.sleep(2)


    def update(self):
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Editar Factura"+" "*38+"██" +reset_color)
        gotoxy(65,4);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(6,4);id_fact = int(input(purple_color+'Ingrese el numero de la factura: '+reset_color))
        json_file = JsonFile(path+'/archivos/invoices.json')       
        factura_a_modificar = json_file.find("factura", id_fact)
        
        fila = 10
        if id_fact == 0:
            gotoxy(15,8);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
        elif factura_a_modificar:
            gotoxy(65,4);print(' '*100)
            invoice = factura_a_modificar[0]  # Extrae la primera factura encontrada
            company = Company()
            gotoxy(6,4);print('-'*100)
            gotoxy(20,5);print(f'{cyan_color} Empresa: {reset_color} {company.business_name}')
            gotoxy(60,5);print(f'{cyan_color} Ruc: {reset_color} {company.ruc}')
            gotoxy(6,6);print('-'*100)
            gotoxy(10,7);new_id = input(f"{cyan_color} Factura: #{reset_color}") or invoice['factura']
            gotoxy(35,7);new_fecha = input(f"{cyan_color} Fecha: {reset_color}") or invoice['Fecha']
            gotoxy(60,7);new_client = input(f"{cyan_color} Cliente: {reset_color}") or invoice['cliente']
            gotoxy(6,8);print('-'*100)
            gotoxy(10,9);print(f"{cyan_color} Detalle: {reset_color}")
            
            fila = 10
            for detail in invoice['detalle']:
                gotoxy(20,fila);print(f'{cyan_color} Producto: {reset_color} {detail["producto"]}')
                gotoxy(20+30,fila);print(f'{cyan_color} Precio: {reset_color} {detail["precio"]}')
                gotoxy(20+55,fila);print(f'{cyan_color} Cantidad: {reset_color} {detail["cantidad"]}')
                fila += 1
                
            gotoxy(6,fila);print('-'*100)
            gotoxy(60,fila+1);new_subtotal = input(f"{cyan_color} Subtotal:  {reset_color}") or invoice['subtotal']      
            gotoxy(60,fila+2);new_descuento = input(f"{cyan_color} Descuento: {reset_color}") or invoice['descuento']     
            gotoxy(60,fila+3);new_iva = input(f"{cyan_color} IVA:       {reset_color}") or invoice['iva']    
            gotoxy(60,fila+4);new_total = input(f"{cyan_color} Total:     {reset_color}") or invoice['total']
            gotoxy(6,fila+5);print('-'*100)
                
            gotoxy(10, fila+7);print(red_color+"¿Está seguro de Modificar la factura? (s/n): "+reset_color)
            gotoxy(55, fila+7);procesar = input().lower()
            gotoxy(57, fila+7);print(red_color+"✔"+reset_color)

            if procesar == "s":
                new_values = {'factura': int(new_id), 'Fecha': new_fecha, 'cliente': new_client, 'subtotal': float(new_subtotal), 'descuento': float(new_descuento), 'iva': float(new_iva), 'total': float(new_total)}
                json_file.update('factura', id_fact, new_values)
                gotoxy(20,fila+9);print(yellow_color+"😊 Factura Modificada satisfactoriamente 😊"+reset_color)
            else:
                gotoxy(20,fila+9);print(yellow_color+"Modificación Cancelada!!"+reset_color)
                    
            time.sleep(2)  
            
        else: 
            gotoxy(65,4);print(' '*100)
            gotoxy(6,6);print(yellow_color+"Factura no existe!!"+reset_color)
            invoices = json_file.read()
            gotoxy(4,8);print('No. Facturas disponibles')
                        
            for fact in invoices:
                gotoxy(6,fila);print(blue_color+ str(fact['factura'])+reset_color)
                fila += 1
                        
            gotoxy(4,fila+2);x=input(red_color+"presione una tecla para continuar..."+reset_color)
            self.update()
    


    
    def delete(self):
        line = 2
        validar = Valida()
        json_file = JsonFile(path + '/archivos/invoices.json')
        existing_ids = [str(product["factura"]) for product in json_file.read()]
        print('\033c', end='')
        gotoxy(25,8);print(cyan_color+"█"*35+reset_color)
        gotoxy(60,8);print(green_color+"█"*35+reset_color)
        for i in range(8,19):
            gotoxy(25,i);print(green_color+"██"+reset_color)
            gotoxy(95,i);print(green_color+"██"+reset_color)
        gotoxy(25,18);print(green_color+"█"*35+reset_color)
        gotoxy(60,18);print(cyan_color+"█"*35+reset_color)
        while True:
            gotoxy(48, 12); print(f"\033[33mIngrese el Numero de Factura: \033[0m")
            factura = validar.id_existe(existing_ids, "Error: Factura invalido ", 53, 13)
            factura_id_str = str(factura)
            factura_id_int = int(factura_id_str) if factura_id_str.isdigit() else None

            json_file = JsonFile(path+'/archivos/invoices.json')  # Assuming the path to your products JSON file
            factura = json_file.find("factura", factura_id_int)
            if not factura:
                gotoxy(40, 15); print("\033[31mIngresa la ID correcta Por Favor!\033[0m")
                for i in range(5, 0, -1):
                    gotoxy(56, 16); print(f"\033[31mEspere {i} segundos...\033[0m", end="\r")
                    time.sleep(1)
                self.delete()
            if factura:
                borrarPantalla()
                for facturs in factura:
                    gotoxy(2,1);print(green_color+"▄▄"*65+reset_color)
                    gotoxy(60,2);print(red_color+"ELIMINACION DE FACTURA"+reset_color)
                    gotoxy(2,3);print(green_color+"▄▄"*65+reset_color)
                    gotoxy(2,2);print(green_color+"██"+reset_color)
                    gotoxy(130,2);print(green_color+"██"+reset_color)
                    gotoxy(130,3);print(green_color+"██"+reset_color)
                    gotoxy(2,3);print(green_color+"██"+reset_color)
                    for i in range(4,30):
                        gotoxy(2,i);print(green_color+"██"+reset_color)
                        gotoxy(130,i);print(green_color+"██"+reset_color)
                    gotoxy(2,30);print(green_color+"██"*65+reset_color)    

                    gotoxy(8,5);print(cyan_color+"Datos actuales del Producto:"+reset_color)
                    print("\n")
                    gotoxy(8,7);print(f"{yellow_color}Num. Factura:{reset_color}")
                    gotoxy(8,9);print(facturs['factura'])
                    gotoxy(30,7);print(f"{yellow_color}Fecha:{reset_color}")
                    gotoxy(30,9);print(facturs['Fecha'])
                    gotoxy(45,7);print(f"{yellow_color}Cliente:{reset_color}")
                    gotoxy(45,9);print(facturs['cliente'])
                    gotoxy(60,7);print(f"{yellow_color}Subtotal:{reset_color}")
                    gotoxy(60,9);print(facturs['subtotal'])
                    gotoxy(72,7);print(f"{yellow_color}Total:{reset_color}")
                    gotoxy(72,9);print(facturs['total'])
                    gotoxy(85,7);print(f"{yellow_color}Productos:{reset_color}")
                    gotoxy(100,7);print(f"{yellow_color}Precio:{reset_color}")
                    gotoxy(110,7);print(f"{yellow_color}Cantidad:{reset_color}")
                    for facturs in factura:
                        for detalle in facturs['detalle']:
                            gotoxy(85,7+line);print(detalle['poducto'])
                            gotoxy(100,7+line);print(detalle['precio'])
                            gotoxy(110,7+line);print(detalle['cantidad'])  
                            line+=2 
                    gotoxy(45,25);update_choice = input(f"{red_color}¿Estás seguro de eliminar este Cliente 😢? (s/n):{reset_color} ").lower()
                    while True:
                        if update_choice in ["s", "n"]:
                            break
                        else:
                            gotoxy(40, 15);print("Seleccione una opción válida.")
                    if update_choice == "s":
                        json_file.delete_by_id_or_dni('factura',  factura_id_int)
                        gotoxy(45,27);print(f"{red_color}Cliente eliminado correctamente.{reset_color}")
                        time.sleep(3)
                        self.delete()
                    elif update_choice == "n":
                        gotoxy(45,27);print(f"{yellow_color}Gracias por no eliminar al cliente TQM❤️{reset_color}")
                        time.sleep(3)
                    else:
                        print("Seleccione una opción válida.")
            break       
           

    def consult(self):        
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*102)
        gotoxy(2,2);print(f"*{' '*41}{cyan_color}CONSULTA DE VENTA{reset_color}{' '*42}{green_color}*{reset_color}")
        gotoxy(2,3);print(f"{green_color}*{'*'*100}*{reset_color}")  
        content_width = 100
        content_height = 25
        marco_lateral(content_width, content_height)
        marco_inferior(content_width, content_height)
        
        gotoxy(80,4);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(10,4);print(purple_color+"Ingrese el NO. de la Factura: "+reset_color)
        id_fact = validar.solo_numero("Error: Solo numeros",40,4)
        
        json_file = JsonFile(path+'/archivos/invoices.json')
        invoice = json_file.find("factura",id_fact)
        invoices = json_file.read()

        
        if id_fact == 0:
            gotoxy(15,8);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
        elif invoice:
            gotoxy(80,4);print(' '*21)
            gotoxy(3,29);print(' '*100) 
            gotoxy(2,5);print(f"{green_color}*{'*'*100}*{reset_color}")
            invoice = invoice[0]
            company = Company()
            gotoxy(3,6);print('-'*100)
            gotoxy(20,7);print(f'{cyan_color} Empresa: {reset_color} {white_color}{company.business_name}{reset_color}')
            gotoxy(60,7);print(f'{cyan_color} Ruc: {reset_color} {white_color}{company.ruc}{reset_color}')
            gotoxy(3,8);print('-'*100)
            gotoxy(10,9);print(f"{cyan_color} Factura: #{reset_color} {white_color}{invoice['factura']}{reset_color}")
            gotoxy(35,9);print(f"{cyan_color} Fecha: {reset_color} {white_color}{invoice['Fecha']}{reset_color}")
            gotoxy(60,9);print(f"{cyan_color} Cliente: {reset_color} {white_color}{invoice['cliente']}{reset_color}")
            gotoxy(3,10);print('-'*100)
            gotoxy(10,11);print(f"{purple_color}Detalle: {reset_color}")
            gotoxy(25,11);print(f"{cyan_color}Producto:{reset_color}")
            gotoxy(55,11);print(f"{cyan_color}Precio:{reset_color}")
            gotoxy(80,11);print(f"{cyan_color}Cantidad:{reset_color}")
                
            fila = 1
   
        for detail in invoice['detalle']:
            if 'producto' in detail:
                gotoxy(26,11+fila);print(f'{white_color}{detail["producto"]}{reset_color}')
            else:
                gotoxy(26,11+fila);print(f'{white_color}N/A{reset_color}')  # Otra acción si la clave 'producto' no existe
            if 'precio' in detail:
                gotoxy(56,11+fila);print(f'{white_color}{detail["precio"]}{reset_color}')
            else:
                gotoxy(56,11+fila);print(f'{white_color}N/A{reset_color}')  # Otra acción si la clave 'precio' no existe
            if 'cantidad' in detail:
                gotoxy(81,11+fila);print(f'{white_color}{detail["cantidad"]}{reset_color}')
            else:
                gotoxy(81,11+fila);print(f'{white_color}N/A{reset_color}')  # Otra acción si la clave 'cantidad' no existe
            fila += 1
                
            gotoxy(3,12+fila);print('-'*100)
            gotoxy(60,13+fila);print(f"{cyan_color} Subtotal:  {reset_color} {white_color}{invoice['subtotal']}{reset_color}")      
            gotoxy(60,14+fila);print(f"{cyan_color} Descuento: {reset_color} {white_color}{invoice['descuento']}{reset_color}")      
            gotoxy(60,15+fila);print(f"{cyan_color} IVA:       {reset_color} {white_color}{invoice['iva']}{reset_color}")      
            gotoxy(60,16+fila);print(f"{cyan_color} Total:     {reset_color} {white_color}{invoice['total']}{reset_color}")
            gotoxy(3,17+fila);print('-'*100)
            gotoxy(2,18+fila);print(f"{green_color}*{'*'*100}*{reset_color}")
            
            # Obtener el cliente de la factura consultada
            cliente_factura = invoice['cliente']
            mensaje(content_width+10, 20+fila, f'Facturas del cliente: {white_color}{cliente_factura}{reset_color}')
                
            total_fact_client = list(filter(lambda facturas_cliente: facturas_cliente['cliente'] == invoice['cliente'], invoices))
            suma = reduce(lambda total, invoice: round(total+ invoice["total"],2), total_fact_client,0)
            totales_map = list(map(lambda invoice: invoice["total"], total_fact_client))
            max_invoice = max(totales_map)
            min_invoice = min(totales_map)
            tot_invoices = sum(totales_map)
            
            gotoxy(3,21-fila);print('-'*100)
            gotoxy(33,fila+22);print(f'{cyan_color}NO.{reset_color}')
            gotoxy(50,fila+22);print(f'{cyan_color}Fecha{reset_color}')
            gotoxy(69,fila+22);print(f'{cyan_color}Total{reset_color}')
            gotoxy(3,21+fila);print('-'*100)
            
            for fac in total_fact_client:
                gotoxy(33,fila+23);print(f"{purple_color}{fac['factura']}")
                gotoxy(50,fila+23);print(f"{fac['Fecha']}")
                gotoxy(69,fila+23);print(f"{fac['total']}{reset_color}")
                fila += 1
            gotoxy(3,24+fila);print('-'*100)

            gotoxy(2,fila+25);print(f"{green_color}*{'*'*100}*{reset_color}")  
            gotoxy(5,fila+26);print(f"{cyan_color} map Facturas: {reset_color}{totales_map}")
            gotoxy(5,fila+28);print(f"{cyan_color} max Factura: {reset_color}{max_invoice}")
            gotoxy(5,fila+30);print(f"{cyan_color} min Factura: {reset_color}{min_invoice}")
            gotoxy(5,fila+32);print(f"{cyan_color} sum Factura: {reset_color}{tot_invoices}")
            gotoxy(5,fila+34);print(f"{cyan_color} reduce Facturas: {reset_color}{suma}")
            gotoxy(3,fila+35);print('-'*100)
            
            for i in range(content_height, fila+39):
                gotoxy(2,i);print(f"{green_color}*")
                gotoxy(103,i);print(f"{green_color}*")   
                         
            gotoxy(10,fila+37);x=input(red_color+"presione una tecla para continuar..."+reset_color) 

            marco_inferior(content_width, fila+40)
        else: 
            gotoxy(80,4);print(' '*21)  
            gotoxy(3,29);print(' '*100)             
            mensaje(content_width, 7, "Factura no existe!!")
            suma = reduce(lambda total, invoice: round(total+ invoice["total"],2), invoices,0)
            totales_map = list(map(lambda invoice: invoice["total"], invoices))

            max_invoice = max(totales_map)
            min_invoice = min(totales_map)
            tot_invoices = round(sum(totales_map), 2)
            
            gotoxy(3,9);print('-'*100)
            gotoxy(33,10);print(f'{cyan_color}NO.{reset_color}')
            gotoxy(50,10);print(f'{cyan_color}Fecha{reset_color}')
            gotoxy(69,10);print(f'{cyan_color}Total{reset_color}')
            gotoxy(3,11);print('-'*100)
            
            fila = 12
            for fac in invoices:
                gotoxy(33,fila);print(f"{purple_color}{fac['factura']}")
                gotoxy(50,fila);print(f"{fac['Fecha']}")
                gotoxy(69,fila);print(f"{fac['total']}{reset_color}")
                fila += 1
            
            gotoxy(2,fila+1);print(f"{green_color}*{'*'*100}*{reset_color}")  
            gotoxy(5,fila+3);print(f"{cyan_color} map Facturas: {reset_color}{totales_map}")
            gotoxy(5,fila+5);print(f"{cyan_color} max Factura: {reset_color}{max_invoice}")
            gotoxy(5,fila+7);print(f"{cyan_color} min Factura: {reset_color}{min_invoice}")
            gotoxy(5,fila+9);print(f"{cyan_color} sum Factura: {reset_color}{tot_invoices}")
            gotoxy(5,fila+11);print(f"{cyan_color} reduce Facturas: {reset_color}{suma}")
            gotoxy(3,fila+12);print('-'*100)
            
            for i in range(content_height, fila+17):
                gotoxy(2,i);print(f"{green_color}*")
                gotoxy(103,i);print(f"{green_color}*")
                
            marco_inferior(content_width, fila+12)
            
        gotoxy(20,fila+14);x=input(red_color+"presione una tecla para continuar..."+reset_color)
        


#Menu Proceso Principal
opc=''
while opc !='4':
    borrarPantalla()
    gotoxy(25,8);print(cyan_color+"█"*35+reset_color)
    gotoxy(60,8);print(green_color+"█"*35+reset_color)
    for i in range(8,19):
        gotoxy(25,i);print(green_color+"██"+reset_color)
        gotoxy(95,i);print(green_color+"██"+reset_color)
    menu_main = Menu("Menu Facturacion",["1) Clientes","2) Productos","3) Ventas","4) Salir"],50,10)
    gotoxy(25,18);print(green_color+"█"*35+reset_color)
    gotoxy(60,18);print(cyan_color+"█"*35+reset_color)
    opc = menu_main.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='5':
            borrarPantalla()
            gotoxy(25,8);print(cyan_color+"█"*35+reset_color)
            gotoxy(60,8);print(green_color+"█"*35+reset_color)
            for i in range(8,20):
                gotoxy(25,i);print(green_color+"██"+reset_color)
                gotoxy(95,i);print(green_color+"██"+reset_color)
            menu_clients = Menu("Menu Cientes",["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],50,10)
            gotoxy(25,19);print(green_color+"█"*35+reset_color)
            gotoxy(60,19);print(cyan_color+"█"*35+reset_color)
            opc1 = menu_clients.menu()
            sales = CrudClients()
            if opc1 == "1":
                sales.create()
            elif opc1 == "2":
                sales.update()
            elif opc1 == "3":
                sales.delete()
            elif opc1 == "4":
                sales.consult()
            print("Regresando al menu Clientes...")
            # time.sleep(2)
    elif opc == "2":
        opc2 = ''
        while opc2 !='5':
            borrarPantalla()
            gotoxy(25,8);print(cyan_color+"█"*35+reset_color)
            gotoxy(60,8);print(green_color+"█"*35+reset_color)
            for i in range(8,20):
                gotoxy(25,i);print(green_color+"██"+reset_color)
                gotoxy(95,i);print(green_color+"██"+reset_color)
            menu_products = Menu("Menu Productos",["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],50,10)
            gotoxy(25,19);print(green_color+"█"*35+reset_color)
            gotoxy(60,19);print(cyan_color+"█"*35+reset_color)
            opc2 = menu_products.menu()
            sales = CrudProducts()
            if opc2 == "1":
                sales.create()
            elif opc2 == "2":
                sales.update()
            elif opc2 == "3":
                sales.delete()
            elif opc2 == "4":
                sales.consult()
    elif opc == "3":
        opc3 =''
        while opc3 !='5':
            borrarPantalla()
            sales = CrudSales()
            gotoxy(25,8);print(cyan_color+"█"*35+reset_color)
            gotoxy(60,8);print(green_color+"█"*35+reset_color)
            for i in range(8,20):
                gotoxy(25,i);print(green_color+"██"+reset_color)
                gotoxy(95,i);print(green_color+"██"+reset_color)
            menu_sales = Menu("Menu Ventas",["1) Registro Venta","2) Consultar","3) Modificar","4) Eliminar","5) Salir"],50,10)
            gotoxy(25,19);print(green_color+"█"*35+reset_color)
            gotoxy(60,19);print(cyan_color+"█"*35+reset_color)
            opc3 = menu_sales.menu()
            if opc3 == "1":
                sales.create()

            elif opc3 == "2":
                sales.consult()
                time.sleep(2)
            elif opc3 == "3":
                sales.update()
            elif opc3 == "4":
                sales.delete()
            elif opc3 == "5":
                pass

    print("Regresando al menu Principal...")
    # time.sleep(2)

borrarPantalla()
input("Presione una tecla para salir...")
borrarPantalla()

