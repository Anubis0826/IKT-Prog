from tkinter import *
import math
ablak= Tk()
ablak.geometry("600x400")

def szamolas():
    mezo4.delete(0, END)
    sugar=int(mezo2.get())
    magas=int(mezo3.get())
    terf=math.pi*sugar**2*magas
    liter=terf/1000
    bor=int(mezo1.get())
    mezo4.insert(0,"{:.0f}".format(liter)+" literes a hordó.")

mezo1=Entry(ablak)
mezo1.grid(row=1, column=1)
mezo1felirat=Label(ablak, text="Bor mennyiség(l):")
mezo1felirat.grid(row=1, column=0)
mezo2=Entry(ablak)
mezo2.grid(row=2, column=1)
mezo2felirat=Label(ablak, text="Hány literes a hordó(cm):")
mezo2felirat.grid(row=2, column=0)
mezo3=Entry(ablak)
mezo3.grid(row=3, column=1)
mezo3felirat=Label(ablak, text="Magassága:")
mezo3felirat.grid(row=3, column=0)
mezo4=Entry(ablak)
mezo4.grid(row=4, column=1)
mezo4felirat=Label(ablak, text="Összesen:")
mezo4felirat.grid(row=4, column=0)

gomb1=Button(ablak, text="Összead", command=szamolas)
gomb1.grid(row=7, column=1)

ablak.mainloop()