# -*- coding: utf-8 -*-
import os

"""agenda con un menu que guardara los datos en un archivo .csv"""

def agregar():
    nombre= input ("ingresa nombre")
    apellido= input ("ingresa apellido")
    celular= input ("ingresa celular")
    datos= nombre.title() + ";" + apellido.title()+ ";" + celular +"\n"
    archivo= open("contactos.csv","a+")
    archivo.write(datos)
    archivo.close()

def listar():
    if os.path.exists("./contactos.csv")== True:
        archivo = open("contactos.csv","r")
        for linea in archivo:
            fila= linea.split(";")
            print("{} {} {}".format(fila[0],fila[1],fila[2]))
        archivo.close()
    else:
        print:("ERROR: el archivo no existe")

def buscar(x):
    if os.path.exists("./contactos.csv")== True:
        archivo= open("contactos.csv","r")
        for linea in archivo:
            fila= linea.split(";")
            if fila[0] == x.title():
                print("{} {} {}".format(fila[0], fila[1], fila[2]))
                resultado= True
            elif fila[1] == x.title():
                print("{} {} {}".format(fila[0], fila[1], fila[2]))
                resultado= True
        if resultado== False:
                print("ERROR: el contacto no se ha podido encontrar")
        archivo.close()
    else:
        print("el archivo no existe")
        
    


def menu():
    while True:
        print("a) agregar un contacto ")
        print("b) buscar contacto ")
        print("c) listar contactos ")
        print("S)salir ")

        opcion=input ("ingresa una opcion")

        if opcion.lower()=="a":
           agregar()
        elif opcion.lower()=="b":
            busqueda= input("ingresa contacto")
            buscar(busqueda)
        elif opcion.lower()=="c":
            listar()
        elif opcion.lower()=="s":
            break

        else:
            print("{} es invalido ".format(opcion))

menu()
            
        
        



