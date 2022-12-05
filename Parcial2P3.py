class sucursal: # Súper clase    
    def __init__(self, code, name, dir, tel ): 
        self.__code = code 
        self.__name = name 
        self.__dir = dir
        self.__tel = tel 
    #Creamos un archivo que almacene todos las sucursales 
    def getCode(self, codigo):
        self.__code = codigo
        return self.__code
    def setCode(self):  
        return self.__code

    def apertura(self):
        self.archivo=open(r"C:\Users\cmjim\OneDrive\Escritorio\Cindy\Parciales\sucursales.txt","a")
    def crear(self):
        self.archivo.write(f"code: {self.__code}, name: {self.__name}, direccion: {self.__dir}, telefono: {self.__tel}\n")
    
    def lecturaFile(self):
        self.archivo=open(r"C:\Users\cmjim\OneDrive\Escritorio\Cindy\Parciales\sucursales.txt","r+")
        self.lect = self.archivo.read()
        print("\nSucursales:\n", self.lect)
    
    def showInfo(self):#Lectura de la sucursal escrita en el objeto
        print("\n---Sucursal---\nName:",self.__name,"\ncode:",self.__code,"\ndireccion:",self.__dir,"\ntelefono:", self.__tel)
    def eliminar (self):
        print("")
    def cierre(self):
        self.archivo.close()
#Subclases
class empleado(sucursal):
    def __init__(self, codeS, nameE, codeE, edad, cargo, ant, nameS = "", dirS = "", telS = ""):
        sucursal.__init__(self, codeS, nameS, dirS, telS) #Info de la sucursal donde trabaja el empl
        self.__nameE = nameE
        self.__codeE = codeE
        self.__edad = edad
        self.__cargo = cargo
        self.__ant = ant        

    def apertura(self):
        self.archivo=open(r"C:\Users\cmjim\OneDrive\Escritorio\Cindy\Parciales\empleados.txt","a+")
    
    def crear(self): 
        self.archivo.write(f"Code_Sucursal: {super().setCode()}, DNI: {self.__codeE}, name: {self.__nameE} Edad: {self.__edad}, Cargo: {self.__cargo}, Antiguedad: {self.__ant}\n")
    
    def lecturaFile(self):
        self.archivo=open(r"C:\Users\cmjim\OneDrive\Escritorio\Cindy\Parciales\empleados.txt","r+")
        self.lect = self.archivo.read()
        print("\nEmpleados:\n", self.lect)
    def showInfo(self):#Lectura de la sucursal escrita en el objeto
        print('\n---Information---\nCode Sucursal:', super().setCode(), '\ncode Empleado:',self.__codeE,
        '\nName:',self.__nameE,'\nEdad:',self.__edad, '\nCargo:', self.__cargo,'\nAntiguedad:', self.__ant)
    def cierre(self): 
        self.archivo.close()

class cliente(sucursal):
    def __init__(self, code, nameC, codeC, edadC, nameS = " ", dirS=0, telS = 0):
        sucursal.__init__(self,code, nameS, dirS, telS) #Info de la sucursal donde trabaja el empl
        self.__nameC = nameC
        self.__codeC = codeC
        self.__edadC =  edadC

    def setnameC(self, nameC):
        self.__nameC = nameC
        return self.__nameC
    def getnameC(self):
        return self.__nameC
    def setCodeC(self, codeC):
        self.__codeC = codeC
        return self.__codeC
    def getCodeC(self):
        return self.__codeC
        
    def apertura(self):
        self.archivo=open(r"C:\Users\cmjim\OneDrive\Escritorio\Cindy\Parciales\Clientes.txt","a+")
    def crear(self): 
        self.archivo.write(f"Code_Sucursal: {super().setCode()}, DNI: {self.__codeC}, name: {self.__nameC} Edad: {self.__edadC}\n")
    def lecturaFile(self):
        self.archivo=open(r"C:\Users\cmjim\OneDrive\Escritorio\Cindy\Parciales\Clientes.txt","r+")
        self.lect = self.archivo.read()
        print("\nClientes:\n", self.lect)
    def showInfo(self):
        print('\n---Information---\nCode_sucursal:', super().setCode(), '\ncode :',self.__codeC,
            '\nName:',self.__nameC,'\nEdad:',self.__edadC,'\n')
    def cierre(self): 
        self.archivo.close()    
#ARCHIVO DE Cuentas abiertas en el banco
class cuenta(cliente): #Number de la cuenta, #Titular de la cuenta #NameC = Titular
    def __init__(self,  Number, titular, codeC,  tipo, codeS = 0, edadC = 0, nameS =" ", dirS=0, telS=0):
        super().__init__(codeS, titular, codeC, edadC, nameS, dirS, telS)
        self.__Number = Number
        self.__tipo = tipo #Ahorro o corriente 
    
    def getTitular(self):
        return super().getnameC()
    def getCodC(self):
        return super().getCodeC()

    def apertura(self):
        self.archivo=open(r"C:\Users\cmjim\OneDrive\Escritorio\Cindy\Parciales\Cuentas.txt","a+")
    def crear(self): 
        self.archivo.write(f"Num_cuenta: {self.__Number}, Titular: {super().getnameC()}, ID: {super().getCodeC()}, tipo: {self.__tipo}\n")
    def lecturaFile(self):
        self.archivo=open(r"C:\Users\cmjim\OneDrive\Escritorio\Cindy\Parciales\Cuentas.txt","r+")
        self.lect = self.archivo.read()
        print("\nCuentas:\n", self.lect)

    def showInfo(self):
        print('\n---Information---\n:ID', super().getCodeC(),'\nTitular :',super().getnameC(),'\nNumero de cuenta',self.__Number,
            '\ntipo de cuenta', self.__tipo,'\n')
    def cierre(self): 
        self.archivo.close()
#---
class tarjeta(cuenta):
    def __init__(self, tipoT, NumberT,  titularAccount, codeC, tipoCuenta = "", NumberAccount = 0, codeS=0, edadC=0, nameS=" ", dirS=0, telS=0):
        super().__init__(NumberAccount, titularAccount, codeC, tipoCuenta, codeS, edadC, nameS, dirS, telS)  
        self.__tipoT = tipoT #Credito o debito
        self.__numeroT = NumberT #Numero

    def showInfo(self):
        print('Informacion de la tarjeta:\nTitular de la cuenta:', super().getTitular(),
        '\nID', super().getCodC() ,'\nTipo:', self.__tipoT, '\nN° Tarjeta:', self.__numeroT)
#---
