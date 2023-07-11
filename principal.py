import os 
import numpy as np
import funciones as fn
matriz=np.empty([10,4], type(object))
fn.llenarMatriz(matriz)
ruts=[]
op=0
total=0
while(op!=5):
    os.system("cls")
    print("CASA FELIZ")
    print("")
    print("[1]Comprar apartamento")
    print("[2]Mostrar apartamento disponibles")
    print("[3]Ver listado de compradores")
    print("[4]Mostrar ganacias totales")
    print("[5]Salir")
    op=fn.valiMenu()
    if(op==1):#comprar
        l=1
        os.system("cls")
        compra=fn.comprar()
        comprueba=fn.buscarDisponbile(matriz,compra)
        if comprueba:
            os.system("cls")
            print("El apartamento esta disponible")
            venta=fn.comprarAp(matriz,compra,ruts)
            print(" Usted cancela: ",venta, "UF")
        else:
            print("El apartamento no esta disponible")
        os.system("pause")      
    if(op==2):
        os.system("cls")
        fn.mostrarDisponibles(matriz)
        os.system("pause")
    if(op==3):#listado de compradores
        if(l==1):
            os.system("cls")
            fn.listado(ruts)
            os.system("pause")
        else:
            print("Debe comprar antes de mostrar el listado de compradores")
            input("<<Enter>> para continuar")
    if(op==4):
        os.system("cls")
        suma=0
        suma=fn.totalVenta(matriz)
        if(suma==0):
            print("No hay apartamentos vendidos")
        else:
            print("El total de ganancias es: $",suma)
        os.system("pause")
    if(op==5):
        print("Adios! |Leo Gutierrez 11/07/2023")