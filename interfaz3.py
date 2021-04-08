from tkinter import *
from api import Api
#L Ó G I C A
def agregarActor():
    siguienteRenglon = len(totalInputs)

    # add label in first row 
    lab = Label(miFrame, text="Actor .- "+str(len(inputsCast)+1)+":",  font=("Futura", 16))
    lab.grid(row=siguienteRenglon, column=1)
    lab.config(bg="beige")

    # add entry in second row
    ent = Entry(miFrame,width=50)
    ent.grid(row=siguienteRenglon, column=2)
    ent.config(bg="pink")
    #int(string)
    inputsCast.append( ent )
    totalInputs.append(1)
def registrarPelicula():
    nombrePelicula = inputNombrePelicula.get()
    print(str(nombrePelicula))
    descripcion = inputDescripcion.get()
    print(str(descripcion))
    dateAdded = inputDA.get()
    print(str(dateAdded))
    show_id = inputId.get()
    print(str(show_id))
    tipo = inputTipo.get()
    print(str(tipo))
    rating = inputRating.get()
    print(str(rating))
    pais = inputPais.get()
    print(str(pais))
    duracion = inputDuracion.get()
    print(str(duracion))
    ano = inputAno.get()
    ano = int(ano)
    directores = inputDirectores.get()
    print(str(directores))
    genero = inputGenero.get()
    print(str(genero))
    
    for i in inputsCast:
        actores.append(inputsCast.pop().get())
    a.registrarPelicula(nombrePelicula, descripcion, dateAdded, show_id, tipo, rating, pais, duracion,ano, directores, genero, actores)
    
    labelVerificacion['text'] = "Verificar En Consola"  

raiz = Tk()
raiz.title("Proyecto Final Bases De Datos Avanzadas")
miFrame = Frame()
miFrame.pack()
miFrame.config(width="500", height="750", bg="beige")
a = Api()
totalInputs=[1,2,3,4,5,6,7,8,9,10,11,12]
inputsCast=[]
actores=[]
#L A B E L S
#Labels de Bienvenido
labelBienvenido = Label(miFrame, text="Registrar →→→→→→→→→", font=("Futura", 16))
labelBienvenido.grid(row=0,column=2)
labelBienvenido.config(bg="beige")
#Labels de Película
labelIngresarNombrePelicula = Label(miFrame, text="Ingrese el nombre de la película o show : ", font=("Futura", 16))
labelIngresarNombrePelicula.grid(row=1,column=1, padx=5, pady=5)
labelIngresarNombrePelicula.config(bg="beige")
#Labels de Descripción
labelIngresarDescripcion = Label(miFrame, text="Ingrese la descripción de la película:", font=("Futura", 16))
labelIngresarDescripcion.grid(row=2,column=1, padx=5, pady=5)
labelIngresarDescripcion.config(bg="beige")
#Labels de Date_Added
labelIngresarFecha = Label(miFrame, text="Ingrese la fecha cuando estás registrando esta película: ", font=("Futura", 16))
labelIngresarFecha.grid(row=3,column=1, padx=5, pady=5)
labelIngresarFecha.config(bg="beige")
#Labels de Id
labelIngresarId = Label(miFrame, text="Ingrese el show_id de la película ", font=("Futura", 16))
labelIngresarId.grid(row=4,column=1, padx=5, pady=5)
labelIngresarId.config(bg="beige")
#Labels de Tipo
labelIngresarTipo = Label(miFrame, text="Ingrese su tipo(Show, Movie, Series): ", font=("Futura", 16))
labelIngresarTipo.grid(row=5,column=1, padx=5, pady=5)
labelIngresarTipo.config(bg="beige")
#Labels de Rating
labelIngresarRating = Label(miFrame, text="Ingrese su rating(A, AA, D, C, B15, B): ", font=("Futura", 16))
labelIngresarRating.grid(row=6,column=1, padx=5, pady=5)
labelIngresarRating.config(bg="beige")
#Labels de País
labelIngresarPais = Label(miFrame, text="Ingrese su país(México, Estados Unidos, Japón, etc.): ", font=("Futura", 16))
labelIngresarPais.grid(row=7,column=1, padx=5, pady=5)
labelIngresarPais.config(bg="beige")
#Labels de Duración
labelIngresarDuracion = Label(miFrame, text="Ingrese su duración(90 min, 3 temporadas, etc.): ", font=("Futura", 16))
labelIngresarDuracion.grid(row=8,column=1, padx=5, pady=5)
labelIngresarDuracion.config(bg="beige")
#Labels de InformacionPelicula
labelAno = Label(miFrame, text="Ingrese el año en que se estrenó:", font=("Futura", 16))
labelAno.grid(row=9,column=1, padx=5, pady=5)
labelAno.config(bg="beige")
#Labels de Directores
labelDirectores = Label(miFrame, text="Ingrese los  directores:", font=("Futura", 16))
labelDirectores.grid(row=10,column=1, padx=5, pady=5)
labelDirectores.config(bg="beige")
#Labels de Género
labelGenero = Label(miFrame, text="Ingrese el género:", font=("Futura", 16))
labelGenero.grid(row=11,column=1, padx=5, pady=5)
labelGenero.config(bg="beige")
#Labels de Verificacion
labelVerificacion = Label(miFrame, text="", font=("Futura", 16))
labelVerificacion.grid(row=0,column=1, padx=5, pady=5)
labelVerificacion.config(bg="beige")
#I N P U T S
#Inputs de Película
inputNombrePelicula = Entry(miFrame, width=50)
inputNombrePelicula.grid(row=1,column=2, padx=5, pady=5)
#Inputs de Descipcion
inputDescripcion = Entry(miFrame, width=50)
inputDescripcion.grid(row=2,column=2, padx=5, pady=5)
#Inputs de DataAddred
inputDA = Entry(miFrame, width=50)
inputDA.grid(row=3,column=2, padx=5, pady=5)
#Inputs de Información Año
inputId = Entry(miFrame, width=50)
inputId.grid(row=4,column=2, padx=5, pady=5)
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
#Inputs de Información Duración
inputAno = Entry(miFrame, width=50)
inputAno.grid(row=9,column=2, padx=5, pady=5)
#Inputs de Información Duración
inputDirectores = Entry(miFrame, width=50)
inputDirectores.grid(row=10,column=2, padx=5, pady=5)
#Inputs de Genero
inputGenero = Entry(miFrame, width=50)
inputGenero.grid(row=11,column=2, padx=5, pady=5)

#Botón Borrar
botonConsultarPelicula = Button(miFrame, text = "Agregar Actor", command=agregarActor,width=20)
botonConsultarPelicula.grid(row=10,column=4, padx=5, pady=5)
#Botón Borrar
botonRegistrar = Button(miFrame, text = "Registrar", command=registrarPelicula, width=20)
botonRegistrar.grid(row=0,column=4, padx=5, pady=5)

#Listener
raiz.mainloop()

