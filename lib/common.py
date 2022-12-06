class Persona:
    def __init__(self,id,name,edad=None,phone=None):
        """
        Build the basic Person class.
        id> required parameter
        name> required parameter
        """
        self.id = id
        self.name = name
        self.edad = edad
        self.phone = phone

    def getName(self):
        return self.name
    def getEdad(self):
        return self.edad
    def getId(self):
        return self.id
    def getPhone(self):
        return self.phone

    def setName(self, name):
        self.name = name

    def setEdad(self, Age):
        self.edad = Age

    def setId(self, id):
        self.id = id

    def setPhone(self,phone):
        self.phone = phone

    def showInfo(self): 
        print("Nombre:", self.name)
        print("ID:", self.id)
        print("Phone:", self.phone)
    

class Vendedor(Persona):
    """
    Build the basic Seller class.
        id> required parameter
        name> required parameter
    """
    def __init__(self,id,name,edad, phone):
        super().__init__(id,name,edad, phone)

class Automovil:
    def __init__(self,matricula, color, marca):
        self.matricula = matricula
        self.color = color
        self.marca = marca 
        self.passenger = None

    def showInfo(self):
        print("Matricula:{} \nColor:{} \nMarca:{}".format(self.matricula,self.color,self.marca))

    def setPassengers(self, lp):
        self.passenger = lp

    def getPassengers(self, lp):
        self.passenger = lp

class Movie:
    """
    Build the basic Movie class.
    """
    def __init__(self,nombre,genero,clasificacion_edad, duracion):
        self.nombre = nombre 
        self.genero = genero
        self.clasificacion_edad = clasificacion_edad
        self.duracion = duracion

    def getNombre(self):
        return self.nombre
    def getGenero(self):
        return self.genero
    def getClasificacion(self):
        return self.clasificacion_edad    
    def getDuracion(self):
        return self.duracion

    def setNombre(self):
        self.nombre = input("Ingrese el nombre de la pelicula: ")

    def setGenero(self):
        self.genero = input("Ingrese el genero de la pelicula: ")

    def setClasificacion(self):
        self.clasificacion_edad = input("Ingrese la edad recomendada de la pelicula: ")

    def setDuracion(self):
        self.duracion = input("Ingrese la duracion de la pelicula: ")

    def ShowInfo(self):
        print("==Informacion Pelicula==")
        print("Nombre: ", self.nombre)
        print("Genero: ", self.genero)#Genero
        print("Edad Permitida: ", self.clasificacion_edad)
        print("duracion: ", self.duracion)