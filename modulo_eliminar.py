# v3
# CRUD - Juan M. Crespo
# proyecto 0001
# 01/03/2026

import tkinter as tk
from tkinter import ttk, messagebox
from cliente import Clientes


class Eliminar:
    def __init__(self, app):
        self.app = app

# ==================== ELIMINAR ====================
    def mostrar_eliminar(self):
        """Muestra el listado para seleccionar un cliente a eliminar."""
        self.app.ocultar_frames()        
        
        for widget in self.app.frame_eliminar.winfo_children():
            widget.destroy()
        
        self.app.frame_eliminar.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.98, relheight=0.88)
        self.app.frame_eliminar.lift()
        
        self.app.frame_eliminar.rowconfigure(1, weight=1)
        self.app.frame_eliminar.columnconfigure(0, weight=1)
        self.app.frame_eliminar.columnconfigure(1, weight=0)
        
        tk.Label(self.app.frame_eliminar, text="Eliminar Cliente",
            font=("Arial", 14, "bold"), bg="#999999").grid(row=0, column=0, columnspan=2, pady=10)
        
        self.app.tabla_eliminar = ttk.Treeview(self.app.frame_eliminar, columns=(
            "id", "tipo", "dni", "nombre", "apellido",
            "nacionalidad", "cod_postal", "telefono",
            "email", "domicilio", "cuit", "razon_social"),
            show="headings")
        
        self.app.scroll_y_eliminar = ttk.Scrollbar(self.app.frame_eliminar, orient="vertical",
                                               command=self.app.tabla_eliminar.yview)
        self.app.tabla_eliminar.configure(yscrollcommand=self.app.scroll_y_eliminar.set)
        self.app.scroll_x_eliminar = ttk.Scrollbar(self.app.frame_eliminar, orient="horizontal", command=self.app.tabla_eliminar.xview)
        self.app.tabla_eliminar.configure(xscrollcommand=self.app.scroll_x_eliminar.set)
        
        for col, w in [("id",30),("tipo",80),("dni",80),("nombre",80),("apellido",80),
                       ("nacionalidad",80),("cod_postal",60),("telefono",80),
                       ("email",130),("domicilio",130),("cuit",90),("razon_social",200)]:
            self.app.tabla_eliminar.heading(col, text=col.replace("_"," ").title())
            self.app.tabla_eliminar.column(col, width=w)
        
        self.app.tabla_eliminar.grid(row=1, column=0, sticky="nsew", padx=(20,0), pady=0)
        self.app.scroll_y_eliminar.grid(row=1, column=1, sticky="ns", padx=(0,20), pady=0)
        self.app.scroll_x_eliminar.grid(row=2, column=0, sticky="ew", padx=(20,0), pady=0)
       
        
        clientes = Clientes.listar()
        if clientes:
            for c in clientes:
                self.app.tabla_eliminar.insert("", "end", values=c)
        
        tk.Label(self.app.frame_eliminar, text="Seleccioná un cliente para eliminar",
            bg="#999999", font=("Arial", 10, "italic")).grid(row=3, column=0, columnspan=2, pady=20)
        
        self.app.tabla_eliminar.bind("<<TreeviewSelect>>", self.ejecutar_eliminar)
        
        tk.Button(self.app.frame_eliminar, text="Salir",
            command=self.app.frame_eliminar.place_forget).place(relx=0.99, rely=0.98, anchor="se")        

    def ejecutar_eliminar(self, event):
        """Confirma y elimina el cliente seleccionado."""
        seleccion = self.app.tabla_eliminar.selection()
        if not seleccion:
            return
        
        valores = self.app.tabla_eliminar.item(seleccion[0])["values"]
        id_cliente = valores[0]
        nombre = valores[3]
        apellido = valores[4]
        
        respuesta = messagebox.askyesno("Eliminar", 
            f"¿Desea eliminar a {nombre} {apellido}?")
        
        if respuesta:
            Clientes.eliminar_por_id(id_cliente)
            messagebox.showinfo("Éxito", "Cliente eliminado exitosamente")
            self.mostrar_eliminar()