from  tkinter import*
from tkinter import messagebox

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


class InterfazMovie(Movie): #Duracion en minutos
    def __init__(self, cartelera, nombre, genero,clasificacion_edad, duracion):
        super().__init__(nombre,genero,clasificacion_edad, duracion)
        self.cartelera = cartelera
        self.InformacionMovie()
    
    def InformacionMovie(self):
        self.cartelera.title('Login')
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

pantallaMovies= InterfazMovie(Tk(), 'Wakanda Por Siempre', "Ciencia Ficcion", 16, 161)
pantallaMovies.cartelera.mainloop()

#PELICULA #1
#Pelicula #2

pantallaMovies= InterfazMovie(Tk(), 'Wakanda Por Siempre', "Ciencia Ficcion", 16, 161)


