from clases1 import * 
import os
import time

menu=True
while menu==True:

    op=int(input('''Bienvenido al menu de registro de CLINICA NUTRICOL
            1.Ingresar paciente
            2.listar paciente
            3.Ingresar Medico
            4.listar Medico
            5. salir
            opcion: '''))
            
    if op ==1:
        print("ingrese los siguientes datos: ")
        nombre=(input("ingrese el nombre: "))
        sexo=(input("ingrese sexo: "))
        edad=int(input("ingrese edad : "))
        rut=(input("ingrese el RUT : "))
        peso=int(input("ingrese el peso del paciente : "))
        altura=float(input("ingrese altura del paciente : "))
        especialidad=(input("ingrese especialidad del medico asignado al paciente : "))
        fecha=(input("ingrese fecha de primera consulta: "))
        
        pacien = paciente(nombre,edad,rut,sexo,peso,altura,especialidad,fecha)
        
        pacien.apertura()
        pacien.escritura()
        pacien.cierre()   
        os.system("cls")

        menu2=True 
        while menu2 == True:
            op=int(input('''Eliga la accion a realizar:
            1.Calcular IMC
            2.Comprobar sexo.
            3.Comptobar edad.
            4.Salir
            opcion: '''))
            if op==1:
             pacien.calcular_IMC()
            elif op==2:
             pacien.comprobar_sex()
            elif op==3:
             pacien.Es_mayor() 
            elif op==4:
                menu2=False
                
    elif op ==2:
        print("listado de pacientes: ")
        pacien=paciente("","",0,"",0,0,"","")
        pacien.lectura()
        pacien.cierre()
        time.sleep(5)
        os.system("cls")
    
    elif op ==3:
        
        print("ingrese los siguientes datos: ")
        nombre=(input("ingrese el nombre del medico: "))
        sexo=(input("ingrese sexo: "))
        edad=int(input("ingrese edad medico : "))
        rut=(input("ingrese el RUT del medico: "))
        peso=(input("ingrese el peso medico: "))
        altura=(input("ingrese altura del medico: "))
        especialidad=(input("ingrese especialidad del medico : "))
        precio=int(input("ingrese el precio de la  consulta: "))
        

        pacien = medico(nombre,edad,rut,sexo,peso,altura,precio,especialidad)
        pacien.apertura()
        pacien.escritura()
        pacien.cierre()   
        os.system("cls")

           
    elif op ==4:
        print("listado de pacientes: ")
        pacien=medico("","",0,"",0,0,"","")
        pacien.lectura()
        pacien.cierre()
        time.sleep(5)
        os.system("cls")
        
    elif op==5:
        menu=False
        break