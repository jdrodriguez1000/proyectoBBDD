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
    

def insertarRegistro(entryI, entryN, entryA, entryE, entryP, txtCom, btnCon, btnGua, btnAct, btnEli):
    messagebox.showinfo("Información requerida", "Los campos nombre, apellido, correo electronico y contraseña son obligatrios")

    limpiarCampos(entryI, entryN, entryA, entryE, entryP, txtCom, btnGua, btnCon, btnEli, btnAct)
    
    entryI.config(state="disabled")
    entryN.config(state="normal")
    entryA.config(state="normal")
    entryE.config(state="normal")
    entryP.config(state="normal")
    txtCom.configure(state="normal")
    
    btnCon.config(state="disabled")
    btnGua.config(state="normal")
    btnAct.config(state="disabled")
    btnEli.config(state="disabled")
    
    
def limpiarCampos(entryI, entryN, entryA, entryE, entryP, txtCom, btnGua, btnCon, btnEli, btnAct):
    entryI.config(state="normal")
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
    txtCom.delete("1.0","end")
    
    entryI.config(state="disabled")
    entryN.config(state="disabled")
    entryA.config(state="disabled")
    entryE.config(state="disabled")
    entryP.config(state="disabled")
    
    btnGua.config(state="disabled")
    btnCon.config(state="disabled")   
    btnEli.config(state="disabled")
    btnAct.config(state="disabled")
    
    txtCom.configure(state="disabled")
 
    
def cerrarCampos(entryI,entryN, entryA, entryE, entryP, btnGua, btnCon, btnEli, btnAct, txtCom):
    entryI.config(state="normal")
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
    
    limpiarCampos(entryI, entryN, entryA, entryE, entryP, txtCom, btnGua, btnCon, btnEli, btnAct)
    
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
    

def guardarRegistro(entryI, entryN, entryA, entryE, entryP, btnGua, btnCon, btnEli, btnAct, txtCom):
    nombre = entryN.get()
    apellido = entryA.get()
    email = entryE.get()
    passw = entryP.get()
    comentarios = txtCom.get("1.0", "end")
    lista_datos = [(nombre, apellido, email, passw, comentarios)]
    if(nombre =="" or apellido=="" or email=="" or passw==""):
        messagebox.showerror("Información obligatoria", "Los campos nombre, apellido, correo electrónico y contraseña son obligatorios")
    else:
        conexionBD = sqlite3.connect("BD_Usuarios")
        cursorBD = conexionBD.cursor()
        
        cursorBD.executemany("insert into tblUsuarios values (NULL, ?, ?, ?, ?, ?)", lista_datos)
        conexionBD.commit()
        conexionBD.close() 
        
        messagebox.showinfo("Registro guardado", "El registro fue guardado exitosamente")
        cerrarCampos(entryI,entryN, entryA, entryE, entryP, btnGua, btnCon, btnEli, btnAct, txtCom) 


def consultarRegistro(entryI, entryN, entryA, entryE, entryP, txtCom, btnCon, btnGua, btnAct, btnEli):
    valor = entryI.get()
    if valor == "":
        messagebox.showerror("Información obligatoria", "El campo ID Usuario es obligatorio")
    else:
        try:
            idusuario = int(valor)
            sqlConsulta="select * from tblUsuarios where idUsuario="
            sqlConsulta = sqlConsulta + str(idusuario)
            print(sqlConsulta)
            conexionBD = sqlite3.connect("BD_Usuarios")
            cursorBD = conexionBD.cursor()
            
            cursorBD.execute(sqlConsulta)
            datosUsuario = cursorBD.fetchall()
            
            registros = (len(datosUsuario))
            if registros == 1:
                nombre = datosUsuario[0][1]
                entryN.config(state="normal")   
                entryN.insert(0, nombre)
                
                apellido = datosUsuario[0][2]
                entryA.config(state="normal")   
                entryA.insert(0, apellido)
                
                email = datosUsuario[0][3]
                entryE.config(state="normal")   
                entryE.insert(0, email)
                
                passw = datosUsuario[0][4]
                entryP.config(state="normal")   
                entryP.insert(0, passw)
                
                coment = datosUsuario[0][5]
                txtCom.configure(state="normal")   
                txtCom.insert("1.0", coment)
                
                btnCon.config(state="disabled")
                btnGua.config(state="disabled")
                btnAct.config(state="normal")
                btnEli.config(state="normal")
                entryI.config(state ="disabled")
                    
            else:
                messagebox.showerror("ID no Existe", "El ID de Usuario ingresado no está registrado en la Base de datos")
                long = entryI.get()
                if long !="":
                    entryI.delete(0,len(long)) 
            
            conexionBD.commit()
            conexionBD.close()
            
        except:
            messagebox.showerror("Información erronea", "Por favor ingrese un Id de usuario numerico y entero")
            long = entryI.get()
            if long !="":
                entryI.delete(0,len(long))    

def actualizarRegistro(entryI, entryN, entryA, entryE, entryP, txtCom, btnGua, btnCon, btnEli, btnAct):
    Id = entryI.get()
    nombre = entryN.get()
    apellido = entryA.get()
    email = entryE.get()
    passw = entryP.get()
    coment = txtCom.get("1.0", "end")
    
    lista_usuario = [(nombre, apellido, email, passw, coment, Id)]
    conexionBD = sqlite3.connect("BD_Usuarios")
    cursorBD = conexionBD.cursor()
    
    cursorBD.executemany("update tblUsuarios set nombre=?, apellido=?, correoelectronico=?, contrasena=?, comentarios=? where idUsuario=?",lista_usuario)
    
    conexionBD.commit()
    conexionBD.close() 
    messagebox.showinfo("Registro actualizado", "El registro se actualizó correctamente")
    cerrarCampos(entryI,entryN, entryA, entryE, entryP, btnGua, btnCon, btnEli, btnAct, txtCom)
    

def eliminarRegistro(entryI, entryN, entryA, entryE, entryP, btnGua, btnCon, btnEli, btnAct, txtCom):
    rpta = messagebox.askyesno("Eliminacion de usuario", "Realmente quiere eliminar de forma definitiva el usuario")
    if rpta != True:
      cerrarCampos(entryI,entryN, entryA, entryE, entryP, btnGua, btnCon, btnEli, btnAct, txtCom)  
    else:
        Id=entryI.get()
        
        conexionBD = sqlite3.connect("BD_Usuarios")
        cursorBD = conexionBD.cursor()
        
        cursorBD.execute("delete from tblUsuarios where idUsuario ="+ Id)
        
        conexionBD.commit()
        conexionBD.close()
        messagebox.showinfo("Eliminacion de usuario", "El usuario fue eliminado exitosamente")
        cerrarCampos(entryI,entryN, entryA, entryE, entryP, btnGua, btnCon, btnEli, btnAct, txtCom)  
        

    
    
   
    

