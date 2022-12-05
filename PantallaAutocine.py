    
from  tkinter import*
from tkinter import messagebox


ventanaLevel = Tk()
ventanaLevel.title("Services Star")
ventanaLevel.geometry("700x500")
ventanaLevel.configure(bg = "white")
ventanaLevel.resizable(False, False)

Fila1 = Frame(ventanaLevel, width = 750, height= 95, bg ='black')
Fila1.place(x=1, y=0)

Columna = Frame(ventanaLevel, width = 550, height= 550, bg ='#2471A3')
Columna.place(x=500, y=0)

heading1 = Label(Columna, text ='___________', fg ='white', bg = '#2471A3', font=( "cursive",25, 'bold') )
heading1.place(x=0, y= 100)
heading2 = Label(Columna, text ='___________', fg ='white', bg = '#2471A3', font=( "cursive",25, 'bold') )
heading2.place(x=0, y= 300)
headingName = Label(Columna, text ='User', fg ='white', bg = '#2471A3', font=( "cursive",12, 'bold') )
headingName.place(x=77, y= 110)
imgUser = PhotoImage(file ='C:\\Users\\cmjim\\OneDrive\\Escritorio\\Cindy\\Parciales\\icons8-user-100.png')
Label(Columna, image = imgUser, bg ='#2471A3').place(x=50, y=10)

botonLot = Button(ventanaLevel, text="Log out", width = 15, command=ventanaLevel.destroy)
botonLot.place(x=30, y=35)

botonActInfo = Button(ventanaLevel, text="Actualizar Informacion", width = 25, command=ventanaLevel.destroy)
botonActInfo.place(x=290, y=35)

opciones = Frame(ventanaLevel, width=500, height=500, bg="#85C1E9")
opciones.place(x= 1, y = 100)

botonRegistroBoleta = Button(opciones, text="Registrar Compra", width = 15, height="10", command=ventanaLevel.destroy)
botonRegistroBoleta.place(x=70, y=100)

botonListarVentas = Button(opciones, text="Listar Venta", width = 15, height ="10", command=ventanaLevel.destroy)
botonListarVentas.place(x =200, y=100)

heading = Label(opciones, text ='______________________________', fg ='white', bg = '#85C1E9', font=( "cursive",25, 'bold') )
heading.place(x=0, y= 0)
heading = Label(opciones, text ='Hola! Vive la experienca Star today!', fg ='white', bg = '#85C1E9', font=( "Ananda Black",15, 'bold') )
heading.place(x=0, y= 8)


mainloop()
