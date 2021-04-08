from tkinter import *
from api import Api
raiz = Tk()
raiz.title("Proyecto Final Bases De Datos Avanzadas")
miFrame = Frame()
miFrame.pack()
miFrame.config(width="500", height="750", bg="pink")
a = Api()
#L Ó G I C A
def clearTextInput():
    textInformacionPelicula.delete("1.0","end")
def obtenerInfoPelicula():
    nombrePelicula = inputNombrePelicula.get()
    resultado2 = a.obtenerInfoPelicula(nombrePelicula)
    textInformacionPelicula.insert(END,resultado2)
def obtenerInfoDePeliculaDeActor():
    nombreActor = inputNombreActor.get()
    resultado = a.obtenerInfoDePeliculaDeActor(nombreActor)
    textInformacionPelicula.insert(END,resultado)
def obtenerInfoPeliculaGenero():
    nombrePelicula = inputNombrePeliculaG.get()
    resultado = a.obtenerInfoGenero(nombrePelicula)
    textInformacionPelicula.insert(END,resultado)
def obtenerAnoPelicula():
    nombrePelicula = inputAnio.get()
    resultado = a.obtenerInfoAno(nombrePelicula)
    textInformacionPelicula.insert(END,resultado)
def obtenerTipoPelicula():
    nombrePelicula = inputTipo.get()
    resultado = a.obtenerInfoTipo(nombrePelicula)
    textInformacionPelicula.insert(END,resultado)
def obtenerRatingPelicula():
    nombrePelicula = inputRating.get()
    resultado = a.obtenerInfoRating(nombrePelicula)
    textInformacionPelicula.insert(END,resultado)
def obtenerPaisPelicula():
    nombrePelicula = inputPais.get()
    resultado = a.obtenerInfoPais(nombrePelicula)
    textInformacionPelicula.insert(END,resultado)
def obtenerDuracionPelicula():
    nombrePelicula = inputDuracion.get()
    resultado = a.obtenerInfoDuracion(nombrePelicula)
    textInformacionPelicula.insert(END,resultado)
#L A B E L S
#Labels de Bienvenido
labelBienvenido = Label(miFrame, text="Bienvenido", font=("Futura", 16))
labelBienvenido.grid(row=0,column=2)
labelBienvenido.config(bg="pink")
#Labels de Película
labelIngresarNombrePelicula = Label(miFrame, text="Ingrese el nombre de la película o show : ", font=("Futura", 16))
labelIngresarNombrePelicula.grid(row=1,column=1, padx=5, pady=5)
labelIngresarNombrePelicula.config(bg="pink")
#Labels de Actor
labelIngresarNombreActor = Label(miFrame, text="Ingrese el nombre del actor del que desea conocer sus película/s:", font=("Futura", 16))
labelIngresarNombreActor.grid(row=2,column=1, padx=5, pady=5)
labelIngresarNombreActor.config(bg="pink")
#Labels de Genero Pelicula
labelIngresarNombrePeliculaG = Label(miFrame, text="Ingrese el nombre de la película o show de la que quiere saber su género: ", font=("Futura", 16))
labelIngresarNombrePeliculaG.grid(row=3,column=1, padx=5, pady=5)
labelIngresarNombrePeliculaG.config(bg="pink")
#Labels de Año
labelIngresarAnio = Label(miFrame, text="Ingrese el nombre de la película o show de la que quiere saber su año: ", font=("Futura", 16))
labelIngresarAnio.grid(row=4,column=1, padx=5, pady=5)
labelIngresarAnio.config(bg="pink")
#Labels de Tipo
labelIngresarTipo = Label(miFrame, text="Ingrese el nombre de la película o show de la que quiere saber su tipo: ", font=("Futura", 16))
labelIngresarTipo.grid(row=5,column=1, padx=5, pady=5)
labelIngresarTipo.config(bg="pink")
#Labels de Rating
labelIngresarRating = Label(miFrame, text="Ingrese el nombre de la película o show de la que quiere saber su rating: ", font=("Futura", 16))
labelIngresarRating.grid(row=6,column=1, padx=5, pady=5)
labelIngresarRating.config(bg="pink")
#Labels de País
labelIngresarPais = Label(miFrame, text="Ingrese el nombre de la película o show de la que quiere saber su país: ", font=("Futura", 16))
labelIngresarPais.grid(row=7,column=1, padx=5, pady=5)
labelIngresarPais.config(bg="pink")
#Labels de Duración
labelIngresarDuracion = Label(miFrame, text="Ingrese el nombre de la película o show de la que quiere saber su duración: ", font=("Futura", 16))
labelIngresarDuracion.grid(row=8,column=1, padx=5, pady=5)
labelIngresarDuracion.config(bg="pink")
#Labels de InformacionPelicula
labelInformacionPelicula = Label(miFrame, text="Información:", font=("Futura", 16))
labelInformacionPelicula.grid(row=9,column=1, padx=5, pady=5)
labelInformacionPelicula.config(bg="pink")
#I N P U T S
#Inputs de Película
inputNombrePelicula = Entry(miFrame, width=50)
inputNombrePelicula.grid(row=1,column=2, padx=5, pady=5)
#Inputs de Actor
inputNombreActor = Entry(miFrame, width=50)
inputNombreActor.grid(row=2,column=2, padx=5, pady=5)
#Inputs de Información Película
inputNombrePeliculaG = Entry(miFrame, width=50)
inputNombrePeliculaG.grid(row=3,column=2, padx=5, pady=5)
#Inputs de Información Año
inputAnio = Entry(miFrame, width=50)
inputAnio.grid(row=4,column=2, padx=5, pady=5)
#Inputs de Información Tipo
inputTipo = Entry(miFrame, width=50)
inputTipo.grid(row=5,column=2, padx=5, pady=5)
#Inputs de Información Rating
inputRating = Entry(miFrame, width=50)
inputRating.grid(row=6,column=2, padx=5, pady=5)
#Inputs de Información País
inputPais = Entry(miFrame, width=50)
inputPais.grid(row=7,column=2, padx=5, pady=5)
#Inputs de Información Duración
inputDuracion = Entry(miFrame, width=50)
inputDuracion.grid(row=8,column=2, padx=5, pady=5)
#T E X T
#Texto de InformaciónPelicula
textInformacionPelicula = Text(miFrame)
textInformacionPelicula.grid(row=9,column=2, padx=5, pady=5)
#S C R O L L E R
#Scroller
scrollVert=Scrollbar(miFrame, command=textInformacionPelicula.yview)
scrollVert.grid(row=9,column=3)
#B O T Ó N
#Botón Actor
botonConsultar = Button(miFrame, text = "Consultar Película/s", command=obtenerInfoDePeliculaDeActor, width=20)
botonConsultar.grid(row=2,column=3, padx=5, pady=5)
#Botón Actor
botonConsultarPelicula = Button(miFrame, text = "Consultar Info Película", command=obtenerInfoPelicula, width=20)
botonConsultarPelicula.grid(row=1,column=3, padx=5, pady=5)
#Botón PeliG
botonConsultarPeliculaG = Button(miFrame, text = "Consultar Género", command=obtenerInfoPeliculaGenero, width=20)
botonConsultarPeliculaG.grid(row=3,column=3, padx=5, pady=5)
#Botón Anio
botonConsultarAnio = Button(miFrame, text = "Consultar Año", command=obtenerAnoPelicula, width=20)
botonConsultarAnio.grid(row=4,column=3, padx=5, pady=5)
#Botón Tipo
botonConsultarTipo = Button(miFrame, text = "Consultar Tipo", command=obtenerTipoPelicula, width=20)
botonConsultarTipo.grid(row=5,column=3, padx=5, pady=5)
#Botón Rating
botonConsultarRating = Button(miFrame, text = "Consultar Rating", command=obtenerRatingPelicula, width=20)
botonConsultarRating.grid(row=6,column=3, padx=5, pady=5)
#Botón País
botonConsultarPais = Button(miFrame, text = "Consultar País", command=obtenerPaisPelicula, width=20)
botonConsultarPais.grid(row=7,column=3, padx=5, pady=5)
#Botón Duración
botonConsultarDuracion = Button(miFrame, text = "Consultar Duración", command=obtenerDuracionPelicula, width=20)
botonConsultarDuracion.grid(row=8,column=3, padx=5, pady=5)
#Botón Borrar
botonConsultarPelicula = Button(miFrame, text = "Limpiar", command=clearTextInput, width=20)
botonConsultarPelicula.grid(row=9,column=4, padx=5, pady=5)

#Listener
raiz.mainloop()
