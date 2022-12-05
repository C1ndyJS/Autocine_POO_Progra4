class vehiculo:
    def __init__(self,marca,modelo,año):
        self.marca=marca
        self.modelo=modelo
        self.año=año

    def calcular_millas(self,a):
        self.kil=a*1,60934
    
    def apertura(self):
        self.archivo=open(r"Escritoriovehiculos.txt","a")   
    def escritura(self,lista):
       for obj in lista:
        self.archivo.write(f"\n Marca:{obj.marca}\n MODELO:{obj.modelo} \n AÑO:{obj.año} ")
    def cierre(self):
        self.archivo.close()
    def lectura(self):
        self.archivo=open(r"Escritoriovehiculos.txt","r")
        self.lectura=self.archivo.read()
        print(self.lectura)    

def buscar_en_lista(self,a):
    for obj in self:
        if obj.marca==a:
         print(obj.marca,obj.modelo,obj.año)

def listar(self):
    c=0
    for obj in self:
        c+=1
        print(c,"\n Marca:",obj.marca,"MODELO:",obj.modelo," AÑO:",obj.año)

def modificar_modelo(self,a,model):
    self[(a-1)].modelo=model

def modificar_año(self,a,año):
    self[(a-1)].año=año








