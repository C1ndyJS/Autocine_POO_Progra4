from  tkinter import *
from lib.common import Persona, Vendedor
from lib.gui import Interfaz


c1 = Vendedor(100, "Pera", 30, 3123, 12345)
c2 = Persona(100, "Pepito", 32, 31983)
name = c1.GetName()

obj = Interfaz(Tk())
obj.root.mainloop()