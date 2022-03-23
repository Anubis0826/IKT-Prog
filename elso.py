from tkinter import *
from math import sqrt
def osszeg():
    a=int(mezo1.get())
    b=int(mezo2.get())
    c=a+b
    mezo3.delete(0, END)
    mezo3.insert(0, "Összeg: "+str(c))
def kivonas():
    a=int(mezo1.get())
    b=int(mezo2.get())
    c=a-b
    mezo3.delete(0, END)
    mezo3.insert(0, "Különbség: "+str(c))
def szorzas():
    a=int(mezo1.get())
    b=int(mezo2.get())
    c=a*b
    mezo3.delete(0, END)
    mezo3.insert(0, "Szorzat: "+str(c))
def osztas():
    a=int(mezo1.get())
    b=int(mezo2.get())
    if a==0 or b==0:
        mezo3.delete(0, END)
        mezo3.configure(fg="red")
        mezo3.insert(0, "Nullával nem osztunk.")
    else:
        c=a/b
        mezo3.delete(0, END)
        mezo3.configure(fg="black")
        mezo3.insert(0, "Hányados: "+str(c))
def negyzetre():
    a = int(mezo1.get())
    if mezo2.get() != "":
        mezo3.delete(0, END)
        mezo3.insert(0, "Csak az elsőbe írj számot!")
        mezo2.delete(0, END)
    else:
        c=a*a
        mezo3.delete(0, END)
        mezo3.insert(0, "A megoldás: "+str(c))
def gyokvonas():
    a = int(mezo1.get())
    if mezo2.get() != "":
        mezo3.delete(0, END)
        mezo3.insert(0, "Csak az elsőbe írj számot!")
        mezo2.delete(0, END)
    else:
        c=sqrt(a)
        mezo3.delete(0, END)
        mezo3.insert(0, "A megoldás: "+str(c))

foablak=Tk()
cimke=Label(foablak, text="Üdvözlet", fg="red")
cimke.pack()
gomb1=Button(foablak, text="OK")
gomb1.pack()
gomb2=Button(foablak, text="Mégse")
gomb2.pack()
gomb3=Button(foablak, text="Kilépés", command=foablak.destroy)
gomb3.pack()
mezo1=Entry(foablak)
mezo1.grip (row=0, column=1)
elso_szam=label(foablak, text="Második szám:")
elso_szam.grid(row=0, culomn=0)
masodik_szam=label(foablak, text="Második szám:")
masodik_szam.grid
mezo2=Entry(foablak)
mezo2.grid(row=1, culomn=1)
gomb4=Button(foablak, text="Összead", command=osszeg)
gomb4.pack()
gomb5=Button(foablak, text="Kivonás", command=kivonas)
gomb5.pack()
gomb6=Button(foablak, text="Szorzás", command=szorzas)
gomb6.pack()
gomb7=Button(foablak, text="Osztás", command=osztas)
gomb7.pack()
gomb8=Button(foablak, text="Négyzetre emelés", command=negyzetre)
gomb8.pack()
gomb9=Button(foablak, text="Gyökvonás", command=gyokvonas)
gomb9.pack()
mezo3=Entry(foablak)
mezo3.pack()

can1 = Canvas(foablak, width =185, height =210, bg='white')
photo = PhotoImage(file ='anu.gif')
item = can1.create_image(80,80, image =photo)
can1.pack()

foablak.mainloop()