
class Persona:
    def __init__(self,id,name,edad, phone):
        self.id = id
        self.name = name
        self.edad = edad
        self.phone = phone

    def GetName(self):
        return self.name
    def GetEdad(self):
        return self.edad
    def GetId(self):
        return self.id
    def GetPhone(self):
        return self.phone
    
    def SetName(self, name):
        self.name = name
        return self.name
    def SetEdad(self, Age):
        self.edad = Age
        return self.edad
    def SetId(self, id):
        self.id = id
        return self.id
    def SetPhone(self,phone):
        self.phone = phone
        return self.phone  

    def ShowInfo(self): 
        print("Nombre:", self.name)
        print("ID:", self.id)
        print("Phone:", self.phone)

    
#==========
class Vendedor(Persona):
    def __init__(self,id,name,edad, phone, dni_T):
        super().__init__(id,name,edad, phone)
        self.dni_T = dni_T
    
    def GetdniT(self):
        return self.dni_T
    def SetdniT(self):
        self.dni_T = input("Ingrese la id de trabajador:")
    
    def ShowInfo(self):
        print("Dni: ", self.dni_T)
        return super().ShowInfo()
#=============

c1 = Vendedor(100, "Pera", 30, 3123, 12345)
c2 = Persona(100, "Pepito", 32, 31983)
name = c1.GetName()
print(name)
class Cliente(Persona):
    def __init__(self,id,name,edad, phone, methodPayment, matricula):
        super().__init__(id,name,edad, phone)
        self.methodPayment = methodPayment
        self.matricula = matricula

    def GetMethodPayment(self):
        return self.methodPayment
    def GetMatricula(self):
        return self.matricula

    def SetMethodPayment(self):
        self.methodPayment = input("Ingrese el metodo de pago")
    def SetMatricula(self):
        self.matricula = input("Ingrese el numero de la matricula")    
    
    def ShowInfo(self):
        print("Informacion CLIENTE:")
        super().ShowInfo()
        print("Metodo Pago:", self.methodPayment)
        print("Matricula", self.matricula)
#==============
c3 = Cliente(100, "Pepito", 32, 12345, "Cash", "GTY234")
x = c3.GetName()
#print(x)

print("\n")
class Automovil(Cliente):
    def __init__(self,id,name, modelo, matricula, phone, methodPayment, edad = 0,):
        super().__init__(id, name, edad, phone, methodPayment, matricula)
        self.modelo = modelo 
        self.matricula = matricula

    def Getmodelo(self):
        return self.modelo        
    def GetMatricula(self):
        return super().GetMatricula()

    def ShowInfo(self):
        print("==Informacion Automovil==")
        print("Modelo", self.modelo)
        return super().ShowInfo()
        


auto = Automovil(101, "Juan",  2022, "GTY234", 312456, "Card")
aut = auto.GetName()
auto.ShowInfo()

# IDEAS Interfaces
# Un panel de opciones (Vender, Informacion) 
# Pantalla del auto cine Parqueadero(Solicitud del espacio donde pondre el carro)

class Movie:
    def __init__(self,nombre,genero,clasificacion_edad, duracion):
        self.nombre = nombre 
        self.genero = genero
        self.clasificacion_edad = clasificacion_edad
        self.duracion = duracion

    def GetNombre(self):
        return self.nombre
    def GetGenero(self):
        return self.genero
    def GetClasificacion(self):
        return self.clasificacion_edad    
    def GetDuracion(self):
        return self.duracion

    def SetNombre(self):
        self.nombre = input("Ingrese el nombre de la pelicula: ")
    def SetGenero(self):
        self.genero = input("Ingrese el genero de la pelicula: ")
    def GetClasificacion(self):
        self.clasificacion_edad = input("Ingrese la edad recomendada de la pelicula: ")    
    def GetDuracion(self):
        self.duracion = input("Ingrese la duracion de la pelicula: ")

    def ShowInfo(self):
        print("==Informacion Pelicula==")
        print("Nombre: ", self.nombre)
        print("Genero: ", self.genero)#Genero
        print("Edad Permitida: ", self.clasificacion_edad)
        print("duracion: ", self.duracion)

class Parqueadero(Movie):
    def __init__(self,id, tipo,cupo, name_Movie):
        self.id = id 
        self.name_Movie = name_Movie
        self.tipo=tipo
        self.cupo = cupo
        
    def GetCupo(self):
        return self.cupo 
        
    def setCupo(self, cupo):
        self.cupo = cupo
            
    def GetIdent(self):
        return self.id

    def Gettipo(self):
        return self.tipo

def TerminosCondiciones():
    a = 0
    return a    
 
#Términos y condiciones: el ingreso para 2 personas de 
#lunes a miércoles tiene un costo de 24.000 y de jueves a domingo
# de 36.000. Niños menores a 8 años pagan la mitad de la boleta'''
 