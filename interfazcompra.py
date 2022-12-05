from  tkinter import*
from tkinter import messagebox

raiz =Tk()

miframe=Frame(raiz)

miframe.pack()
pantalla=Label(miframe,text="PANTALLA",pady=25)
pantalla.grid(row=0 ,column=0,columnspan=6)
ima=PhotoImage(file=r'C:\Users\Usuario\Downloads\icons8-user-100.png')

usernsme=Label(miframe,image=ima,bg="blue",padx=300,pady= 200 ,relief="solid")
usernsme.grid(row=1,column=6,rowspan=3)

info=Label(miframe,text="PELICULA INFO",padx=85,pady= 65 ,relief="solid",justify="right")
info.grid(row=5,column=6,rowspan=2)

info2=Label(miframe,text="HORA ENTRADA",padx=82,pady= 70 ,relief="solid")
info2.grid(row=3,column=6,rowspan=2)



#letra=Label(miframe,text="hola").place(x=10,y=10)

   

posa1=Button(miframe,text="A1",bg="white",width=3, padx=25, pady=25)
posa1.grid(row=1,column=0)
posa2=Button(miframe,text="A2",bg="white",width=3, padx=25, pady=25)
posa2.grid(row=1,column=1)
posa3=Button(miframe,text="A3",bg="white",width=3, padx=25, pady=25)
posa3.grid(row=1,column=2)
posa4=Button(miframe,text="A4",bg="white",width=3, padx=25, pady=25)
posa4.grid(row=1,column=3)
posa5=Button(miframe,text="A5",bg="white",width=3, padx=25, pady=25)
posa5.grid(row=1,column=4)
posa6=Button(miframe,text="A6",bg="white",width=3, padx=25, pady=25)
posa6.grid(row=1,column=5)

posb1=Button(miframe,text="B1",bg="white",width=3, padx=25, pady=25)
posb1.grid(row=2,column=0)
posb2=Button(miframe,text="B2",bg="white",width=3, padx=25, pady=25)
posb2.grid(row=2,column=1)
posb3=Button(miframe,text="B3",bg="white",width=3, padx=25, pady=25)
posb3.grid(row=2,column=2)
posb4=Button(miframe,text="B4",bg="white",width=3, padx=25, pady=25)
posb4.grid(row=2,column=3)
posb5=Button(miframe,text="B5",bg="white",width=3, padx=25, pady=25)
posb5.grid(row=2,column=4)
posb6=Button(miframe,text="B6",bg="white",width=3, padx=25, pady=25)
posb6.grid(row=2,column=5)

posc1=Button(miframe,text="C1",bg="white",width=3, padx=25, pady=25)
posc1.grid(row=3,column=0)
posc2=Button(miframe,text="C2",bg="white",width=3, padx=25, pady=25)
posc2.grid(row=3,column=1)
posc3=Button(miframe,text="C3",bg="white",width=3, padx=25, pady=25)
posc3.grid(row=3,column=2)
posc4=Button(miframe,text="C4",bg="white",width=3, padx=25, pady=25)
posc4.grid(row=3,column=3)
posc5=Button(miframe,text="C5",bg="white",width=3, padx=25, pady=25)
posc5.grid(row=3,column=4)
posc6=Button(miframe,text="C6",bg="white",width=3, padx=25, pady=25)
posc6.grid(row=3,column=5)

posd1=Button(miframe,text="D1",bg="white",width=3, padx=25, pady=25)
posd1.grid(row=4,column=0)
posd2=Button(miframe,text="D2",bg="white",width=3, padx=25, pady=25)
posd2.grid(row=4,column=1)
posd3=Button(miframe,text="D3",bg="white",width=3, padx=25, pady=25)
posd3.grid(row=4,column=2)
posd4=Button(miframe,text="D4",bg="white",width=3, padx=25, pady=25)
posd4.grid(row=4,column=3)
posd5=Button(miframe,text="D5",bg="white",width=3, padx=25, pady=25)
posd5.grid(row=4,column=4)
posd6=Button(miframe,text="D6",bg="white",width=3, padx=25, pady=25)
posd6.grid(row=4,column=5)

pose1=Button(miframe,text="E1",bg="white",width=3, padx=25, pady=25)
pose1.grid(row=5,column=0)
pose2=Button(miframe,text="E2",bg="white",width=3, padx=25, pady=25)
pose2.grid(row=5,column=1)
pose3=Button(miframe,text="E3",bg="white",width=3, padx=25, pady=25)
pose3.grid(row=5,column=2)
pose4=Button(miframe,text="E4",bg="white",width=3, padx=25, pady=25)
pose4.grid(row=5,column=3)
pose5=Button(miframe,text="E5",bg="white",width=3, padx=25, pady=25)
pose5.grid(row=5,column=4)
pose6=Button(miframe,text="E6",bg="white",width=3, padx=25, pady=25)
pose6.grid(row=5,column=5)

posf1=Button(miframe,text="F1",bg="white",width=3, padx=25, pady=25)
posf1.grid(row=6,column=0)
posf2=Button(miframe,text="F2",bg="white",width=3, padx=25, pady=25)
posf2.grid(row=6,column=1)
posf3=Button(miframe,text="F3",bg="white",width=3, padx=25, pady=25)
posf3.grid(row=6,column=2)
posf4=Button(miframe,text="F4",bg="white",width=3, padx=25, pady=25)
posf4.grid(row=6,column=3)
posf5=Button(miframe,text="F5",bg="white",width=3, padx=25, pady=25)
posf5.grid(row=6,column=4)
posf6=Button(miframe,text="F6",bg="white",width=3, padx=25, pady=25)
posf6.grid(row=6,column=5)


raiz.mainloop()