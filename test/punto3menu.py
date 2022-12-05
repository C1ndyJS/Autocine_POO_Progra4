from Parcial2P3 import *

lista=[]
menu=True

while menu==True:
    op=int(input('''\nBienvenido al Banco _BWSC_
            1. Registrar Sucursal        2. Listar Sucursal 
            3. Registrar Empleado        4. Listar Empleados
            5. Registrar Clientes        6. Listar Clientes
            7. Registrar cuenta          8. Listar Cuentas Abiertas
            
            9.Registar Tarjeta Debito
            10. Eliminar algun registro
            opcion: '''))
    print("\n")
    if op ==1:
        print("====Crear Sucursal en la base de datos====\n")
        code = input("Ingrese el codigo de la sucursal:")
        name = input("Ingrese el nombre de la sucursal:")
        dir = input("Ingrese ladireccion de la sucursal:")
        tel = input("Ingrese el telefono de la sucursal:")
        suc = sucursal(code, name, dir, tel)
        suc.apertura() 
        suc.crear() #Escribir una nueva sucursal en el archivo 
        suc.showInfo()
        suc.cierre()
        #Lectura del archivo
        
    elif op == 2: #Listado Sucursales
        suc = sucursal(0,"", "", 0)
        suc.apertura()
        suc.lecturaFile()
        suc.cierre()

    elif op ==3:
        print("====Ingresar registro de Empleado====\n")
        codeS = input("Ingrese el codigo de la sucursal de trabajo:")
        name = input("Ingrese el nombre del empleado:")
        idE = input("Ingrese el ID del empleado:")
        edad = int(input("Ingrese la edad del empleado:"))
        cargo = int(input("Ingrese el cargo del empleado:"))
        ant = int(input("Ingrese el tiempo de antiguedad (meses)"))
        emp = empleado(codeS, name, idE, edad,  cargo, ant)
        emp.apertura()
        emp.showInfo()
        emp.crear()
        emp.cierre()
        #---
        #codeS, nameE, codeE, edad, cargo, ant,
    elif op == 4: #Listado Empleados
        emp = empleado(1, "", 0, 0,"", 0)        
        emp.apertura()
        emp.lecturaFile()
        emp.cierre()
        
    elif op == 5:
        codeSuc = input("====CLIENTE===\nCod Sucursal:")
        nameC = input("Ingrese el nombre del cliente:")
        codeC = input("Ingrese la ident. del cliente:")
        edadC = int(input("Ingrese la edad del cliente :"))
        custom = cliente(codeSuc, nameC, codeC, edadC)
        custom.apertura()
        custom.crear()
        custom.cierre()
        custom.showInfo()
        
    elif op == 6: #Listado Clientes
        custom = cliente(1,1,1,1)        
        custom.apertura()
        custom.lecturaFile()
        custom.cierre()
        
    elif op == 7:       
        numberAc = input("Ingrese el numero de la cuenta:")
        titular = input("Ingrese el nombre y/o titular de la cuenta:")
        codeC = int(input("Ingrese la id del titular de la cuenta :"))
        tipo = input("ingresa el tipo de cuenta (Ahorro/Corriente): ")
        account = cuenta(numberAc, titular, codeC, tipo)
        account.apertura()
        account.crear()
        account.cierre()
        account.showInfo()

    elif op == 8: #Listado Cuentas
        account = cuenta(0,0,0,0)
        account.apertura()
        account.lecturaFile()
        account.cierre()

    elif op == 9:
        
        titular = input("Ingrese el nombre y/o titular de la tarjeta(Como aparece registrado):")
        tipoT= input("Tipo de tarjeta(Debito/Credito):")
        numberTarj = int(input("Ingrese el numero de la tarjeta :"))
        idTitular = int(input("ingresa el numero de identificacion): "))
        tarj = tarjeta(tipoT, numberTarj, titular, idTitular)
        tarj.showInfo()
#--------------------

