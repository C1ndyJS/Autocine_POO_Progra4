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
