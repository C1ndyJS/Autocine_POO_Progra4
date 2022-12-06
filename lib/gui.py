from  tkinter import *
from lib.common import *
from lib.utils import *
import os 
img_dir = os.getcwd()

class Interfaz:
    def __init__(self, root) -> None:
        self.root = root
        self.firstWindow()

    def firstWindow(self):
        """firstWindow: 
          This creates the first initial window of the tkinter application
        """
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

        self.framepw = Frame(self.root, width = 180, height= 20, bg ='white')
        self.framepw.place(x=140, y = 285)

        self.password = Entry(self.framepw, show ='*', validate="key", width=25, fg='black', border = 5, bg = 'white', font=('Microsoft YaHeu UI Light', 10))
        self.password.place(x = 1, y = 0)    
        
        self.botonexit = Button(self.root, text="exit", width = 5, command=self.root.destroy) #good
        self.botonexit.place(x=400, y=475)
        
        botonLogin = Button(self.root, text = "Login", command=self.SecondWindow)
        botonLogin.place(x=210, y=320)
    
    def SecondWindow(self):
        self.root.iconify()
        self.ventanaLevel = Toplevel()
        self.ventanaLevel.title("Services Star:AutoCine")
        self.ventanaLevel.geometry("700x450")
        self.ventanaLevel.configure(bg = "white")
        self.ventanaLevel.resizable(False, False)

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
        v = Vendedor("1113123","Heticor")
        self.correo = Label(self.Columna, text =f'XXXX@XXX.co', fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold') )
        self.correo.place(x=50, y= 110) 
        self.Nombre = Label(self.Columna, text =f' Nombre:{v.getName()}', fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold') )
        self.Nombre.place(x=0, y= 150)        
        self.Iden = Label(self.Columna, text =f' Ident:{v.getId()}', fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold'))
        self.Iden.place(x=0, y= 170)
        self.Edad = Label(self.Columna, text =f' Edad:{v.getEdad()} años', fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold') )
        self.Edad.place(x=0, y= 190)
        self.Phone = Label(self.Columna, text =f' phone:{v.getPhone()} CO', fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold') )
        self.Phone.place(x=0, y= 230)
        
        self.botonLot = Button(self.ventanaLevel, text="Log out", width = 15, command=self.ventanaLevel.destroy) #good
        self.botonLot.place(x=30, y=15)

        self.botonActInfo = Button(self.ventanaLevel, text="Actualizar Informacion", width = 20, command=self.ventanaLevel.destroy)
        self.botonActInfo.place(x=520, y=15)

        self.opciones = Frame(self.ventanaLevel, width=500, height=500, bg="#85C1E9")
        self.opciones.place(x= 0, y = 56)
        
        self.botonRegistroBoleta = Button(self.opciones, text="Registrar\nBoleta", width = 15, height="10", command=self.reserves)
        self.botonRegistroBoleta.place(x=65, y=100)

        self.botonInfoPeliculas = Button(self.opciones, text=f'Informacion\nMovies', width = 15, height ="10", command=self.thirdWindow)
        self.botonInfoPeliculas.place(x =195, y=100)

        self.botonListarVentas = Button(self.opciones, text="Resume", width = 15, height ="10", command=self.reserves)
        self.botonListarVentas.place(x = 325, y=100)

        self.heading = Label(self.opciones, text ='______________________________', fg ='white', bg = '#85C1E9', font=( "cursive",25, 'bold') )
        self.heading.place(x=0, y= 0)
        self.heading = Label(self.opciones, text ='Hola! Vive la experienca Star today!', fg ='white', bg = '#85C1E9', font=( "Ananda Black",15, 'bold') )
        self.heading.place(x=0, y= 8)
        
        self.fila2 = Frame(self.ventanaLevel, width = 700, height= 165, bg ='black')
        self.fila2.place(x=0, y=398)
    
    def thirdWindow(self):
        self.cartelera = Toplevel()
        self.cartelera.title('Cartelera')
        self.cartelera.geometry('700x650')
        self.cartelera.configure(bg ="#154360")
        self.cartelera.resizable(False, False)
 
        self.sinopsismovie1 =' Título Original Black Panther: Wakanda Forever' 
        self.sinopsismov1 =' Director: Ryan Coogler.'
        self.sinopsismo1 ='País de Origen: United States of America '
        self.sinopsism1 ='Lenguaje: Inglés'

        self.sinopsismovie2 =' Título Original: Lyle, Lyle Crocodile' 
        self.sinopsismov2 ='País de Origen: United States of America.'
        self.sinopsismo2 ='Director: Tetsuro Kodama. '
        self.sinopsism2 ='Lenguaje: Inglés'
  
        self.fila1 = Frame(self.cartelera, width = 700, height= 65, bg ='black')
        self.fila1.place(x=0, y=0)
        self.headingC = Label(self.fila1, text = 'Cartelera', fg='white', bg = 'black', font=('cursive', 25, 'bold') )
        self.headingC.place(x=280, y=17)
        self.framemovie = Frame(self.cartelera, width= 200, height = 250, background='white')
        self.framemovie.place(x = 50, y = 100)

        self.sinopsis = Frame(self.cartelera, width= 360, height = 100, background='black')
        self.sinopsis.place(x = 280, y = 140 )

        self.head1 = Label(self.sinopsis, text= self.sinopsismovie1, fg = "White", bg ='black',font=('cursive', 12) )
        self.head1.place(x= 0, y =0)
        self.head1 = Label(self.sinopsis, text=self.sinopsismov1, fg = "White", bg ='black',font=('cursive', 12) )
        self.head1.place(x= 0, y =25)
        self.head1 = Label(self.sinopsis, text=self.sinopsismo1, fg = "White", bg ='black',font=('cursive', 12) )
        self.head1.place(x= 0, y =50)
        self.head1 = Label(self.sinopsis, text=self.sinopsism1, fg = "White", bg ='black',font=('cursive', 12) )
        self.head1.place(x= 0, y =75)
        #Frame of Foto
        self.framemovie2 = Frame(self.cartelera, width= 210, height = 300, background='white')
        self.framemovie2.place(x = 450, y = 300) 
        #Frame of Text
        self.sinopsis2 = Frame(self.cartelera, width= 310, height = 100, background='Black')
        self.sinopsis2.place(x = 80, y = 380 ) 

        self.head2 = Label(self.sinopsis2, text = self.sinopsismovie2, fg = "White", bg ='black',font=('cursive', 12) )
        self.head2.place(x= 0, y =0)
        self.head2 = Label(self.sinopsis2, text =self.sinopsismov2, fg = "White", bg ='black',font=('cursive', 12) )
        self.head2.place(x= 0, y =25)
        self.head2 = Label(self.sinopsis2, text =self.sinopsismo2, fg = "White", bg ='black',font=('cursive', 12) )
        self.head2.place(x= 0, y =50)
        self.head2 = Label(self.sinopsis2, text =self.sinopsism2, fg = "White", bg ='black',font=('cursive', 12) )
        self.head2.place(x= 0, y =75)
        
        self.imgUserwk = PhotoImage(file =f'{img_dir}/images/movies/Panteranegra.png')
        Label(self.framemovie, image=self.imgUserwk, bg = 'white').place(x=0, y=0)
        
        self.imgUserlilo = PhotoImage(file =f'{img_dir}/images/movies/lilo-mi-amigo-el-cocodrilo.png')
        Label(self.framemovie2, image=self.imgUserlilo, bg = 'white').place(x=0, y=0)

        self.botonsalirCartelera= Button(self.cartelera, text=f'Salir', width = 8, height =1, command=self.cartelera.destroy)
        self.botonsalirCartelera.place(x =20, y=510)

    #CuartaPantalla
    def reserves(self):
        self.reserves = Toplevel()
        self.reserves.title('Reservar Lugar')
        self.reserves.geometry('670x500')
        self.reserves.configure(bg ="#154360")
        self.reserves.resizable(False, False)
        
        self.title = Frame(self.reserves, width= 450, height = 25)
        self.title.pack()
        self.title2 =Label(self.title, text ="Pantalla", fg ='black' ).place(x=220, y = 0)
        self.frame = Frame(self.reserves, width= 600, height = 500)
        self.frame.place(x = 100, y =50)
    
        lista = ['A','B','C','D','E','F']
        buttons = []

        # Disable the button when is clicked
        def checkout(row, col):
            print("Checkout {} {}".format(row,col))
            
        def disable( button):
            button.config(state="disabled")

        for i in range(6):
            buttons.append([])
            for j in range(6):
                button = Button(self.frame, width = 10, height =2, text="{}{}".format(lista[i], (j+1)))
                button.grid(row=i, column=j)
                buttons[i].append(button)

        for i in range(6):
            for j in range(6):
                buttons[i][j].config(command=lambda b=buttons[i][j]: disable(b))
