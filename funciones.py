import os
import numpy as np


def llenarMatriz(matriz):
    cont=1
    for i in range(10):
        for j in range(4):
            matriz[i,j]=cont
            cont+=1
def valiMenu(): #funcion validacion ingreso menu
    op=0
    while(True):
        try:
            op=int(input(" Ingrese opción "))
            if(op>=1 and op<=5):
                break
            else:
                print("Debe ingresar una de las opciones")
        except ValueError:
            print("Debe ingresar un número entero")
    return op

def comprar():
    compra=0
    while(True):
        try:
            compra=int(input("Ingrere número de apartamento 1-40: "))
            if(compra>=1 and compra <=40):
                break
            else:
                print("Debe ingresar un asiento entre 1 y 40")
        except ValueError:
            print("Error.. ingrese apartamento entre 1 y 40")
    return compra
def buscarDisponbile(matriz,compra):
    for i in range(10):
        for j in range(4):
            if(compra==matriz[i,j]):
                return True
    return False
def comprarAp(matriz,compra,ruts):
    for i in range(10):
        for j in range(4):
            if(matriz[i,j]==compra):
                while(True):
                    try:
                        rut=int(input(" Ingrese rut 8 digitos minimo "))
                        if(rut<9999999):
                            print("Error, debe tener 8 digitos minimo")
                        else:
                            break
                    except ValueError:
                        print("Debe ingresar un número entero")
                ruts.append(rut)
                matriz[i,j]="X"
                if(i==0):
                    pago=3800
                if(i==1):
                    pago=3000
                if(i==2):
                    pago=2800
                if(i==3):
                    pago=3500
    return pago

def mostrarDisponibles(matriz):
    for i in range(10):
        print("\n")#salto de linea
        for j in range(4):
            if(j==1):
                print(matriz[i,j], end=" ")
            else:
                print(matriz[i,j], end=" ")
    print("\n\n")

def totalVenta(matriz):
    suma=0
    for i in range(10):
        for j in range(4):
            if(matriz[i,j]=="X"):
                if(i==0):
                    suma+=3800
                if(i==1):
                    suma+=3000
                if(i==2):
                    suma+=2800
                if(i==3):
                    suma+=3500
    return suma

def listado(r):
    r.sort()
    print("Listado de compradores ordenados de menor a mayor")
    print("\t",r)