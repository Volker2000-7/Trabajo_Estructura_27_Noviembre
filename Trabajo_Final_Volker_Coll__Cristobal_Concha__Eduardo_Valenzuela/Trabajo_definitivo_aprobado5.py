listaClientes="listaCliente.csv"
listaBuses="listaBuses.csv"
listaViajes="listaViajes.csv"
listaCiudades="listaCiudades.csv"
listaPasajes="listaPasajes.csv"
ENCODE="UTF-8"

import datetime
import os
import csv

from colorama import Fore, Style , init 

init(autoreset=True)

#CLASE CLIENTE QUE FUNCIONA COMO NODO
class Cliente:
    def __init__(self,idCliente:int,rut:int,nombre:str,apellido_paterno:str,apellido_materno:str,fono:int):
        self.idCliente=idCliente
        self.rut=rut
        self.nombre=nombre
        self.apellido_paterno=apellido_paterno
        self.apellido_materno=apellido_materno
        self.fono=fono
        self.siguiente=None

#CLASE BUS QUE FUNCIONA COMO NODO
class Bus:
    def __init__(self,idBus:int,patente:str,capacidad:int,disponibilidad:bool):
        self.idBus=idBus
        self.patente=patente
        self.capacidad=capacidad
        self.disponibilidad=disponibilidad
        self.siguiente=None

#CLASE CIUDAD QUE FUNCIONA COMO NODO
class Ciudad:
    def __init__(self,id_ciudad:int,nombre:str,posicion:int):
        self.id_ciudad=id_ciudad
        self.nombre=nombre
        self.posicion=posicion
        self.siguiente=None

#CLASE VIAJE QUE FUNCIONA COMO NODO
class Viaje:
    def __init__(self,id_viaje,id_bus,origen,destino,fecha,hora):
        self.id_viaje=id_viaje
        self.id_bus=id_bus
        self.origen=origen
        self.destino=destino
        self.fecha=fecha
        self.hora=hora
        self.siguiente=None


class Pasaje:
    def __init__(self,id_pasaje,id_viaje,id_cliente,id_origen,id_destino,asiento,valor,estado):
        self.id_pasaje=id_pasaje
        self.id_viaje=id_viaje
        self.id_cliente=id_cliente
        self.id_origen=id_origen
        self.id_destino=id_destino
        self.asiento=asiento
        self.valor=valor
        self.estado=estado
        self.siguiente=None

#CLASE LISTA ENLAZADA QUE CONTIENE TODAS LAS FUNCIONES
class ListaEnlazada:
    def __init__(self):
        self.inicio=None

#FUNCION AGREGAR LOS NODOS A LAS LISTAS
    def agregar(self,nuevo):
        if self.inicio==None:
            self.inicio=nuevo
        else:
            actual=self.inicio
            while actual.siguiente!=None:
                actual=actual.siguiente
            actual.siguiente=nuevo

#FUNCION QUE MUESTRA LA LISTA DE CLIENTES
    def mostrarClientes(self):
        if self.inicio==None:
            raise Exception("LISTA VACIA")
        actual=self.inicio
        print("-----------------------")
        while actual!=None:
            print(f"ID: {actual.idCliente}")
            print(f"RUT: {actual.rut}")
            print(f"NOMBRE: {actual.nombre}")
            print(f"APELLIDO PATERNO: {actual.apellido_paterno}")
            print(f"APELLIDO MATERNO: {actual.apellido_materno}")
            print(f"FONO: {actual.fono}")
            print("-----------------------")
            actual=actual.siguiente

#FUNCION QUE BUSCA A UN CLIENTE SEGUN SU ID
    def buscarCliente(self,id:int):
        if self.inicio==None:
            raise Exception("LISTA VACIA")
        actual=self.inicio
        while(actual!=None):
            if(str(actual.idCliente)==str(id)):
                return actual
            actual=actual.siguiente
        raise Exception("CLIENTE NO ENCONTRADO")

#FUNCION QUE MUESTRA LA LISTA DE BUSES
    def mostrarBuses(self):
        if self.inicio==None:
            raise Exception("LISTA VACIA")
        actual=self.inicio
        print("-----------------------")
        while actual!=None:
            print(f"ID: {actual.idBus}")
            print(f"PATENTE: {actual.patente}")
            print(f"CAPACIDAD: {actual.capacidad}")
            print(f"ESTADO: {actual.disponibilidad}")
            print("-----------------------")
            actual=actual.siguiente

#FUNCION QUE BUSCA A UN BUS SEGUN SU ID
    def buscarBus(self,id:int)->Bus:
        if self.inicio==None:
            raise Exception("LISTA VACIA")
        actual=self.inicio
        while(actual!=None):
            if(actual.idBus==id):
                return actual
            actual=actual.siguiente
        raise Exception("BUS NO ENCONTRADO")

#FUNCION QUE MUESTRA LA LISTA DE CIUDADES
    def mostrarCiudades(self):
        if self.inicio==None:
            raise Exception("LISTA VACIA")
        actual=self.inicio
        print("-----------------------")
        while actual!=None:
            print(f"ID: {actual.id_ciudad}")
            print(f"CIUDAD: {actual.nombre}")
            print(f"POSICIÓN: {actual.posicion}")
            print("-----------------------")
            actual=actual.siguiente

    #FUNCION QUE MUESTRA LA LISTA DE CIUDADES
    def mostrarViajes(self):
        if self.inicio==None:
            raise Exception("LISTA VACIA")
        actual=self.inicio
        print("-----------------------")
        while actual!=None:
            print(f"ID VIAJE: {actual.id_viaje}")
            print(f"ID BUS: {actual.id_bus}")
            print(f"ORIGEN: {actual.origen}")
            print(f"DESTINO: {actual.destino}")
            print(f"FECHA: {actual.fecha}")
            print(f"HORA: {actual.hora}")
            print("-----------------------")
            actual=actual.siguiente
    def buscarViajes(self,id:int):
        if self.inicio==None:
            raise Exception("LISTA VACIA")
        actual=self.inicio
        while(actual!=None):
            if((actual.id_viaje)==(id)):
                return actual
            actual=actual.siguiente
        raise Exception("VIAJE NO ENCONTRADO")


#FUNCION QUE GUARDA A LOS CLIENTES DE LA LISTA EN UN ARCHIVO
def guardar_clientes(lista:ListaEnlazada):
    with open("ListaCliente.csv","w",encoding="utf-8") as archivo:
        archivo.write("idCliente,rut,nombre,apellido_paterno,apellido_materno,fono\n")
        actual=lista.inicio
        while actual!=None:
            archivo.write(
                f"{actual.idCliente},"
                f"{actual.rut},"
                f"{actual.nombre},"
                f"{actual.apellido_paterno},"
                f"{actual.apellido_materno},"
                f"{actual.fono}\n"
            )
            actual=actual.siguiente

#FUNCION QUE CARGA LOS CLIENTES DEL ARCHIVO A LA LISTA
def cargar_Clientes(lista:ListaEnlazada):
        try:
            with open(listaClientes, "r", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    nuevoCliente = Cliente(
                        int(fila["idCliente"]),
                        int(fila["rut"]),
                        fila["nombre"],
                        fila["apellido_paterno"],
                        fila["apellido_materno"],
                        int(fila["fono"])
                    )
                    lista.agregar(nuevoCliente)
        except FileNotFoundError:
            with open(listaClientes, "w", encoding="utf-8") as archivo:
                archivo.write("idCliente,rut,nombre,apellido_paterno,apellido_materno,fono\n")

#FUNCION QUE GUARDA A LOS BUSES DE LA LISTA EN UN ARCHIVO
def guardar_buses(lista:ListaEnlazada):
    with open("listaBuses.csv","w",encoding="utf-8") as archivo:
        archivo.write("idBus,patente,capacidad,disponibilidad\n")
        actual=lista.inicio
        while actual!=None:
            archivo.write(
                f"{actual.idBus},"
                f"{actual.patente},"
                f"{actual.capacidad},"
                f"{actual.disponibilidad}\n"
            )
            actual=actual.siguiente


#FUNCION QUE CARGA LOS BUSES DEL ARCHIVO A LA LISTA
def cargar_Bus(lista:ListaEnlazada):
        try:
            with open(listaBuses, "r", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    disp = fila["disponibilidad"] == "True"
                    nuevoBus = Bus(
                        int(fila["idBus"]),
                        fila["patente"],
                        int(fila["capacidad"]),
                        disp
                    )
                    lista.agregar(nuevoBus)
        except FileNotFoundError:
            with open(listaBuses, "w", encoding="utf-8") as archivo:
                archivo.write("idBus,patente,capacidad,disponibilidad\n")

#FUNCION QUE CARGA LAS CIUDADES DEL ARCHIVO A LA LISTA
def cargar_Ciudad(lista:ListaEnlazada):
    try:
        with open(listaCiudades, "r", encoding=ENCODE) as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                lista.agregar(Ciudad(int(fila["id_ciudad"]), fila["nombre"], int(fila["posicion"])))
    except FileNotFoundError:
        pass

    if lista.inicio is None:
        with open(listaCiudades, "w", encoding=ENCODE) as archivo:
            archivo.write("id_ciudad,nombre,posicion\n")
            archivo.write("0,Concepción,0\n1,Chillán,1\n2,Linares,2\n3,Talca,3\n4,Rancagua,4\n5,Santiago,5\n")
        cargar_Ciudad(lista)

#FUNCION QUE GUARDA A LOS VIAJES DE LA LISTA EN UN ARCHIVO
def guardar_viajes(lista:ListaEnlazada):
    with open("listaViajes.csv","w",encoding="utf-8") as archivo:
        archivo.write("id_viaje,id_bus,origen,destino,fecha,hora\n")
        actual=lista.inicio
        while actual!=None:
            archivo.write(
                f"{actual.id_viaje},"
                f"{actual.id_bus},"
                f"{actual.origen},"
                f"{actual.destino},"
                f"{actual.fecha},"
                f"{actual.hora}\n"
            )
            actual=actual.siguiente

#FUNCION QUE CARGA LOS VIAJES DEL ARCHIVO A LA LISTA
def cargar_viajes(lista:ListaEnlazada):
    try:
        with open(listaViajes, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                
                nuevoViaje = Viaje(
                    int(fila["id_viaje"]),
                    int(fila["id_bus"]),
                    str(fila["origen"]),
                    str(fila["destino"]),
                    fila["fecha"],
                    fila["hora"]
                    
                )
                lista.agregar(nuevoViaje)
    except FileNotFoundError:
        with open(listaViajes, "w", encoding="utf-8") as archivo:
            archivo.write("id_viaje,id_bus,origen,destino,fecha,hora\n")
            
def verificar_palabras(palabra:str)->bool: 
    limpiezita=palabra.strip()
    if len(limpiezita)>0 and limpiezita.replace(" ","").isalpha():
        return True 
    else: 
        return False 
#FUNCION QUE VERIFICA SI UN NUMERO ES VALIDO O NO
def verificar_numeros(numero:str)->bool:
    limpiezito=numero.strip()#le quito los espacios en blanco 
    if limpiezito.isdigit() and int(limpiezito)>0:#convierto el numero de str a int y verifico que sea mayor a 0 y la funcion isdigit() verifica si el numero sea realmente un numero y no una palabra
        return True 
    else:
        return False
#FUNCION QUE VALIDA LOS DATOS DEL CLIENTE
def validar_cliente()->list:
                idCliente=id_menu_1_2()
                client=1
                while client==1:
                    rut=input("Ingrese rut sin puntos ni guión: ").strip()
                    resultadocliente=verificar_numeros(rut)
                    if resultadocliente==True:
                        client=2
                    else:
                        print("Ingrese rut valido")
                client=1
                while client==1:    
                    nom=input("Ingrese nombre: ").strip().capitalize()
                    resultadocliente=verificar_palabras(nom)
                    if resultadocliente == True:
                        client=2
                    else:
                        print("Ingrese nombre válido")
                client=1
                while client==1:
                    apeP=input("Ingrese apellido paterno: ").strip().capitalize()
                    resultadocliente=verificar_palabras(apeP)
                    if resultadocliente == True:
                        client=2
                    else:
                        print("Ingrese apellido válido")
                client=1
                while client==1:
                    apeM=input("Ingrese apellido Materno: ").strip().capitalize()
                    resultadocliente=verificar_palabras(apeM)
                    if resultadocliente == True:
                        client=2
                    else:
                        print("Ingrese apellido válido")
                client=1
                while client==1:
                    fono=input("Ingrese numero de Contacto del Cliente: ").strip()
                    resultadocliente=verificar_numeros(fono)
                    if resultadocliente==True:
                        client=2
                    else:
                        print("Ingrese fono válido")
                cliente=[idCliente,rut,nom,apeP,apeM,fono]
                return cliente
#FUNCION QUE CALCULA LA TARIFA SEGUN LA DISTANCIA DE LAS CIUDADES
def calcular_tarifa(listaciudades:list,origen:str,destino:str,tarifa:int)->int:
    tarifabase=tarifa
    origenNUM=0
    destinoNUM=0
    if origen == destino:#si ambos son igual "imposible" le mandamos a que escriba la vaina denuevo
        return print("Ingrese origen y destino válidos")
    for a in listaciudades:#recorro la lista de ciudades hasta que encuentre el origen y el contador origenNUM me dice en que posicion estaba 
        origenNUM+=1
        if listaciudades[a]==origen:
           break    
    for a in listaciudades:#recorro la lista de ciudades hasta que encuentre el destino y el contador destinonNUM me dice en que posicion estaba 
        destinoNUM+=1
        if listaciudades[a]==destino:
            break
    resultado=origenNUM - destinoNUM #saco la distancia de ciudades para calcular la tarifa             
    if resultado<0:# si el resultado es negativo lo cambio a positivo
       resulPosit=resultado*-1
    else:
        resulPosit=resultado#segun el resultado se le realizará el calculo de su tarifa
        if resulPosit == 5:#distancia maxima
            tarifafinal=tarifabase
        elif resulPosit==4:
            tarifafinal= tarifabase - (tarifabase*0.1) # distancia maxima menos 1 , por lo que se aplica el 10% de descuento
        elif resulPosit==3:
            tarifafinal=tarifabase - (tarifabase*0.2)# distancia maxima menos 2 , por lo que se aplica el 20% descuento
        elif resulPosit==2:
            tarifafinal= tarifabase - (tarifabase*0.3) # distancia maxima menos 3, por lo que se aplica el 30% descuento 
        elif resulPosit==1:
            tarifafinal= tarifabase - (tarifabase*0.4)# distancia maxima menos 4 , por lo que se aplica el 40% descuento 
        return tarifafinal #regresa la tarifa que se debe aplicar al cliente segun el viaje que realizará
#FUNCION QUE VALIDA EL ID DEL CLIENTE PARA BUSCARLO
def id_menu_1_2()->int:
    while True:
        try:
            id=input("Ingrese el id del cliente a buscar:").strip()
            if not verificar_numeros(id):
                raise ValueError("El ID debe ser un número mayor a 0.")
            return int(id)
                
        except Exception as err:
            print("error: ",err)
#FUNCION QUE REGISTRA UN CLIENTE NUEVO
def registrar_cliente(Clientes:ListaEnlazada):
    registro=validar_cliente()
    nuevoCliente=Cliente(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5])
    actual=Clientes.inicio
    while actual is not None:
        if actual.idCliente == nuevoCliente.idCliente:
            print("El cliente ya existe")
            return
        actual = actual.siguiente
    Clientes.agregar(nuevoCliente)
    guardar_clientes(Clientes)
    return print("Cliente registrado exitosamente")
            
            
def registrar_bus(Buses: ListaEnlazada, idBus: int, patente: str, capacidad: int, disponibilidad: bool):
    try:
        if idBus <= 0:
            raise ValueError("El ID tiene que ser mayor a 0")
        if patente == "":
            raise ValueError("La patente no puede estar vacia")
        if capacidad <= 0:
            raise ValueError("La capacidad no puede ser negativa")

        actual = Buses.inicio
        while actual is not None:
            if actual.idBus == idBus:
                raise ValueError("Ya existe un bus con ese ID.")
            if actual.patente == patente:
                raise ValueError("Ya existe un bus con esa patente.")
            actual = actual.siguiente

        nuevoBus = Bus(idBus, patente, capacidad, disponibilidad)
        Buses.agregar(nuevoBus)
        guardar_buses(Buses)
        print("Bus registrado")
    except ValueError as error:
        print(f"Error: {error}")
def anularPasaje(Pasajes: ListaEnlazada, id_pasaje: int):
    try:
        actual = Pasajes.inicio
        while actual is not None:
            if actual.id_pasaje == id_pasaje:
                if actual.estado == "Anulado":
                    raise ValueError("El pasaje ya esta anulado.")
                actual.estado = "Anulado"
                guardar_pasajes(Pasajes)
                print("Pasaje anulado!!.")
                return
            actual = actual.siguiente
        raise ValueError("No existe ese pasaje.")
    except ValueError as error:
        print(f"Error: {error}")
def cargar_pasajes(lista: ListaEnlazada):
    try:
        with open("listaPasajes.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                nuevoPasaje = Pasaje(
                    int(fila["id_pasaje"]),
                    int(fila["id_viaje"]),
                    int(fila["id_cliente"]),
                    int(fila["id_origen"]),
                    int(fila["id_destino"]),
                    int(fila["asiento"]),
                    int(fila["valor"]),
                    fila["estado"]
                )
                lista.agregar(nuevoPasaje)
    except FileNotFoundError:
        with open("listaPasajes.csv", "w", encoding="utf-8") as archivo:
            archivo.write("id_pasaje,id_viaje,id_cliente,id_origen,id_destino,asiento,valor,estado\n")
            
def buscar_cliente(Clientes:ListaEnlazada):
    id=id_menu_1_2()
    buscado=Clientes.buscarCliente(id)
    print("-----------------------")
    print(f"ID: {buscado.idCliente}")
    print(f"RUT: {buscado.rut}")
    print(f"NOMBRE: {buscado.nombre}")
    print(f"APELLIDO PATERNO: {buscado.apellido_paterno}")
    print(f"APELLIDO MATERNO: {buscado.apellido_materno}")
    print(f"FONO: {buscado.fono}")
    print("-----------------------")
    
    
def opcion9(Clientes: ListaEnlazada,Buses: ListaEnlazada,Viajes: ListaEnlazada,Ciudades: ListaEnlazada,Pasajes: ListaEnlazada) -> None:
    while True:
        print(Fore.CYAN + Style.BRIGHT + "\n--- RF09: CONSULTAS Y REPORTES ---")
        print("1. Lista general de clientes, buses y viajes programados")
        print("2. Pasajes vigentes y anulados de un viaje + Recaudación vigente")
        print("0. menú principal")
        sub_op: str = input("Seleccione una opción: ").strip()
        if sub_op == "1":
            print(Fore.CYAN + Style.BRIGHT + "\n LISTADO DE CLIENTES ")
            try:
                Clientes.mostrarClientes()
            except Exception as e:
                print(Fore.YELLOW + f"Aviso Clientes: {e}")

            print(Fore.CYAN + Style.BRIGHT + "\n LISTA DE BUSES ")
            try:
                Buses.mostrarBuses()
            except Exception as e:
                print(Fore.YELLOW + f"Aviso Buses: {e}")

            print(Fore.CYAN + Style.BRIGHT + "\n LISTA DE VIAJES PROGRAMADOS ")
            try:
                Viajes.mostrarViajes()
            except Exception as e:
                print(Fore.YELLOW + f"Aviso Viajes: {e}")

        elif sub_op == "2":
            reporte_pasajes_y_recaudacion_viaje(Pasajes, Viajes, Clientes, Ciudades)
        elif sub_op == "0":
            break
        else:
            print(Fore.RED + "Opción inválida.")


    
def reporte_pasajes_y_recaudacion_viaje(Pasajes: ListaEnlazada,Viajes: ListaEnlazada,Clientes: ListaEnlazada,Ciudades: ListaEnlazada) -> None:
    try:
        Viajes.mostrarViajes()
        id_viaje=int(input(("Ingrese id del viaje a preguntar")))
        if id_viaje <= 0:
            raise ValueError("El ID del viaje debe ser mayor a 0.")
        
        viaje = Viajes.buscarViajes(id_viaje)
        origen = buscar_nombre_ciudad(viaje.origen)
        destino = buscar_nombre_ciudad(viaje.destino)

        print(Fore.CYAN + Style.BRIGHT + f"\n REPORTE DE PASAJES Y RECAUDACIÓN - VIAJE #{id_viaje} ({origen} -> {destino})")
        actual = Pasajes.inicio
        recaudacion_vigente = 0
        cont_vigentes = 0
        cont_anulados = 0

        while actual is not None:
            if actual.id_viaje == id_viaje:
                cliente= Clientes.buscarCliente(actual.id_cliente)
                nom_origen= buscar_nombre_ciudad(actual.id_origen)
                nom_destino = buscar_nombre_ciudad(actual.id_destino)

                if actual.estado == "Activo":
                    etiqueta = Fore.GREEN + "[VIGENTE]"
                    recaudacion_vigente += actual.valor
                    cont_vigentes += 1
                else:
                    etiqueta = Fore.RED + "[ANULADO]"
                    cont_anulados += 1

                print(
                    f"{etiqueta}{Style.RESET_ALL} Pasaje #{actual.id_pasaje} | "
                    f"Asiento: {actual.asiento} | "
                    f"Pasajero: {cliente.nombre} {cliente.apellido_paterno} | "
                    f"Tramo: {nom_origen} -> {nom_destino} | "
                    f"Valor: ${actual.valor}"
                )
            actual = actual.siguiente

        if cont_vigentes == 0 and cont_anulados == 0:
            print(Fore.YELLOW + "Viaje aún no registra pasajes vendidos ni anulados.")
        else:
            print(Fore.CYAN + "-------------------------------------------------------------------------")
            print(f"Pasajes Vigentes: {Fore.GREEN}{cont_vigentes}{Style.RESET_ALL} | Pasajes Anulados: {Fore.RED}{cont_anulados}")
            print(Fore.GREEN + Style.BRIGHT + f"RECAUDACIÓN VIGENTE DEL VIAJE: ${recaudacion_vigente}")
            print(Fore.CYAN + "-------------------------------------------------------------------------")
    except Exception as error:
        print(Fore.RED + f"Error al generar reporte del viaje: {error}")

#ORDENAMIENTO POR QUICK SORT
def criterio_apellido(pasajero):
    cliente=pasajero[0]
    pasaje=pasajero[1]
    return(cliente.apellido_paterno.casefold(),cliente.apellido_materno.casefold(),cliente.nombre.casefold(),int(pasaje.asiento))

def criterio_nombres(pasajero):
    cliente=pasajero[0]
    pasaje=pasajero[1]
    return(cliente.nombre.casefold(),cliente.apellido_paterno.casefold(),cliente.apellido_materno.casefold(),int(pasaje.asiento))

def criterio_asiento(pasajero):
    cliente=pasajero[0]
    pasaje=pasajero[1]
    return(int(pasaje.asiento),cliente.apellido_paterno.casefold(),cliente.apellido_materno.casefold(),cliente.nombre.casefold())

def quick_sort(lista,inicio,fin,criterio):
    if inicio<fin:
        pivote=particionar(lista,inicio,fin,criterio)
        quick_sort(lista,inicio,pivote-1,criterio)
        quick_sort(lista,pivote+1,fin,criterio)

def particionar(lista,inicio,fin,criterio):
    pivote=lista[fin]
    i=inicio-1
    for j in range(inicio,fin):
        if criterio(lista[j])<=criterio(pivote):
            i+=1
            lista[i],lista[j]=lista[j],lista[i]
    lista[i+1],lista[fin]=lista[fin],lista[i+1]
    return i+1
    
def buscar_nombre_ciudad(id_ciudad):
    actual=Ciudades.inicio
    while(actual!=None):
        if str(actual.id_ciudad)==str(id_ciudad):
            return actual.nombre
        actual=actual.siguiente
    return "CIUDAD FUERA DE LIMITES"
#FUNCION QUE CARGA LOS PASAJES DEL ARCHIVO A LA LISTA
def cargar_pasajes(lista:ListaEnlazada):
    try:
        with open(listaPasajes, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                nuevoPasaje = Pasaje(
                    int(fila["id_pasaje"]),
                    int(fila["id_viaje"]),
                    int(fila["id_cliente"]),
                    int(fila["id_origen"]),
                    int(fila["id_destino"]),
                    int(fila["asiento"]),
                    int(fila["valor"]),
                    fila["estado"]
                )
                lista.agregar(nuevoPasaje)
    except FileNotFoundError:
        with open(listaPasajes, "w", encoding="utf-8") as archivo:
            archivo.write("id_pasaje,id_viaje,id_cliente,id_origen,id_destino,asiento,valor,estado\n")

#FUNCION QUE GUARDA A LOS PASAJES DE LA LISTA EN UN ARCHIVO
def guardar_pasajes(lista:ListaEnlazada):
    with open("listaPasajes.csv","w",encoding="utf-8") as archivo:
        archivo.write("id_pasaje,id_viaje,id_cliente,id_origen,id_destino,asiento,valor,estado\n")
        actual=lista.inicio
        while actual!=None:
            archivo.write(
                f"{actual.id_pasaje},"
                f"{actual.id_viaje},"
                f"{actual.id_cliente},"
                f"{actual.id_origen},"
                f"{actual.id_destino},"
                f"{actual.asiento},"
                f"{actual.valor},"
                f"{actual.estado}\n"
            )
            actual=actual.siguiente

#FUNCION QUE OBTIENE LOS TRAMOS DEL VIAJE
def obtener_tramos(origen:int,destino:int)->list:
    if origen<destino:
        return list(range(origen,destino))
    elif origen>destino:
        return list(range(origen,destino,-1))
    else:
        return []

#FUNCION QUE CALCULA EL VALOR DEL VIAJE
def calcular_valor(origen, destino,tarifa):
    precio_base=tarifa
    tramos_totales=5
    tramos_utilizados=len(obtener_tramos(origen, destino))
    tramos_no_utilizados=tramos_totales - tramos_utilizados
    descuento=precio_base*0.10*tramos_no_utilizados
    return int(precio_base-descuento)

#COMPRUEBA LOS TRAMOS DE LOS PASAJES
def comprobar_tramos(origen1,destino1,origen2,destino2):
    tramos1=set(obtener_tramos(origen1, destino1))
    tramos2=set(obtener_tramos(origen2, destino2))
    return bool(tramos1 & tramos2)

#FUNCION QUE REVISA SI EL ASIENTO ESTA DISPONIBLE
def asiento_disponible(inicio,id_viaje,asiento,origen,destino):
    actual=inicio
    while actual!=None:
        if (actual.id_viaje==id_viaje
            and actual.asiento==asiento
            and actual.estado=="Activo"):
            if comprobar_tramos(origen,destino,actual.id_origen,actual.id_destino):
                return False
        actual = actual.siguiente
    return True
#INICIO DEL MAIN

Clientes=ListaEnlazada()
cargar_Clientes(Clientes)
Buses=ListaEnlazada()
cargar_Bus(Buses)
Ciudades=ListaEnlazada()
cargar_Ciudad(Ciudades)
Viajes=ListaEnlazada()
cargar_viajes(Viajes)
Pasajes=ListaEnlazada()
cargar_pasajes(Pasajes)
while True:
    
    print("1. RF01: Registrar, listar y buscar clientes")
    print("2. RF02: Registrar, listar y consultar buses")
    print("3. RF03: Consultar el catálogo persistente de las seis ciudades y sus posiciones")
    print("4. RF04: Programar y consultar viajes")
    print("5. RF05: Ventas de pasajes")
    print("6. RF06: Anulación de pasajes")
    print("7. RF07: Seleccionar un viaje y mostrar todos sus pasajes vigentes")
    print("8. RF08: Consultas y reportes")
    op=input("Ingrese la opcion deseada: ")

    #OPCION 1 CLIENTES
    if op=="1": #REGISTRAR, LISTAR Y BUSCAR CLIENTES
        while True:
            print("1. Registrar Cliente")
            print("2. Listar Clientes")
            print("3. Buscar Cliente")
            print("4. Volver al menú principal")
            op2=input("Ingrese la opcion deseada: ")
            #REGISTRAR CLIENTE
            if op2=="1":
                
               registrar_cliente(Clientes)
                
            #LISTAR CLIENTES
            elif op2=="2":
                try:
                    Clientes.mostrarClientes()
                except Exception as err:
                    print(Fore.RED + f"Error: {err}")
            #BUSCAR CLIENTE
            elif op2=="3":
                try: 
                    buscar_cliente(Clientes)
                except Exception as err:
                    print(Fore.RED + f"Error: {err}")

            elif op2=="4":
                break
            else:
                print(Fore.RED + "Opcion no valida")
    #OPCION 2 BUSES
    elif op=="2":
        while True:
            #idBus:int,patente:str,capacidad:int,disponibilidad:bool
            print("1. Registrar Bus")
            print("2. Listar Buses")
            print("3. Buscar Bus")
            print("4. Volver al menú principal")
            op2=input("Ingrese la opcion deseada: ")
                #REGISTRAR BUS
            if op2=="1":
                try:
                    id=int(input("Ingrese el id: "))
                    patente=input("Ingrese la patente: ").strip().upper()
                    capacidad=int(input("Ingrese la capacidad: "))
                    disp=input("Ingrese la disponibilidad (True/False): ").strip().capitalize()
                    if disp == "True":
                        disponible = True
                    elif disp == "False":
                        disponible = False
                    else:
                        raise ValueError("Debe escribir True o False.")
                    registrar_bus(Buses, id, patente, capacidad, disponible)
                except ValueError as err:
                    print(Fore.RED + f"Error: {err}")
            #MOSTRAR LISTA DE BUSES
            elif op2=="2":
                try:
                    Buses.mostrarBuses()
                except ValueError as err:
                    print(Fore.RED + f"Error: {err}")
                #BUSCAR BUS
            elif op2=="3":
                try:
                    id=int(input("Ingrese el id del cliente a buscar: "))
                    buscado=Buses.buscarBus(id)
                    print("-----------------------")
                    print(f"ID: {buscado.idBus}")
                    print(f"PATENTE: {buscado.patente}")
                    print(f"CAPACIDAD: {buscado.capacidad}")
                    print(f"ESTADO: {buscado.disponibilidad}")
                    print("-----------------------")
                except Exception as err:
                    print(Fore.RED + f"Error: {err}")
            elif op2=="4":
                break
            else:
                print(Fore.RED + "Opcion no valida")
    #OPCION 3 CATALOGO DE CIUDADES            
    elif op=="3":
        try:
            Ciudades.mostrarCiudades()
        except ValueError as err:
            print(Fore.RED + f"Error: {err}")
    #OPCION 4 PROGRAMAR Y CONSULTAR VIAJES    
    elif op=="4":
        while True:
            print("1. Programar viaje")
            print("2. Consultar Viajes")
            print("3. Volver al menú principal")
            op2=input("Ingrese la opcion deseada: ")
            #PROGRAMAR VIAJE
            if op2=="1":
                try:
                    
                    id_viaje=int(input("Ingrese el id del viaje: "))
                    #VALIDACIONES ID_VIAJE
                    if id_viaje <= 0:
                        raise ValueError("El ID debe ser mayor a 0.")
                    viajeactual = Viajes.inicio
                    while viajeactual is not None:
                        if viajeactual.id_viaje == id_viaje:
                            raise ValueError("Ya existe un viaje con ese ID.")
                        viajeactual = viajeactual.siguiente
                    id_bus=int(input("Ingrese el id del bus: ")) 
                    #VALIDACIONES PARA EL ID_BUS
                    if id_bus <= 0:
                        raise ValueError("El ID del bus debe ser mayor a 0.")
                    bus = Buses.buscarBus(id_bus)
                    if bus is None:
                        raise ValueError("No existe un bus con ese ID.")
                    Ciudades.mostrarCiudades()
                    origen=int(input("Ingrese el ID de la ciudad de origen: "))
                    if origen == "":
                        raise ValueError("El ID de la ciudad de origen no puede estar vacío.")
                    if origen < 0 or origen > 5:
                        raise ValueError("El ID de la ciudad de origen no existe")
                    
                    Ciudades.mostrarCiudades()
                    destino=int(input("Ingrese el ID de la ciudad de destino: "))
                    if destino == "":
                        raise ValueError("El ID de la ciudad de destino no puede estar vacío.")
                    if destino < 0 or destino > 5:
                        raise ValueError("El ID de la ciudad de destino no existe.")
                    
                    if origen == destino:
                        raise ValueError("El origen y el destino no pueden ser iguales.")
                    
                    fecha=input("Ingrese la fecha(DD/MM/AAAA): ").strip()
                    datetime.datetime.strptime(fecha, "%d/%m/%Y")
                    
                    hora=input("Ingrese la hora de salida(HH:MM): ").strip()
                    datetime.datetime.strptime(hora, "%H:%M")
                    
                    nuevoViaje=Viaje(id_viaje,id_bus,origen,destino,fecha,hora)
                    Viajes.agregar(nuevoViaje)
                    guardar_viajes(Viajes)

                    print(Fore.GREEN + "Viaje programado con exito!")
                    
                except Exception as e:
                    print(Fore.RED + f"Error: {e}")
            #CONSULTAR VIAJES
            elif op2=="2":
                try:
                    Viajes.mostrarViajes()
                except ValueError as err:
                    print(Fore.RED + f"Error: {err}")
            elif op2=="3":
                break
            else:
                print(Fore.RED + "Opcion no valida")
    #OPCION 5 VENTA DE PASAJES
    #id_pasaje,id_viaje,id_cliente,id_origen,id_destino,asiento,valor,estado
    elif op=="5":
        while True:
            try:
                
                        id_pasaje=int(input("Ingrese el id del pasaje: "))
                        if id_pasaje <= 0:
                            raise ValueError("El ID del pasaje debe ser mayor a 0.")
                        actual=Pasajes.inicio
                        while actual is not None:
                            if actual.id_pasaje == id_pasaje:
                                raise ValueError("Ya existe un pasaje con ese ID.")
                            actual = actual.siguiente
                            
                        id_viaje=int(input("Ingrese el id del viaje: "))
                        if id_viaje <= 0:
                            raise ValueError("El ID del viaje debe ser mayor a 0.")
                        encontrado=None
                        actual = Viajes.inicio
                        while actual is not None:
                                    if actual.id_viaje == id_viaje:
                                        encontrado=actual
                                        break

                                    actual = actual.siguiente
                        if encontrado is None:
                            raise ValueError("No existe un viaje con ese ID.")    
                            

                        id_cliente=int(input("Ingrese el id del cliente: "))
                        if id_cliente <= 0:
                            raise ValueError("El ID del cliente debe ser mayor a 0.")
                        cliente = Clientes.buscarCliente(id_cliente)
                        if cliente is None:
                            raise ValueError("No existe un cliente con ese ID.")
                        
                        Ciudades.mostrarCiudades()
                        id_origen=int(input("Ingrese el ID de la ciudad de origen: "))
                        if id_origen == "":
                            raise ValueError("El ID de la ciudad de origen no puede estar vacío.")
                        if id_origen < 0 or id_origen > 5:
                            raise ValueError("El ID de la ciudad de origen no existe")
                                        
                        Ciudades.mostrarCiudades()
                        id_destino=int(input("Ingrese el ID de la ciudad de destino: "))
                        if id_destino == "":
                            raise ValueError("El ID de la ciudad de destino no puede estar vacío.")
                        if id_destino < 0 or id_destino > 5:
                            raise ValueError("El ID de la ciudad de destino no existe.")
                                        
                        if id_origen == id_destino:
                            raise ValueError("El origen y el destino no pueden ser iguales.") 
                        
                        asiento=int(input("Ingrese el numero de asiento: "))
                        if not asiento_disponible(Pasajes.inicio, id_viaje, asiento, id_origen, id_destino):
                            raise ValueError("El asiento no está disponible para el tramo seleccionado.")
                        
                        #CALCULAR EL VALOR DEL PASAJE
                        valor=0
                        estado="Activo"
                        tarifabase=int(input("Ingrese la tarifa base: "))
                        if tarifabase <= 0:
                            raise ValueError("La tarifa base debe ser un valor positivo.")
                        if tarifabase == "":
                            raise ValueError("La tarifa base no puede estar vacía.")
                        
                        verificar=calcular_valor(id_origen,id_destino,tarifabase)
                        
                        nuevoPasaje=Pasaje(id_pasaje,id_viaje,id_cliente,id_origen,id_destino,asiento,verificar,estado)
                        Pasajes.agregar(nuevoPasaje)
                        guardar_pasajes(Pasajes)
                        print(Fore.GREEN + f"Nuevo pasaje registrado")
                        break
            except Exception as err:
                print(Fore.RED + f"Error: {err}")
            
        
       
        
    #OPCION 7 ANULACIÓN DE PASAJES
    elif op=="6":
        try:
            id_pasaje=int(input("Ingrese el id del pasaje a anular: "))
            anularPasaje(Pasajes,id_pasaje)
        except Exception as err:
            print(Fore.RED + f"Error: {err}")
    #OPCION 8 SELECCIONAR UN VIAJE Y MOSTAR TODOS SUS PASAJES VIGENTES
    elif op=="7":
        id_viaje=input("Ingrese el id del viaje: ")
        
        lista=[]
        actual=Pasajes.inicio
        while actual!=None:
            if str(actual.id_viaje)==str(id_viaje) and actual.estado=="Activo":
                cliente=Clientes.buscarCliente(actual.id_cliente)
                lista.append((cliente,actual))
            actual=actual.siguiente

        if len(lista)==0:
            print("Este viaje no tiene pasajeros vigentes.")
        else:
            print("Seleccione el ordenamiento:")
            print("1. Apellido paterno (A-Z)")
            print("2. Nombres (A-Z)")
            print("3. Numero de asiento (menor a mayor)")
            op=input("Seleccione una opcion: ")
            if op=="1":
                quick_sort(lista,0,len(lista)-1,criterio_apellido)
            elif op=="2":
                quick_sort(lista,0,len(lista)-1,criterio_nombres)
            elif op=="3":
                quick_sort(lista,0,len(lista)-1,criterio_asiento)
            else:
                print("Opcion no valida.")
                continue
            for pasajero in lista:
                cliente=pasajero[0]
                pasaje=pasajero[1]
                origen=buscar_nombre_ciudad(pasaje.id_origen)
                destino=buscar_nombre_ciudad(pasaje.id_destino)
                print("-----------------------")
                print(f"ASIENTO: {pasaje.asiento}")
                print(f"PASAJERO: {cliente.nombre} {cliente.apellido_paterno} {cliente.apellido_materno}")
                print(f"TRAMO: {origen}->{destino}")
                print("-----------------------")

    #OPCION 9 CONSULTAS Y REPORTES
    elif op=="8":
        opcion9(Clientes,Buses,Viajes,Ciudades,Pasajes)
        
    else:
        print(Fore.RED + "Opcion invalida")

