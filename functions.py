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
    

def insertarRegistro(entryI, entryN, entryA, entryE, entryP, textCom, btnCon, btnGua, btnAct, btnEli):
    messagebox.showinfo("Información requerida", "Los campos nombre, apellido, correo electronico y contraseña son obligatrios")

    entryI.config(state="disabled")
    entryN.config(state="normal")
    entryA.config(state="normal")
    entryE.config(state="normal")
    entryP.config(state="normal")
    textCom.configure(state="normal")
    
    btnCon.config(state="disabled")
    btnGua.config(state="normal")
    btnAct.config(state="disabled")
    btnEli.config(state="disabled")
    
    
def limpiarCampos(entryI, entryN, entryA, entryE, entryP, textCom):
    valor = entryI.get()
    if valor !="":
        entryI.delete(0,len(valor))
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
 
    
def cerrarCampos(entryI,entryN, entryA, entryE, entryP, btnGua, btnCon, btnEli, btnAct, txtCom):
    valor = entryI.get()
    if valor !="":
        entryI.delete(0,len(valor))
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
    
    entryI.config(state="disabled")
    entryN.config(state="disabled")
    entryA.config(state="disabled")
    entryE.config(state="disabled")
    entryP.config(state="disabled")
    
    btnGua.config(state="disabled")
    btnCon.config(state="disabled")   
    btnEli.config(state="disabled")
    btnAct.config(state="disabled") 
    
    txtCom.delete("1.0","end") 
    txtCom.configure(state="disabled")
 
    
def leerRegistro(entryI, entryN, entryA, entryE, entryP, txtCom, btnGua, btnCon, btnEli, btnAct):
    messagebox.showinfo("Lectura Registro", "Para leer un registro se requiere ingresar el Id del usuario y presionar el boton consultar")
    
    entryI.config(state="normal")
    entryN.config(state="disabled")
    entryA.config(state="disabled")
    entryE.config(state="disabled")
    entryP.config(state="disabled")

    txtCom.configure(state="disabled")
    
    btnGua.config(state="disabled")
    btnCon.config(state="normal")
    btnEli.config(state="disabled")
    btnAct.config(state="disabled")
    

def guardarRegistro(entryI, entryN, entryA, entryE, entryP, texCom):
    nombre = entryN.get()
    apellido = entryA.get()
    email = entryE.get()
    passw = entryP.get()
    comentarios = texCom.get("1.0", "end")
    lista_datos = [(nombre, apellido, email, passw, comentarios)]
    if(nombre =="" or apellido=="" or email=="" or passw==""):
        messagebox.showerror("Información obligatoria", "Los campos nombre, apellido, correo electrónico y contraseña son obligatorios")
    else:
        conexionBD = sqlite3.connect("BD_Usuarios")
        cursorBD = conexionBD.cursor()
        
        cursorBD.executemany("insert into tblUsuarios values (NULL, ?, ?, ?, ?, ?)", lista_datos)
        conexionBD.commit()
        conexionBD.close() 
        limpiarCampos(entryI, entryN, entryA, entryE, entryP, texCom)
        messagebox.showinfo("Registro guardado", "El registro fue guardado exitosamente")


    


