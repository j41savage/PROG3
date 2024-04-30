import tkinter as tk
from PIL import Image,ImageTk

ventana=tk.Tk()
ventana.title("My first window")
ventana.geometry("1024x960")

lnombre=tk.Label(ventana,text="Nombre:");
lnombre.grid(column=0,row=1,pady=3)

cnombre=tk.Entry(ventana,width=30)
cnombre.grid(column=1,row=1,pady=3)    

lapellido=tk.Label(ventana,text="Apellido:")
lapellido.grid(column=0,row=2,pady=3)

capellido=tk.Entry(ventana,width=30)
capellido.grid(column=1,row=2,pady=3)

ledad=tk.Label(ventana,text="Edad:")    
ledad.grid(column=0,row=3,pady=3)

cedad=tk.Entry(ventana,width=30)
cedad.grid(column=1,row=3,pady=3)

lsexo=tk.Label(ventana,text="Sexo:")
lsexo.grid(column=0,row=4,pady=3)

cmasc= tk.Radiobutton(ventana,text="Masculino",value="M")
cmasc.grid(column=0,row=5,pady=3)

cfem= tk.Radiobutton(ventana,text="Femenino",value="F")
cfem.grid(column=1,row=5,pady=3)


lciudad=tk.Listbox(ventana,width=30,selectmode="single")    
lciudad.insert(1, "Barcelona")  
lciudad.insert(2, "Madrid")
lciudad.insert(3, "Sevilla")
lciudad.grid(column=1,row=6,pady=4)

lbutton=tk.Button(ventana,text="Registro")
lbutton.grid(column=1,row=7,pady=5)

ventana.mainloop()
