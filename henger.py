from tkinter import *
ablak= Tk()
mezo1=Entry(ablak)
mezo1.grid(row=1, column=1)
mezo1felirat=Label(ablak, text="Sugár (cm):")
mezo1felirat.grid(row=1, column=0)

mezo2=Entry(ablak)
mezo2.grid(row=2, column=1)
mezo2felirat=Label(ablak, text="Magasság (cm):")
mezo2felirat.grid(row=2, column=0)

mezo3=Entry(ablak)
mezo3.grid(row=5, column=1)
mezo3felirat=Label(ablak, text="Térfogat")
mezo3felirat.grid(row=5, column=0)

mezo4=Entry(ablak)
mezo4.grid(row=6, column=1)
mezo4felirat=Label(ablak, text="Vashenger")
mezo4felirat.grid(row=6, column=0)

mezo5=Entry(ablak)
mezo5.grid(row=7, column=1)
mezo5felirat=Label(ablak, text="Fahenger")
mezo5felirat.grid(row=7, column=0)

gomb1=Button(ablak, text="Kiszámít")
gomb1.grid(row=3, column=1)

ablak.mainloop()