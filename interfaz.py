# v3
# CRUD - Juan M. Crespo
# proyecto 0001
# 23/02/2026

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from cliente import Clientes
from modulo_eliminar import Eliminar
from modulo_actualizar import Actualizar
from modulo_buscar import Buscar
from modulo_listar import Listar
from modulo_agregar import Agregar
import platform

#CLASE BASE

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("ABM Clientes")
        self.ventana1.geometry("800x600")
        self.eliminar = Eliminar(self)
        self.actualizar = Actualizar(self)
        self.buscar = Buscar(self)
        self.listar = Listar(self)
        self.agregar = Agregar(self)
        
        
        if platform.system() == "Windows":
            self.ventana1.state("zoomed")
        else:
            self.ventana1.attributes("-zoomed", True)
               
# Frame Titulo - arriba
        self.frame_titulo = tk.Frame(self.ventana1, bg="#373C4F", height=50)
        self.frame_titulo.pack(side="top", fill="x")
        
        self.label_titulo = tk.Label(self.frame_titulo, text="Gestión de Clientes", 
            bg="#373C4F", fg="#F5E6E6", font=("Arial", 24))
        self.label_titulo.pack(pady=10)
        
# Frame izquierdo - botones       
        self.frame_izquierdo = tk.Frame(self.ventana1, bg="#CCC0C0", width=200)
        self.frame_izquierdo.pack(side="left", fill="y")

        self.espacio = tk.Label(self.frame_izquierdo, bg="#CCC0C0")
        self.espacio.grid(column=0, row=0, pady=0)

        self.boton1=tk.Button(self.frame_izquierdo, text="Agregar", width=15, command=self.agregar.agregar_formulario)
        self.boton1.grid(column=0, row=1, padx=10, pady=10)

        self.boton2=tk.Button(self.frame_izquierdo, text="Listado Clientes", width=15, command=self.listar.listar_clientes)
        self.boton2.grid(column=0, row=2, padx=10, pady=10)
        
        self.boton3=tk.Button(self.frame_izquierdo, text="Buscar", width=15, command=self.buscar.buscar_clientes)
        self.boton3.grid(column=0, row=3, padx=10, pady=10)
        
        self.boton4=tk.Button(self.frame_izquierdo, text="Actualizar", width=15, command=self.actualizar.mostrar_actualizar)
        self.boton4.grid(column=0, row=4, padx=10, pady=10)
        
        self.boton5=tk.Button(self.frame_izquierdo, text="Eliminar", width=15, command=self.eliminar.mostrar_eliminar)
        self.boton5.grid(column=0, row=5, padx=10, pady=10)
        
# Espaciador
        self.espacio2 = tk.Label(self.frame_izquierdo, bg="#CCC0C0")
        self.espacio2.grid(column=0, row=6, pady=120)
        self.frame_izquierdo.rowconfigure(6, weight=1)

                
# Frame derecho - contenido con imagen
        self.frame_derecho = tk.Frame(self.ventana1, bg="white")
        self.frame_derecho.pack(side="right", fill="both", expand=True)
        
# Imagen
        self.imagen_original = Image.open("imagen_python.jpg")
        self.label_imagen = tk.Label(self.frame_derecho)
        self.label_imagen.place(x=0, y=0, relwidth=1, relheight=1)
        self.frame_derecho.bind("<Configure>", self.ajustar_imagen)
        
# Frame Formulario agregar clientes
        self.frame_formulario = tk.Frame(self.frame_derecho, bg="#999999", 
            width=550, height=550, relief="raised", bd=2)
        
# Frame Formulario listar clientes
        self.frame_listado = tk.Frame(self.frame_derecho, bg="#999999", relief="raised", bd=2)
        
# Frame actualizar clientes
        self.frame_actualizar = tk.Frame(self.frame_derecho, bg="#999999",
            width=550, height=550, relief="raised", bd=2)
        
# Frame Formulario buscar clientes
        self.frame_buscar = tk.Frame(self.frame_derecho, bg="#999999", relief="raised", bd=2)
        
# Frame eliminar clientes
        self.frame_eliminar = tk.Frame(self.frame_derecho, bg="#999999", relief="raised", bd=2)
        
# Boton Salir de la aplicación
        self.boton_salir_app = tk.Button(self.frame_izquierdo, text="Salir", 
            width=15, command=self.confirmar_salir)
        self.boton_salir_app.grid(column=0, row=7, padx=10, pady=10)

# Salir con escape
        

        
#Loop ventana
        self.ventana1.bind("<Escape>", lambda event: self.ocultar_frames())
        self.ventana1.mainloop()

    def ajustar_imagen(self, event):
        """
        Redimensiona la imagen de fondo cuando el frame cambia de tamaño.
        Se ejecuta automáticamente cada vez que el frame cambia de tamaño.
        """
        imagen_redimensionada = self.imagen_original.resize(
            (event.width, event.height), Image.LANCZOS)
        self.imagen = ImageTk.PhotoImage(imagen_redimensionada)
        self.label_imagen.config(image=self.imagen)

    def confirmar_salir(self):
        """Muestra un cartel de confirmación antes de cerrar la aplicación."""
        respuesta = messagebox.askyesno("Salir", "¿Desea salir de la aplicación?")
        if respuesta:
            self.ventana1.destroy()
    
    def ocultar_frames(self):
        self.frame_formulario.place_forget()
        self.frame_listado.place_forget()
        self.frame_actualizar.place_forget()
        self.frame_buscar.place_forget()
        self.frame_eliminar.place_forget()

