from clases2 import *
import os
lista=[]
menu=True
while menu==True:

    op=int(input('''Bienvenido al gestor de vehiculos
            1.Nuevo Vehiculo
            2.listar Vehiculos
            3.Buscar Vehiclos
            4.Modificar Vehiculo
            5.Millas a kilometros
            6.Salir
            opcion: '''))
            
    if op ==1:
        print("ingrese los siguientes datos: ")
        marca=input("ingrese la marca del vehiculo: ")
        modelo=input("ingrese el modelo: ")
        año=int(input("ingrese la edad: "))
        carro = vehiculo(marca,modelo,año)
        lista.append(carro)   
    elif op ==2:
        listar(lista)
        
    elif op==3:
        a=input("ingrese la marca del vehiculo que desea buscar ")
        buscar_en_lista(lista,a)
        break
    elif op==4:
        menu2=True 
        while menu2 == True:
            listar(lista)
            a=int(input('''Que vehiculo desea modificar:'''))
            op2=int(input('''Que desea modificar
            1.Modelo
            2.Año
            3.Salir
            opcion: '''))
            if op2==1:
             modelo=input("ingrese nuevo modelo: ")                
             modificar_modelo(lista,a,modelo)
             
            elif op2==2:
             año=input("ingrese nuevo año: ")     
             modificar_año(lista,a,año)
             
            elif op2==3:
                menu2=False
    elif op==5:
        a=float(input("Ingrese numero de millas:"))
        carro=vehiculo("","",0)
        carro.calcular_millas(a)
    elif op==6:
        carro=vehiculo("","",0)
        carro.apertura()
        carro.escritura(lista)
        carro.cierre


