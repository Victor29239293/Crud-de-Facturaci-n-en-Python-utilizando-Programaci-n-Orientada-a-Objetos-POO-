from utilities import borrarPantalla, gotoxy,white_color
import json





from time import sleep
import time
class Menu:
    def __init__(self,titulo="",opciones=[],col=6,fil=1):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
        
    def menu(self):
        gotoxy(self.col,self.fil);print(self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil +=1
            gotoxy(self.col,self.fil);print(opcion)
        gotoxy(self.col+5,self.fil+2)
        opc = input(f"Elija opcion[1...{len(self.opciones)}]: ") 
        return opc   

class Valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input()
            try:
                if float(valor) >= 0:
                    break
            except:
                gotoxy(col,fil);print(mensajeError)
                gotoxy(col,fil);print(" "*20)
                time.sleep(1)
                
        return valor
    def solo_numero(self, mensaje, col, fil):
        gotoxy(col, fil)
        valor = input(white_color)
        try:
            valor_entero = int(valor)
            if valor_entero == 0:
                return valor_entero
            elif valor_entero > 0:
                return valor_entero
            else:
                print("          ------><  | Error: Solo números positivos")
                time.sleep(1)
                return self.solo_numeros(mensaje, col, fil)
        except ValueError:
            print("          ------><  | Error: Solo números enteros")
            time.sleep(1)
            return self.solo_numero(mensaje, col, fil)
        
    def id_existe(self, existing_ids, error_msg, x, y):
        while True:
            gotoxy(x, y)
            id = input()
            if id.isdigit():  # Verificar si la entrada son solo dígitos
                id = int(id)
                if id in existing_ids:
                    gotoxy(x, y); print(error_msg)
                    time.sleep(1)
                    gotoxy(x,y);print(" "*35)
                else:
                    return id
            else:
                gotoxy(x, y); print(error_msg)
                time.sleep(1)
                gotoxy(x,y);print(" "*35)
    def nombre_existe(self, existing_names, error_msg, x, y):
        while True:
            gotoxy(x, y)
            nombre = input()
            if nombre in existing_names:
                gotoxy(x, y); print(error_msg)
                time.sleep(1)
                gotoxy(x,y);print(" "*45)
            else:
                return nombre
    def id__producto(self, existing_ids, error_message, col, fil):
        while True:
            gotoxy(col, fil)
            id = input()
            if id.strip() == '':
                return None  # Return None when input is empty to indicate retrieving all products
            try:
                id_int = int(id)
                if str(id_int) in existing_ids:
                    return id_int
                else:
                    gotoxy(col, fil);print(error_message)
                    time.sleep(1)
                    gotoxy(col,fil);print(" "*45)
            except ValueError:
                gotoxy(col, fil);print(error_message)    
                time.sleep(1)
                gotoxy(col,fil);print(" "*45)    
                
    def id_existe_producto(self, existing_names, error_msg, x, y):
        while True:
            gotoxy(x, y)
            id = int(input())
            if id in existing_names:
                gotoxy(x, y); print(error_msg)
                time.sleep(1)
                gotoxy(x,y);print(" "*45)
            else:
                return id

    def validate_input(prompt, condition, error_message):
        while True:
            user_input = input(prompt).strip()
            if condition(user_input):
                return user_input
            else:
                print("\033[91m\033[4m" + error_message + "\033[0m")
                time.sleep(2)            
    def solo_letras(self, mensajeError,col,fil):
        while True:
            gotoxy(col,fil)      
            valor = input()  # Usar f-string para formato
            if valor.isalpha():
                return valor  # Retornar el valor si solo contiene letras
            else:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*20)# Mostrar mensaje de error
                
    def validacion_telefono(self, mensajeError,col,fil):
        while True:
            gotoxy(col,fil)      
            valor = input()  # Usar f-string para formato
            if len(valor)== 10:
                return valor  # Retornar el valor si solo contiene letras
            else:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*35)
    
    
            
    def solo_decimales(self,mensaje,mensajeError):
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                print("          ------><  | {} ".format(mensajeError))
        return valor
   
    def validar_cedula(self, mensaje_error, col, fil):
        while True:
            gotoxy(col,fil) # Repetir hasta que se ingrese un DNI válido
            cedula = input()
            if not self.es_cedula_valida(cedula):
                gotoxy(col, fil)
                print(mensaje_error)
                time.sleep(1)
                gotoxy(col,fil);print(" "*35)
            else:
                return cedula  # Devolver el DNI válido y salir del bucle
    # Devuelve el DNI válido
    
    def validar_dni(self):
        while True: # Repetir hasta que se ingrese un DNI válido
            cedula = input()
            if not self.es_cedula_valida(cedula):
                return []
            else:
                return cedula
            
    def es_cedula_valida(self, cedula):
        # Asegurarse de que la cédula tenga exactamente 10 dígitos
        if len(cedula) != 10 or not cedula.isdigit():
            return False
        
        # Extraer los primeros 9 dígitos
        primeros_nueve = cedula[:-1]
        # Extraer el décimo dígito que es el dígito de verificación
        digito_verificacion = int(cedula[-1])

        # Multiplicadores alternos para el cálculo del dígito de verificación
        multiplicadores = [2, 1]  # alternancia 2, 1

        # Realizar la multiplicación alterna y ajustar resultados mayores que 9
        suma_total = 0
        for i, digito in enumerate(primeros_nueve):
            digito_int = int(digito)
            multiplicador = multiplicadores[i % 2]  # alternar entre 2 y 1
            resultado = digito_int * multiplicador
            
            if resultado > 9:
                resultado = resultado - 9
            
            suma_total += resultado

        digito_verificacion_esperado = (10 - (suma_total % 10)) % 10

        # Comparar el dígito calculado con el dígito de verificación
        return digito_verificacion_esperado == digito_verificacion
    

    
class otra:
    pass    

if __name__ == '__main__':
    # instanciar el menu
    opciones_menu = ["1. Entero", "2. Letra", "3. Decimal"]
    menu = Menu(titulo="-- Mi Menú --", opciones=opciones_menu, col=10, fil=5)
    # llamada al menu
    opcion_elegida = menu.menu()
    print("Opción escogida:", opcion_elegida)
    valida = Valida()
    if(opciones_menu==1):
      numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
      print("Número validado:", numero_validado)
    
    numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
    print("Número validado:", numero_validado)
    
    letra_validada = valida.solo_letras("Ingrese una letra:", "Mensaje de error")
    print("Letra validada:", letra_validada)
    
    decimal_validado = valida.solo_decimales("Ingrese un decimal:", "Mensaje de error")
    print("Decimal validado:", decimal_validado)