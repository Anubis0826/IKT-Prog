from tkinter import *
ablak = Tk()
mezo1=Entry(ablak)
mezo1.grid(row=0, column=2)
mezo1felirat=Label(ablak, text="Első mező:")
mezo1felirat.grid(row=0, column=1)


kep = 'H:\\IKT Prog\\'
ablak1.geometry('600x600')
ablak1.title('tk')
icon= PhotoImage(file=kep+'red.png')
ablak1.iconphoto(True, icon)
ablak1.config(background='white')
elsokep=PhotoImage(file=kep+'lámpa.png')
gombkep=PhotoImage(file=kep+'lámpa.png', width='50', height='50')
cimke = Label(ablak1,
                font=('Arial', 45, 'bold'),
                bd=10,
                relief=RAISED,
                padx=25,
                pady=30,
                image=elsokep,
                compound='center'
                ).pack()



ablak.mainloop()