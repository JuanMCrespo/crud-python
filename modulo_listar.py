# v3
# CRUD - Juan M. Crespo
# proyecto 0001
# 04/03/2026       
        
import tkinter as tk
from tkinter import ttk, messagebox
from cliente import Clientes


class Listar:
    def __init__(self, app):
        self.app = app
        
    # ==================== LISTAR ====================
    def listar_clientes(self):
        """Muestra el listado de clientes en el frame formulario"""
        self.app.ocultar_frames()
      
        for widget in self.app.frame_listado.winfo_children():
            widget.destroy()
 
        self.app.frame_listado.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.98, relheight=0.88)
        self.app.frame_listado.lift()

        # Configurar expansión
        self.app.frame_listado.rowconfigure(1, weight=1)
        self.app.frame_listado.columnconfigure(0, weight=1)
        self.app.frame_listado.columnconfigure(1, weight=0)
       
        # Título
        self.app.label_titulo_list = tk.Label(self.app.frame_listado, text="Listado de Clientes",
            font=("Arial", 14, "bold"), bg="#999999")
        self.app.label_titulo_list.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Treeview
        self.app.tabla = ttk.Treeview(self.app.frame_listado, columns=(
            "id", "tipo", "dni", "nombre", "apellido",
            "nacionalidad", "cod_postal", "telefono",
            "email", "domicilio", "cuit", "razon_social"),
            show="headings")
        
        # Scrollbar vertical
        self.app.scroll_y = ttk.Scrollbar(self.app.frame_listado, orient="vertical", command=self.app.tabla.yview)
        self.app.tabla.configure(yscrollcommand=self.app.scroll_y.set)
        
        # Scrollbar horizontal
        self.app.scroll_x = ttk.Scrollbar(self.app.frame_listado, orient="horizontal", command=self.app.tabla.xview)
        self.app.tabla.configure(xscrollcommand=self.app.scroll_x.set)
        
        # Encabezados y anchos
        self.app.tabla.heading("id", text="ID")
        self.app.tabla.column("id", width=30)
        self.app.tabla.heading("tipo", text="Tipo")
        self.app.tabla.column("tipo", width=80)
        self.app.tabla.heading("dni", text="DNI")
        self.app.tabla.column("dni", width=80)
        self.app.tabla.heading("nombre", text="Nombre")
        self.app.tabla.column("nombre", width=80)
        self.app.tabla.heading("apellido", text="Apellido")
        self.app.tabla.column("apellido", width=80)
        self.app.tabla.heading("nacionalidad", text="Nacionalidad")
        self.app.tabla.column("nacionalidad", width=80)
        self.app.tabla.heading("cod_postal", text="C.Postal")
        self.app.tabla.column("cod_postal", width=60)
        self.app.tabla.heading("telefono", text="Teléfono")
        self.app.tabla.column("telefono", width=80)
        self.app.tabla.heading("email", text="Email")
        self.app.tabla.column("email", width=130)
        self.app.tabla.heading("domicilio", text="Domicilio")
        self.app.tabla.column("domicilio", width=130)
        self.app.tabla.heading("cuit", text="CUIT")
        self.app.tabla.column("cuit", width=90)
        self.app.tabla.heading("razon_social", text="Razón Social")
        self.app.tabla.column("razon_social", width=200)
        
        # listar clientes grid tabla      
        self.app.tabla.grid(row=1, column=0, sticky="nsew", padx=(20, 0), pady=0)
        self.app.scroll_y.grid(row=1, column=1, sticky="ns", padx=(0, 20), pady=0)
        self.app.scroll_x.grid(row=2, column=0, sticky="ew", padx=(20, 0), pady=0)
        
        # Cargar datos
        clientes = Clientes.listar()
        if clientes:
            for c in clientes:
                valores_limpios = []
                for v in c:
                    if v is None:
                        valores_limpios.append("")
                    else:
                        valores_limpios.append(v)
                self.app.tabla.insert("", "end", values=tuple(valores_limpios))
        
                
        tk.Label(self.app.frame_listado, text="",
            bg="#999999", font=("Arial", 10, "italic")).grid(row=3, column=0, columnspan=2, pady=20)

        #Boton Salir
        self.app.boton_salir = tk.Button(self.app.frame_listado, text="Salir",
            command=self.app.frame_listado.place_forget)
        self.app.boton_salir.place(relx=0.99, rely=0.98, anchor="se")