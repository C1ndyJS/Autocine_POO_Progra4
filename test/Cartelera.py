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
#En PANTERA NEGRA: WAKANDA POR SIEMPRE de Marvel Studios, la reina Ramonda (Angela Bassett), 
# Shuri (Letitia Wright), M'Baku (Winston Duke), Okoye (Danai Gurira) y las Dora Milaje 
# (incluida Florence Kasumba) luchan por proteger a su nación de las potencias mundiales que 
# intervienen tras la muerte del Rey T'Challa. Mientras los habitantes de Wakanda se esfuerzan 
# por embarcarse en un nuevo capítulo, los héroes deben unirse con la ayuda de War Dog Nakia (Lupita Nyong'o) 
# y Everett Ross (Martin Freeman) y forjar un nuevo camino para el reino de Wakanda.
#  El film que cuenta con Tenoch Huerta como Namor, rey de una nación submarina oculta,
#  también está protagonizada por Dominique Thorne, Michaela Coel, Mabel Cadena y Alex Livanalli.
'''Título Original
Black Panther: Wakanda Forever

País de Origen
United States of America

Director
Ryan Coogler.

Actores
Angela Bassett, Letitia Wright, Winston Duke, Danai Gurira, Florence Kasumba, Lupita Nyong'o, Martin Freeman, Tenoch Huerta, Dominique Thorne, Michaela Coel, Mabel Cadena y Alex Livanalli.

Lenguaje
Inglés
'''
#Pelicula #2
'''Basado en la serie best selling de libros con el mismo nombre, Lyle, Lyle Crocodile es traida a la gran 
pantalla como un musical live action para toda la familia. La historia sigue a la familia Primm, que acaba 
de llegar a Nueva York por el nuevo trabajo del Señor Primm. Josh Primm, de 12 años, le teme a muchas cosas 
y le cuesta hacer amigos. Cuando Josh descubre a Lyle, un cocodrilo que baila y canta en su ático, los dos 
forman un vínculo inusual mientras Lyle le muestra la magia de Nueva York a su nuevo amigo. Mientras cada 
miembro de la familia encuentra una relación única con Lyle, los Primm se transforman y adoptan un nuevo 
sentido del amor y la aventura. Cuando el antiguo dueño de Lyle, el excéntrico Hector P. Valenti, vuelve 
a reclamar a su cocodrilo para un nuevo acto musical, los Primm se dan cuenta que este cocodrilo super 
talentoso y con un gran corazón les cambió la vida para siempre y deben ir a luchar para mantenerlo en la 
familia. ¡Con música original de Pasek & Paul (La La Land, El Gran Showman), el cocodrilo cantante nos 
tendrá a todos cantando con él!

Título Original
Lyle, Lyle Crocodile
País de Origen
United States of America
Director
Tetsuro Kodama.
Actores
Javier Barden (Hector P. Valenti), Shawn Mendez (Lyle), Sal Viscou, Don DiPetta.
Lenguaje
Inglés'''
pantallaMovies= InterfazMovie(Tk(), 'Wakanda Por Siempre', "Ciencia Ficcion", 16, 161)


