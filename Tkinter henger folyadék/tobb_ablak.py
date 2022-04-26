from tkinter import *
import math
abl1 = Tk()
abl1.geometry("600x400")

def ujablak():
    abl2=Toplevel(abl1)
    abl2.title('Eredmények')
    abl2.minsize(width=300,height=100)
    sz1=Label(abl2,text=felszin)
    sz2=Label(abl2,text=terfogat)
    m1=Entry(abl2)
    m2=Entry(abl2)
    gomb2=Button(abl2, text=felszin, command=abl2.destroy)
    uz2.pack()
    gomb2.pack()
    a = eval(mezo1.get())
    b = eval(mezo2.get())
    c = eval(mezo3.get())
    felszin=2*(a*b+a*c+b*c)
    terfogat=a*b*c
    m1.delete(0,END)
    m1.insert(0,str(felszin))
    m2.delete(0,END)
    m2.insert(0,str(terfogat))
    abl2.mainloop()



mezo1=Entry(abl1)
mezo1.grid(row=1, column=1)
mezo1felirat=Label(abl1, text="A")
mezo1felirat.grid(row=1, column=0)

mezo2=Entry(abl1)
mezo2.grid(row=2, column=1)
mezo2felirat=Label(abl1, text="B")
mezo2felirat.grid(row=2, column=0)

mezo3=Entry(abl1)
mezo3.grid(row=3, column=1)
mezo3felirat=Label(abl1, text="C")
mezo3felirat.grid(row=3, column=0)

gomb1=Button(abl1, text='Számítás', command=ujablak)
gomb1.grid(row=7, column=1)

abl1.mainloop()