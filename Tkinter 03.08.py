from tkinter import *
def klikk():
    print('Klikkeltem')
ablak1 = Tk()
gyoker = 'H:\\IKT Prog\\'
ablak1.geometry('600x600')
ablak1.title('Boldog nő napot!')
icon= PhotoImage(file=gyoker+'red.png')
ablak1.iconphoto(True, icon)
ablak1.config(background='red')
elsokep=PhotoImage(file=gyoker+'anu.gif')
gombkep=PhotoImage(file=gyoker+'anu.gif', width='50', height='50')
cimke = Label(ablak1,
                text='Survivor',
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

gomb = Button(ablak1, 
                text='Kattints',
                fg='blue',
                font=('Comic Sans', 35, 'bold'),
                bg='red',
                relief=SUNKEN,
                bd=10,
                command=klikk,
                padx=12,
                pady=12,
                image=gombkep,
                compound='bottom',
                activeforeground='blue',
                state=ACTIVE).pack()

ablak1.mainloop()