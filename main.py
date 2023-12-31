from tkinter import *
from tkinter import messagebox
from functions import *

root = Tk()

root.title("Practica Base de datos")

frameSuperior = Frame(root, width=400, height=600, pady=15)
frameSuperior.pack()

# Creacion de los labels para el frame superior
labelId = Label(frameSuperior, text="ID Usuario")
labelId.grid(row=0, column=0, sticky="e", padx=5, pady=5)
labelId.config(font=("Verdana", 8))

labelNombre = Label(frameSuperior, text="Nombre Usuario")
labelNombre.grid(row=1, column=0, sticky="e", padx=5, pady=5)
labelNombre.config(font=("Verdana", 8))

labelApellido = Label(frameSuperior, text="Apellido Usuario")
labelApellido.grid(row=2, column=0, sticky="e", padx=5, pady=5)
labelApellido.config(font=("Verdana", 8))

labelEmail = Label(frameSuperior, text="Email Usuario")
labelEmail.grid(row=3, column=0, sticky="e", padx=5, pady=5)
labelEmail.config(font=("Verdana", 8))

labelPass = Label(frameSuperior, text="Contraseña Usuario")
labelPass.grid(row=4, column=0, sticky="e", padx=5, pady=5)
labelPass.config(font=("Verdana", 8))

labelComentarios = Label(frameSuperior, text="Comentarios ")
labelComentarios.grid(row=5, column=0, sticky="e", padx=5, pady=5)
labelComentarios.config(font=("Verdana", 8))

#Creacion de los entries para el frame superior
entryId = Entry(frameSuperior)
entryId.grid(row=0, column=1, padx=5, pady=5)
entryId.config(font=("Verdanda", 12), justify="center", state="disabled")

entryNombre = Entry(frameSuperior)
entryNombre.grid(row=1, column=1, padx=5, pady=5)
entryNombre.config(font=("Verdanda", 12), justify="center", state="disabled")

entryApellido = Entry(frameSuperior)
entryApellido.grid(row=2, column=1, padx=5, pady=5)
entryApellido.config(font=("Verdanda", 12), justify="center", state="disabled")

entryEmail = Entry(frameSuperior)
entryEmail.grid(row=3, column=1, padx=5, pady=5)
entryEmail.config(font=("Verdanda", 12), justify="center", state="disabled")

entryPass = Entry(frameSuperior)
entryPass.grid(row=4, column=1, padx=5, pady=5)
entryPass.config(font=("Verdanda", 12), justify="center", show="*", state="disabled")

# Agregar el campo tipo Text
textComentarios = Text(frameSuperior, width=26, height=5, state="disabled")
textComentarios.grid(row=5, column=1, padx=5, pady=5)

#Agregamos la barra al campo de texto de comentario
barraVert = Scrollbar(frameSuperior, command=textComentarios.yview)
barraVert.grid(row=5, column=2, sticky="nsew")
textComentarios.config(yscrollcommand=barraVert.set)

#Creacion del frame inferior
frameInferior = Frame(root, width=400, height=60)
frameInferior.pack()

# Creacion de los botones
botonConsultar = Button(frameInferior, text="Consultar", width=10, command=lambda:consultarRegistro(entryId, entryNombre, entryApellido, entryEmail, entryPass, textComentarios, botonConsultar, botonGuardar, botonActualizar, botonEliminar))
botonConsultar.grid(row=1, column=0, padx=5, pady=5)
botonConsultar.config(font=("Verdana", 10), state="disabled")

botonGuardar = Button(frameInferior, text="Insertar", width=10, command=lambda:guardarRegistro(entryId, entryNombre, entryApellido, entryEmail, entryPass, botonGuardar, botonConsultar, botonEliminar, botonActualizar, textComentarios))
botonGuardar.grid(row=1, column=1, padx=5, pady=5)
botonGuardar.config(font=("Verdana", 10), state="disabled")

botonActualizar = Button(frameInferior, text="Actualizar", width=10, command=lambda:actualizarRegistro(entryId, entryNombre, entryApellido, entryEmail, entryPass, textComentarios, botonGuardar, botonConsultar, botonEliminar, botonActualizar))
botonActualizar.grid(row=1, column=2, padx=5, pady=5)
botonActualizar.config(font=("Verdana", 10), state="disabled")

botonEliminar = Button(frameInferior, text="Eliminar", width=10, command=lambda:eliminarRegistro(entryId, entryNombre, entryApellido, entryEmail, entryPass, botonGuardar, botonConsultar, botonEliminar, botonActualizar, textComentarios))
botonEliminar.grid(row=1, column=3, padx=5, pady=5)
botonEliminar.config(font=("Verdana", 10), state="disabled")

#Construccion de la barra de menu
menuBarra = Menu(root)
root.config(menu=menuBarra, width=300, height=300)

menuBBDD = Menu(menuBarra, tearoff=0)
menuCRUD = Menu(menuBarra, tearoff=0)
menuAyuda = Menu(menuBarra, tearoff=0)

menuBarra.add_cascade(label="Base Datos", menu=menuBBDD, font=("Verdana", 15))
menuBarra.add_cascade(label="Operaciones", menu=menuCRUD, font=("Verdana", 15))
menuBarra.add_cascade(label="Ayuda", menu=menuAyuda, font=("Verdana", 15))

#Construccion submenus
menuBBDD.add_command(label="Crear Base de Datos", command=crearBaseDatos)
menuBBDD.add_separator()
menuBBDD.add_command(label="Cerrar aplicacion", command=lambda:cerrarCampos(entryId, entryNombre, entryApellido, entryEmail, entryPass, botonGuardar, botonConsultar, botonEliminar, botonActualizar, textComentarios) )
menuBBDD.add_command(label="Salir de la aplicación", command=lambda:salirAplicacion(root))

menuCRUD.add_command(label="Insertar registro", command=lambda:insertarRegistro(entryId,entryNombre, entryApellido, entryEmail, entryPass, textComentarios, botonConsultar, botonGuardar, botonActualizar, botonEliminar))
menuCRUD.add_command(label="Leer registro", command=lambda:leerRegistro(entryId, entryNombre, entryApellido, entryEmail, entryPass, textComentarios, botonGuardar, botonConsultar, botonEliminar, botonActualizar))
menuCRUD.add_separator()
menuCRUD.add_command(label="Limpiar campos", command=lambda:limpiarCampos(entryId, entryNombre, entryApellido, entryEmail, entryPass, textComentarios, botonGuardar, botonConsultar, botonEliminar, botonActualizar))

menuAyuda.add_command(label="Licencia")
menuAyuda.add_command(label="Acerca de...")


root.mainloop()