from tkinter import *
from tkinter import messagebox
import sqlite3

# Funcion conectar a la base de datos
def crearBaseDatos():
    conexionBD = sqlite3.connect("BD_Usuarios")
    cursorBD = conexionBD.cursor()
    try:
        cursorBD.execute('''
                         create table tblUsuarios(
                            idUsuario integer primary key autoincrement,
                            nombre varchar(50),
                            apellido varchar(50),
                            correoelectronico varchar(50),
                            contrasena varchar(15),
                            comentarios varchar(200)
                        )
                        ''')
        messagebox.showinfo("Base de datos", "Base de datos creada exitosamente")    
    except:
        messagebox.showwarning("Base de datos", "La base de datos ya existe")    


def salirAplicacion(root):
    rpta = messagebox.askyesno("Salir aplicacion", "Desea salir de la aplicacion?")
    if rpta==True:
        conexionBD = sqlite3.connect("BD_Usuarios")
        conexionBD.close()
        root.destroy()
    

def insertarRegistro(entryNombre, entryApellido, entryEmail, entryPass, textComentarios, botonConsultar, botonLimpiar, botonGuardar, botonCerrar):
    messagebox.showinfo("Información requerida", "Los campos nombre, apellido, correo electronico y contraseña son obligatrios")

    entryNombre.config(font=("Verdanda", 12), justify="center", state="normal")
    entryApellido.config(font=("Verdanda", 12), justify="center", state="normal")
    entryEmail.config(font=("Verdanda", 12), justify="center", state="normal")
    entryPass.config(font=("Verdanda", 12), justify="center", state="normal")
    textComentarios.configure(state="normal")
    botonConsultar.config(font=("Verdana", 10), state="disabled")
    botonLimpiar.config(font=("Verdana", 10), state="normal")
    botonGuardar.config(font=("Verdana", 10), state="normal")
    botonCerrar.config(font=("Verdana", 10), state="normal")
    
    
def limpiarCampos(entryN, entryA, entryE, entryP, textCom):
    valor = entryN.get()
    if valor !="":
        entryN.delete(0,len(valor))
    valor = entryA.get()
    if valor !="":
        entryA.delete(0,len(valor))
    valor = entryE.get()
    if valor !="":
        entryE.delete(0,len(valor))
    valor = entryP.get()
    if valor !="":
        entryP.delete(0,len(valor))
    textCom.delete("1.0","end")

    


