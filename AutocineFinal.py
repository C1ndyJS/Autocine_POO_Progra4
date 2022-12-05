from  tkinter import*
from tkinter import messagebox
import os 
img_dir = os.getcwd()

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

class Interfaz(Vendedor):
    def __init__(self, root, id,name,edad, phone, dni_T) -> None:
        super().__init__(id,name,edad, phone, dni_T)
        self.root = root
        self.firstWindow()

    def firstWindow(self):#Primera Pantalla
        self.root.title('Login')
        self.root.geometry('450x500')
        self.root.configure(bg ="#1F618D")
        self.root.resizable(False, False)

        self.imgUser = PhotoImage(file =f'{img_dir}/images/users.png')
        Label(self.root, image=self.imgUser, bg = '#1F618D').place(x=180, y=105)
        #Login 
        self.frameUs = Frame(self.root, width = 180, height= 20, bg ='white')
        self.frameUs.place(x=140, y = 235)

        self.user = Entry(self.frameUs, width=25, fg='black', border = 5, bg = 'white', font=('Microsoft YaHeu UI Light', 10))
        self.user.place(x = 1, y = 0)
        name = self.user.get()
        print(name)
        self.framepw = Frame(self.root, width = 180, height= 20, bg ='white')
        self.framepw.place(x=140, y = 285)

        self.password = Entry(self.framepw, show ='*', width=25, fg='black', border = 5, bg = 'white', font=('Microsoft YaHeu UI Light', 10))
        self.password.place(x = 1, y = 0)    
        
        botonLogin = Button(self.root, text = "Login", command=self.SecondWindow)
        botonLogin.place(x=210, y=320)
    
    def SecondWindow(self):
        self.ventanaLevel = Toplevel()
        self.ventanaLevel.title("Services Star")
        self.ventanaLevel.geometry("700x450")
        self.ventanaLevel.configure(bg = "white")
        self.ventanaLevel.resizable(False, False)
        self.correo = self.user.get()
        print(self.correo)
        self.Fila1 = Frame(self.ventanaLevel, width = 750, height= 55, bg ='black')
        self.Fila1.place(x=0, y=0)
        self.Columna = Frame(self.ventanaLevel, width = 550, height= 550, bg ='#2471A3')
        self.Columna.place(x=500, y=56)

        self.imgUser2 = PhotoImage(file =f'{img_dir}/images/users.png')
        Label(self.Columna, image = self.imgUser2, bg ='#2471A3').place(x=50, y=10)
        self.heading1 = Label(self.Columna, text ='___________', fg ='white', bg = '#2471A3', font=( "cursive",25, 'bold') )
        self.heading1.place(x=-2, y= 100)
        self.heading2 = Label(self.Columna, text ='___________', fg ='white', bg = '#2471A3', font=( "cursive",25, 'bold') )
        self.heading2.place(x=-2, y= 300)
        #Vendedor
        self.correo = Label(self.Columna, text =self.correo, fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold') )
        self.correo.place(x=50, y= 110) 
        self.Nombre = Label(self.Columna, text =f' Nombre:{self.name}', fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold') )
        self.Nombre.place(x=0, y= 150)        
        self.Iden = Label(self.Columna, text =f' Ident:{self.id}', fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold'))
        self.Iden.place(x=0, y= 170)
        self.Edad = Label(self.Columna, text =f' Edad:{self.edad} años', fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold') )
        self.Edad.place(x=0, y= 190)
        self.DNIT = Label(self.Columna, text =f' DniT:{self.dni_T}', fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold') )
        self.DNIT.place(x=0, y= 210)
        self.Phone = Label(self.Columna, text =f' phone:{self.phone} (Co)', fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold') )
        self.Phone.place(x=0, y= 230)
        
        self.botonLot = Button(self.ventanaLevel, text="Log out", width = 15, command=self.ventanaLevel.destroy)
        self.botonLot.place(x=30, y=15)

        self.botonActInfo = Button(self.ventanaLevel, text="Actualizar Informacion", width = 20, command=self.ventanaLevel.destroy)
        self.botonActInfo.place(x=520, y=15)

        self.opciones = Frame(self.ventanaLevel, width=500, height=500, bg="#85C1E9")
        self.opciones.place(x= 0, y = 56)
        
        self.botonRegistroBoleta = Button(self.opciones, text="Registrar \nCompra", width = 15, height="10", command=self.ventanaLevel.destroy)
        self.botonRegistroBoleta.place(x=65, y=100)

        self.botonInfoPeliculas = Button(self.opciones, text=f'Informacion\nMovies', width = 15, height ="10", command=self.ventanaLevel.destroy)
        self.botonInfoPeliculas.place(x =195, y=100)

        self.botonListarVentas = Button(self.opciones, text="Listar Venta", width = 15, height ="10", command=self.ventanaLevel.destroy)
        self.botonListarVentas.place(x = 325, y=100)

        self.heading = Label(self.opciones, text ='______________________________', fg ='white', bg = '#85C1E9', font=( "cursive",25, 'bold') )
        self.heading.place(x=0, y= 0)
        self.heading = Label(self.opciones, text ='Hola! Vive la experienca Star today!', fg ='white', bg = '#85C1E9', font=( "Ananda Black",15, 'bold') )
        self.heading.place(x=0, y= 8)
        
        self.fila2 = Frame(self.ventanaLevel, width = 700, height= 165, bg ='black')
        self.fila2.place(x=0, y=398)
#class InterfazVentas:

#=============

c1 = Vendedor(100, "Pera", 30, 3123, 12345)
c2 = Persona(100, "Pepito", 32, 31983)
name = c1.GetName()
#print(name)

#id,name,edad, phone, dni_T
obj = Interfaz(Tk(), 100, "Andres", 30, 3123, 12345)
nam = obj.GetName()
print(nam)
obj.root.mainloop()