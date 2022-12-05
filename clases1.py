class persona:
    def __init__(self,nombre,edad,rut,sexo,peso,altura):
        self.__nombre=nombre
        self.__edad=edad
        self.__rut=rut
        self.__sexo=sexo
        self.__peso=peso
        self.__altura=altura

    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_rut(self):
        return self.__rut
    def get_sexo(self):
        return self.__sexo        
    def get_peso(self):
        return self.__peso 
    def get_altura(self):
        return self.__altura     
    def set_nombre(self):
        self.__nombre=input("ingrese un valor:")    
    def set_edad(self):
        self.__edad=input("ingrese un valor:")    
    def set_rut(self):
        self.__rut=input("ingrese un valor:")
    def set_sexo(self):
        self.__sexo=input("ingrese un valor:")
    def set_peso(self):
        self.__peso=input("ingrese un valor:")    
    def set_altura(self):
        self.__altura=input("ingrese un valor:")       


class medico(persona):

    def __init__(self, nombre, edad, rut, sexo, peso, altura,precio,especialidad):
        super().__init__(nombre, edad, rut, sexo, peso, altura)   
        self.__precio=precio
        self.__especialidad=especialidad
    
    def get_precio(self):
        return self.__precio 
    def get_especialidad(self):
        return self.__especialidad  
    
    def set_precio(self):
        self.__precio=input("ingrese un valor:")    
    def set_especialidad(self):
        self.__especialidad=input("ingrese un valor:")
    
    def apertura(self):
        self.archivo=open(r"Escritoriomedicos.txt","a")   
    def escritura(self):
       self.archivo.write(f"\n nombre:{self.get_nombre()}\n edad:{self.get_edad()}\n sexo:{self.get_sexo()}\n rut:{self.get_rut()}\n peso:{self.get_peso()}\n altura:{self.get_altura()}\n especialidad medico:{self.get_esp()}\n Precio consulta:{self.get_precio()} ")
    def cierre(self):
        self.archivo.close()
    def lectura(self):
        self.archivo=open(r"Escritoriomedicos.txt","r")
        self.lectura=self.archivo.read()
        print(self.lectura)    


class paciente(persona):
    def __init__(self, nombre, edad, rut, sexo, peso, altura, especialidad,fecha):
        super().__init__(nombre, edad, rut, sexo, peso, altura)
        self.__fecha=fecha
        self.__especialidad=especialidad
        
    def get_fecha(self):
        return self.__fecha
    def set_fecha(self):
        self.__fecha=input("ingrese un valor:")  
    
    def get_esp(self):
        return self.__especialidad
    def set_esp(self):
        self.__especialidad=input("ingrese un valor:")    
       
    def calcular_IMC(self):
        cont=0
        imc=(self.get_peso())/((self.get_altura())*(self.get_altura()))
        if imc<18.5:
            cont=-1
        elif imc>=18.5 and imc<=24.9 :
            cont=0
        elif imc >24.9:
            cont=1
        print("Su estado de peso es: ",cont)

    def Es_mayor(self):
        es=False
        if self.get_edad() >=18:
            es=True
        if es==True:
           print("El paciente es mayor de edad")
        else:
           print("El paciente no es mayor de edad")


    def comprobar_sex(self):
        if self.get_sexo() in ( 'HFhf'):
           None
        else:
           self.__sexo= 'H'        
    
    def apertura(self):
        self.archivo=open(r"Escritoriopacientes.txt","a")   
    def escritura(self):
        self.archivo.write(f"\n nombre:{self.get_nombre()}\n edad:{self.get_edad()}\n sexo:{self.get_sexo()}\n rut:{self.get_rut()}\n peso:{self.get_peso()}\n altura:{self.get_altura()}\n especialidad medico:{self.get_esp()}\n Fecha primera consulta:{self.get_fecha()} ")
    def cierre(self):
        self.archivo.close()
    def lectura(self):
        self.archivo=open(r"Escritoriopacientes.txt","r")
        self.lectura=self.archivo.read()
        print(self.lectura)    
           

        
         





