from  tkinter import*
from tkinter import messagebox

root =Tk()
root.title('Login')
root.geometry('450x600')
root.configure(bg ="white")
root.resizable(False, False)

#Primera Pantalla
imgUser = PhotoImage(file ='C:\\Users\\cmjim\\OneDrive\\Escritorio\\Cindy\\Parciales\\icons8-user-100.png')
Label(root, image=imgUser, bg = 'white').place(x=180, y=105)

frameUs = Frame(root, width = 250, height= 250, bg ='white')
frameUs.place(x=140, y = 235)

user = Entry(frameUs, width=25, fg='black', border = 5, bg = 'white', font=('Microsoft YaHeu UI Light', 10))
user.place(x = 1, y = 0)
user.insert(0,"username")

#===========================================================

framepw = Frame(root, width = 250, height= 250, bg ='white')
framepw.place(x=140, y = 285)

password = Entry(framepw, show ='*', width=25, fg='black', border = 5, bg = 'white', font=('Microsoft YaHeu UI Light', 10))
password.place(x = 1, y = 0)    
password.insert(0,"Password")

botonQuit = Button(root, text="Quit", command=root.destroy)
botonQuit.place(x=400, y=450)
#===========================================================


#===========================================================
'''
#img = PhotoImage(file ='C:\\Users\\cmjim\\OneDrive\\Escritorio\\Cindy\\Parciales\\icons8-login-100.png')
#Label(root, image=img, bg = 'white').place(x=100, y=255)

imgIcon = PhotoImage(file ='C:\\Users\\cmjim\\OneDrive\\Escritorio\\Cindy\\Parciales\\icons8-lock-100.png')
#Label(root, image=imgIcon, bg ='white').place(x=20, y=400)

heading = Label(frame, text ='_________________', fg ='#209898', bg = 'white', font=('Microsoft YaHeu UI Light', 15, 'bold') )
heading.place(x=0, y= 0)

'''

root.mainloop()

