from tkinter import *
ablak1 = Tk()
gyoker = 'H:\\IKT Prog\\'
ablak1.geometry('600x600')
ablak1.title('tk')
icon= PhotoImage(file=gyoker+'red.png')
ablak1.iconphoto(True, icon)
ablak1.config(background='white')
elsokep=PhotoImage(file=gyoker+'lámpa.png')
gombkep=PhotoImage(file=gyoker+'lámpa.png', width='50', height='50')
cimke = Label(ablak1,
                fg='#000000',
                bg='#c3cee0',
                font=('Arial', 45, 'bold'),
                bd=10,
                relief=RAISED,
                padx=25,
                pady=30,
                image=elsokep,
                compound='center'
                ).pack()

ablak1.mainloop()