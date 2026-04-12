# v3
# CRUD - Juan M. Crespo
# proyecto 0001
# 01/03/2026       
        
import tkinter as tk
from tkinter import ttk, messagebox
from cliente import Clientes


class Buscar:
    def __init__(self, app):
        self.app = app

# ==================== Buscar ====================
    def buscar_clientes(self):
        """Muestra busqueda de clientes"""
        self.app.ocultar_frames()        
        
        for widget in self.app.frame_buscar.winfo_children():
            widget.destroy()
        
        self.app.frame_buscar.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.98, relheight=0.78)

        self.app.frame_buscar.lift()
        
        # Configurar expansión
        self.app.frame_buscar.rowconfigure(3, weight=1)  # la fila del Treeview absorbe el espacio
        self.app.frame_buscar.columnconfigure(0, weight=1)
        self.app.frame_buscar.columnconfigure(1, weight=0)
        
        # Título
        self.app.label_titulo_list = tk.Label(self.app.frame_buscar, text="Buscar clientes",
            font=("Arial", 14, "bold"), bg="#999999")
        self.app.label_titulo_list.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Frame para campo y boton centrados
        self.app.frame_busqueda = tk.Frame(self.app.frame_buscar, bg="#999999")
        self.app.frame_busqueda.grid(row=1, column=0, columnspan=2, pady=10)

        # Campo Busqueda
        self.app.entry_busqueda = tk.Entry(self.app.frame_busqueda, width=50, font=("Arial", 12))
        self.app.entry_busqueda.pack(pady=5)

        # Boton Buscar
        self.app.boton_buscar = tk.Button(self.app.frame_busqueda, text="Buscar", width=53, command=self.encontrar_cliente)
        self.app.boton_buscar.pack(pady=5)
     
      
        # Treeview
        self.app.tabla = ttk.Treeview(self.app.frame_buscar, columns=(
            "id", "tipo", "dni", "nombre", "apellido",
            "nacionalidad", "cod_postal", "telefono",
            "email", "domicilio", "cuit", "razon_social"),
            show="headings")
        
        # Scrollbar vertical
        self.app.scroll_y = ttk.Scrollbar(self.app.frame_buscar, orient="vertical", command=self.app.tabla.yview)
        self.app.tabla.configure(yscrollcommand=self.app.scroll_y.set)
        
        # Scrollbar horizontal
        self.app.scroll_x = ttk.Scrollbar(self.app.frame_buscar, orient="horizontal", command=self.app.tabla.xview)
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
        self.app.tabla.column("razon_social", width=120)
        
        # Ubicar tabla y scrollbars de buscar
        self.app.tabla.grid(row=3, column=0, sticky="nsew", padx=(20, 0), pady=0)
        self.app.scroll_y.grid(row=3, column=1, sticky="ns", padx=(0, 20), pady=0)
        self.app.scroll_x.grid(row=4, column=0, sticky="ew", padx=(20, 0), pady=0)

        tk.Label(self.app.frame_buscar, text="",
            bg="#999999", font=("Arial", 10, "italic")).grid(row=5, column=0, columnspan=2, pady=20)

        #Boton Salir
        self.app.boton_salir = tk.Button(self.app.frame_buscar, text="Salir",
            command=self.app.frame_buscar.place_forget)
        self.app.boton_salir.place(relx=0.99, rely=0.98, anchor="se")

    def encontrar_cliente(self):
        valor = self.app.entry_busqueda.get()
        
        if not valor:
            messagebox.showwarning("Atención", "Ingrese un valor para buscar")
            return
        
        # Buscar en todos los campos
        resultados = []
        campos = ["tipo_cliente", "dni", "nombre", "apellido", 
                  "nacionalidad", "telefono", "email", "domicilio", "cuit", "razon_social"]
        
        ids_encontrados = set()  # para evitar duplicados
        for campo in campos:
            clientes = Clientes.buscar(campo, valor)
            if clientes:
                for c in clientes:
                    if c[0] not in ids_encontrados:
                        resultados.append(c)
                        ids_encontrados.add(c[0])
        
        # Limpiar tabla y cargar resultados
        for item in self.app.tabla.get_children():
            self.app.tabla.delete(item)
        
        if resultados:
            for c in resultados:
                self.app.tabla.insert("", "end", values=c)
        else:
            messagebox.showinfo("Búsqueda", "No se encontraron clientes")