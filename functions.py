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
    

def insertarRegistro(entryN, entryA, entryE, entryP, textCom, botonCo, botonLi, botonGu, botonCe):
    messagebox.showinfo("Información requerida", "Los campos nombre, apellido, correo electronico y contraseña son obligatrios")

    entryN.config(font=("Verdanda", 12), justify="center", state="normal")
    entryA.config(font=("Verdanda", 12), justify="center", state="normal")
    entryE.config(font=("Verdanda", 12), justify="center", state="normal")
    entryP.config(font=("Verdanda", 12), justify="center", state="normal")
    textCom.configure(state="normal")
    botonCo.config(font=("Verdana", 10), state="disabled")
    botonLi.config(font=("Verdana", 10), state="normal")
    botonGu.config(font=("Verdana", 10), state="normal")
    botonCe.config(font=("Verdana", 10), state="normal")
    
    
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
    
def cerrarCampos(entryN, entryA, entryE, entryP, btnLim, btnGua, btnCer, btnCon, txtCom):
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
    
    entryN.config(state="disabled")
    entryA.config(state="disabled")
    entryE.config(state="disabled")
    entryP.config(state="disabled")
    
    btnLim.config(state="disabled")
    btnGua.config(state="disabled")
    btnCer.config(state="disabled")
    btnCon.config(state="disabled")   
    
    txtCom.delete("1.0","end") 
    txtCom.configure(state="disabled")


