from tkinter import *

root = Tk()
root.title("Ventana principal")
root.geometry("300x100")

botonQuit = Button(root, text="Quit", command=root.destroy)
botonQuit.place(x=400, y=450)

ventana_nueva1 = Toplevel()
ventana_nueva1.geometry("300x200")
ventana_nueva1.title("Ventana secundaria")

mainloop()