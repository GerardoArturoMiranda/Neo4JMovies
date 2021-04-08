from tkinter import *
from api import Api
raiz = Tk()
raiz.title("Proyecto Final Bases De Datos Avanzadas")
miFrame = Frame()
miFrame.pack()
miFrame.config(width="500", height="750", bg="yellow")
a = Api()
#L Ó G I C A
def clearTextInput():
    textInformacionPelicula.delete("1.0","end")
def query1():
    anoEstadistico = inputAno.get()
    resultado = a.query1(anoEstadistico)
    textInformacionPelicula.insert(END,resultado)
def query2():
    generoEstadistico = inputGenero.get()
    resultado = a.query2(generoEstadistico)
    textInformacionPelicula.insert(END,resultado)
def query3():
    actorEstadistico = inputActor.get()
    resultado = a.query3(actorEstadistico)
    textInformacionPelicula.insert(END,resultado)
#L A B E L S
#Labels de Bienvenido
labelBienvenido = Label(miFrame, text="Bienvenido", font=("Futura", 16))
labelBienvenido.grid(row=0,column=2)
labelBienvenido.config(bg="yellow")
#Labels de QUERY1
labelIngresar1 = Label(miFrame, text="QUERY 1.- Ingrese el año del que desea conocer cuántas películas posee la base de datos ", font=("Futura", 16))
labelIngresar1.grid(row=1,column=1, padx=5, pady=5)
labelIngresar1.config(bg="yellow")
#Labels de QUERY2
labelIngresar2 = Label(miFrame, text="QUERY 2.- Ingrese el genero del que desea conocer cuántas películas posee la base de datos ", font=("Futura", 16))
labelIngresar2.grid(row=2,column=1, padx=5, pady=5)
labelIngresar2.config(bg="yellow")
#Labels de QUERY3
labelIngresar3 = Label(miFrame, text="QUERY 3.- Ingrese el actor del que desea conocer cuántas películas posee la base de datos ", font=("Futura", 16))
labelIngresar3.grid(row=3,column=1, padx=5, pady=5)
labelIngresar3.config(bg="yellow")
#I N P U T S
#Inputs de Ano QUERY1
inputAno = Entry(miFrame, width=50)
inputAno.grid(row=1,column=2, padx=5, pady=5)
#Inputs de Ano QUERY2
inputGenero = Entry(miFrame, width=50)
inputGenero.grid(row=2,column=2, padx=5, pady=5)
#Inputs de Ano QUERY3
inputActor = Entry(miFrame, width=50)
inputActor.grid(row=3,column=2, padx=5, pady=5)
#B O T Ó N
#Botón Ano
botonQ1 = Button(miFrame, text = "Consultar Información", command=query1, width=20)
botonQ1.grid(row=1,column=3, padx=5, pady=5)
#Botón Ano
botonQ2 = Button(miFrame, text = "Consultar Información", command=query2, width=20)
botonQ2.grid(row=2,column=3, padx=5, pady=5)
#Botón Actor
botonQ3 = Button(miFrame, text = "Consultar Información", command=query3, width=20)
botonQ3.grid(row=3,column=3, padx=5, pady=5)
#T E X T
#Texto de InformaciónPelicula
textInformacionPelicula = Text(miFrame)
textInformacionPelicula.grid(row=9,column=2, padx=5, pady=5)
#Listener
raiz.mainloop()