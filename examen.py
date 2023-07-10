import os 


#Aquí están las listas de los asientos 
ListaPlat1 = ['1' , '2', '3', '4', '5', '6', '7', '8', '9', '10']
ListaPlat2 = ["11","12","13","14","15","16","17","18","19","20"]
ListaGold1 = ["21","22","23","24","25","26","27","28","29","30"]
ListaGold2 = ["31","32","33","34","35","36","37","38","39","40"]
ListaGold3 = ["41","42","43","44","45","46","47","48","49","50"]
ListaSilver1 = ["51","52","53","54","55","56","57","58","59","60"]
ListaSilver2 = ["61","62","63","64","65","66","67","68","69","70"]
ListaSilver3 = ["71","72","73","74","75","76","77","78","79","80"]
ListaSilver4 = ["81","82","83","84","85","86","87","88","89","90"]
ListaSilver5 = ["91","92","93","94","95","96","97","98","99","100"]



ListaAsist = []
ListaRut = []



#este es el menú 

def mostrar_menu(): 
        
    print("""
               MENÚ 

    1). Comprar entradas 

    2). Mostrar Ubicaciones disponibles

    3). Ver listado de asistentes 

    4). Mostrar ganancias totales 

    5). Salir 
    
  
   """)
          
def ingresar_rut():
    try:
      rut = input("ingrese rut sin puntos, guion ni digito verificador: ")
      rut2 = len(rut)
      if rut2 == 8:
       ListaRut.append(rut)
      else:
          print("ingresa rut valido")
    except:
        print("Ingresa un rut valido")

        
#Aqui hago las funciones por cada opcion del menú

def numero_asiento():
    
    while True:
        try:
         Asiento = input("Elija numero de asiento:  ")
         if Asiento >= 1 and Asiento <=20:
            ValorPlat = 120000
         elif Asiento >= 21 and Asiento <=50:
            ValorGold = 80000
         elif Asiento >= 51 and Asiento <= 100:
            ValorSilv = 50000
            break
        except:
            print("Ha ocurrido una exepción")

        
    


def cant_entradas():

    while True:
        try:
            numero_entradas = input("Ingrese cuantas entradas quiere \n (Mín(1)/Max(3):")
            
            if numero_entradas == 1:
                ubi_disp()
                print("elija")

                           
            elif numero_entradas == 2:
                elegir_ubi()
               
            elif numero_entradas == 3:
                elegir_ubi()
            break
        except:
             print("ocurrió una exepción")
def elegir_ubi():
    ubi_disp()
    numero_asiento()

def ubi_disp():
    print("""
                                   ================================
                                   |                              |
                                   |         ESCENARIO            |
                                   |                              |
                                   ================================
     
    """)

    print("                        *************ASIENTOS************* ")
    print()
    print(f"PLATINUM FILA 1| {ListaPlat1}")
    print(f"PLATINUM FILA 2| {ListaPlat2}")
    print()
    print(f"GOLD FILA 1    | {ListaGold1}")
    print(f"GOLD FILA 2    | {ListaGold2}")
    print(f"GOLD FILA 3    | {ListaGold3}")
    print()
    print(f"SILVER FILA 1  | {ListaSilver1}")
    print(f"SILVER FILA 2  | {ListaSilver2}")
    print(f"SILVER FILA 3  | {ListaSilver3}")
    print(f"SILVER FILA 4  | {ListaSilver4}")
    print(f"SILVER FILA 5  | {ListaSilver5}")


def ver_listado():
    print(f"{ListaRut}")

def salir():
    print("Muchas gracias por usar el programa\n Solange Cea Gonzalez\n 10/07/2023")

def programa_main():
    while True:
        try:
            mostrar_menu() 
            opcion = int(input("ingresa una opcion:  ")) 
            if opcion == 1:
                os.system("cls") 
                cant_entradas() 
                input("presiona enter para continuar") 
            elif opcion == 2:
                os.system("cls") #aqui limpio la pantalla
                ubi_disp() 
                input("presiona enter para continuar") 
            elif opcion == 3:
                os.system("cls")
                ver_listado()
                input("presiona enter para continuar")
            elif opcion == 5:
                os.system("cls") 
                salir() 
                break 
            else:
                print("ingresaste una opcion incorrecta")
        except:
            print("debes ingresar un numero")

#ejecucion del programa
programa_main()