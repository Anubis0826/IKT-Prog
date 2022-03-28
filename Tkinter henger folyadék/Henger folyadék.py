from tkinter import *
ablak= Tk()
ablak.geometry("600x400")

mezo1=Entry(ablak)
mezo1.grid(row=1, column=1)
mezo1felirat=Label(ablak, text="Sugár (cm):")
mezo1felirat.grid(row=1, column=0)
ablak.mainloop()