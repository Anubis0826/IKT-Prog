from tkinter import *
from math import sqrt
ablak= Tk()
ablak.geometry("600x400")

def osszeg():
    a=int(mezo1.get())
    b=int(mezo2.get())
    c=a+b
    mezo3.delete(0, END)
    mezo3.insert(0, "Összeg: "+str(c))
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
mezo3felirat=Label(ablak, text="Mennyi fér még bele(%):")
mezo3felirat.grid(row=3, column=0)
gomb1=Button(foablak, text="Összead", command=osszeg)
gomb4.pack()
gomb1.grid(row=4, column=1)
ablak.mainloop()