#https://github.com/ClaudioMolina27/Prueba3.git
import csv
lista=[]
cont = 0
def categoria_equipo (a):
    if puntos_equipo >= 0 and puntos_equipo <= 40:
        categoria = "Amateur"
    if puntos_equipo >= 41 and puntos_equipo <= 80:
        categoria = "Principiante"
    if puntos_equipo >= 81 and puntos_equipo <= 120:
        categoria = "Avanzado"
    if puntos_equipo >= 121:
        categoria = "Idolos"
    return categoria
def validar_puntos (a):
    if a >= 0 and a <=150:
        return 1
    if a<0 or a>150:
        return 0

def validar_desicion():
    op=input("Esta seguro que desea realizar el cambio? (si/no)")
    if op == "si":
        return 1
    if op == "no":
        return 0
    else:
        print("Opcion no valida")

def puntaje_promedio():
    cont1 = 0
    acum = 0
    for u in lista:
        cont1 = cont1+1
        acum =acum+u[2]
    prom=acum/cont1
    return prom

def puntaje_mas_alto():
    gol=0
    for y in lista:
        g = y[2]
        if gol<g:
            gol = y[2]
    return gol

while True:
    try:
        print("=======================Menu=======================")
        print("")
        print("1.- Agregar equipo")
        print("2.- Lista equipo")
        print("3.- Actualizar nombre del equipo por  ID")
        print("4.- Generar BBDD")
        print("5.- Cargar BBDD")
        print("6.- Estadistias")
        print("0.- Salir")
        print("")
        menu=int(input("ingrese la opcion deseada: "))

        if menu ==1:
            print("")
            print("===================Agregar Equipo===================")
            print("")
            id_equipo=int(input("Ingrese el id del Equipo: "))
            nombre_equipo=input("Ingrese el nombre del Equipo: ")
            puntos_equipo= int(input("Ingrese los puntos del Equipo: "))
            while True:
                validacion = validar_puntos(puntos_equipo)
                if validacion == 1:
                    categoria=categoria_equipo(puntos_equipo)
                    break
                if validacion == 0:
                    puntos_equipo = int(input("Ingrese los puntos del Equipo nuevamente: "))
            lista_datos=[id_equipo,nombre_equipo,puntos_equipo,categoria]
            lista.append(lista_datos)
        elif menu ==2:
            print("")
            print("===================Listar Equipos===================")
            print("")
            for x in lista:
                print("ID del equipo:",x[0],"\nNombre del equipo:",x[1],"\nPuntos del equipo:",x[2],"\nCategoria del equipo:",x[3])
                print("---------------------------------------")
        elif menu ==3:
            print("")
            print("===================Actualizar Nombre Equipo===================")
            print("")
            cambio_id=int(input("Ingresa la id del equipo que desea cambiarle el nombre:"))
            for x in lista:
                if cambio_id== x[0]:
                    nuevo_nombre=input("Ingrese el nuevo nombre para el equipo: ")
                    valido=validar_desicion()
                    if valido == 1:
                        x[1]=nuevo_nombre
                    if valido == 0:
                        print("Volviendo al menu")
            print("")
        elif menu ==4:
            print("")
            print("===================Generando BBDD===================")
            print("")
            with open('BBDD_equipos.csv','w',newline='') as BBDD_equipos:
                escritor_csv = csv.writer(BBDD_equipos)
                escritor_csv.writerow((['ID','Nombre Equipo','Puntos','Categoria']))
                escritor_csv.writerows(lista)
                print("Archivo generado con exito :D")
            print("")
        elif menu ==5:
            print("")
            print("===================Cargando BBDD===================")
            print("")
            with open('BBDD_equipos.csv', 'r', newline='') as BBDD_equipos:
                lector_csv=csv.reader(BBDD_equipos)
                for x in lector_csv:
                    if cont == 0:
                        cont+=1
                        continue
                    i=int(x[0])
                    n=x[1]
                    p=int(x[2])
                    j=x[3]
                    listita=[i,n,p,j]
                    lista.append(listita)
                print("Archivo cargado con exito :D")
            print("")
        elif menu ==6:
            print("")
            print("===================Estadisticas===================")
            print("")
            promedio_por_equipo=puntaje_promedio()
            print("El puntaje promedio por equipo es de:",promedio_por_equipo)
            puntajealto=puntaje_mas_alto()
            print("El puntaje mas alto es de:", puntajealto)
            print("")
        elif menu ==0:
            print("Adios :D")
            break
        else:
            print("Error, ingrese opcion valida")
    except:
        print("==========================================")
        print("Error volviendo al principio")
