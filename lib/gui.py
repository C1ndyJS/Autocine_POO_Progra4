from  tkinter import *
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

        self.password = Entry(self.framepw, show ='*', width=25, fg='black', border = 5, bg = 'white', font=('Microsoft YaHeu UI Light', 10))
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
        self.correo = Label(self.Columna, text =f'XXXXX', fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold') )
        self.correo.place(x=50, y= 110) 
        self.Nombre = Label(self.Columna, text =f' Nombre:XXXX', fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold') )
        self.Nombre.place(x=0, y= 150)        
        self.Iden = Label(self.Columna, text =f' Ident:XXXXXX', fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold'))
        self.Iden.place(x=0, y= 170)
        self.Edad = Label(self.Columna, text =f' Edad:XXXXX años', fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold') )
        self.Edad.place(x=0, y= 190)
        self.DNIT = Label(self.Columna, text =f' DniT:XXXX', fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold') )
        self.DNIT.place(x=0, y= 210)
        self.Phone = Label(self.Columna, text =f' phone:XXXXXXXXXX CO', fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold') )
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
        self.cartelera.geometry('700x600')
        self.cartelera.configure(bg ="#154360")
        self.cartelera.resizable(False, False)
        
        self.fila1 = Frame(self.cartelera, width = 700, height= 65, bg ='black')
        self.fila1.place(x=0, y=0)
        self.heading = Label(self.fila1, text = 'Cartelera', bg = 'black', )
        self.framemovie = Frame(self.cartelera, width= 200, height = 200, background='white')
        self.framemovie.place(x = 50, y = 100)
        
        self.framemovie = Frame(self.cartelera, width= 200, height = 200, background='white')
        self.framemovie.place(x = 450, y = 350)
    #CuartaPantalla

    def reserves(self):
        # Create the main window
        self.reserves = Toplevel()
        # Create a frame for the parking map
        frame = Frame(self.reserves)
        frame.pack()

        # Create a 2D array of Buttons representing the Parkin space.
        seats = []
        rows = ['A','B','C','D','F','G']
        for row in range(len(rows)):
            seats.append([])
            for col in range(6):
                seat = IntVar()
                #cb = Checkbutton(frame, text=f'Parqueader {row},{col}', variable=seat)
                cb = Button(frame,text=f'{rows[row]}{col}',bg="white",width=3, padx=25, pady=25)
                cb.grid(row=row, column=col)
                seats[row].append(seat)
        # Create a button to reserve the selected seats
        reserve_button = Button(self.reserves, text='Reserve seats', command=lambda: reserve_seats(seats))
        reserve_button.pack()