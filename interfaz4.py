from tkinter import *
from api import Api
#L Ó G I C A
def actualizarPelicula():
    nombrePelicula = inputNombrePelicula.get()
    print(str(nombrePelicula))
    descripcion = inputDescripcion.get()
    print(str(descripcion))
    dateAdded = inputDA.get()
    print(str(dateAdded))
    show_id = inputId.get()
    print(str(show_id))
    a.actualizarPelicula(nombrePelicula, descripcion, dateAdded, show_id)
    labelVerificacion['text'] = "Verificar En Consola"  
raiz = Tk()
raiz.title("Proyecto Final Bases De Datos Avanzadas")
miFrame = Frame()
miFrame.pack()
miFrame.config(width="500", height="750", bg="orange")
a = Api()
#L A B E L S
#Labels de Bienvenido
labelBienvenido = Label(miFrame, text="Actualizar →→→→→→→→→", font=("Futura", 16))
labelBienvenido.grid(row=0,column=2)
labelBienvenido.config(bg="orange")
#Labels de Película
labelIngresarNombrePelicula = Label(miFrame, text="Ingrese el nombre de la película o show a editar: ", font=("Futura", 16))
labelIngresarNombrePelicula.grid(row=1,column=1, padx=5, pady=5)
labelIngresarNombrePelicula.config(bg="orange")
#Labels de Descripción
labelIngresarDescripcion = Label(miFrame, text="Ingrese la descripción de la película:", font=("Futura", 16))
labelIngresarDescripcion.grid(row=2,column=1, padx=5, pady=5)
labelIngresarDescripcion.config(bg="orange")
#Labels de Date_Added
labelIngresarFecha = Label(miFrame, text="Ingrese la fecha cuando estás registrando esta película: ", font=("Futura", 16))
labelIngresarFecha.grid(row=3,column=1, padx=5, pady=5)
labelIngresarFecha.config(bg="orange")
#Labels de Id
labelIngresarId = Label(miFrame, text="Ingrese el show_id de la película ", font=("Futura", 16))
labelIngresarId.grid(row=4,column=1, padx=5, pady=5)
labelIngresarId.config(bg="orange")
#Labels de Verificacion
labelVerificacion = Label(miFrame, text="", font=("Futura", 16))
labelVerificacion.grid(row=0,column=1, padx=5, pady=5)
labelVerificacion.config(bg="orange")
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


#Botón Borrar
botonRegistrar = Button(miFrame, text = "Actualizar", command=actualizarPelicula, width=20)
botonRegistrar.grid(row=0,column=4, padx=5, pady=5)

#Listener
raiz.mainloop()

