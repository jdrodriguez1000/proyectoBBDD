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
    
        

