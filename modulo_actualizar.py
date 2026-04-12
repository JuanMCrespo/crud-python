# v3
# CRUD - Juan M. Crespo
# proyecto 0001
# 01/03/2026

import tkinter as tk
from tkinter import ttk, messagebox
from cliente import Clientes

class Actualizar:
    def __init__(self, app):
        self.app = app

# ==================== ACTUALIZAR ====================
    def mostrar_actualizar(self):
        """Muestra el listado para seleccionar un cliente a actualizar."""
        self.app.ocultar_frames()        
        
        for widget in self.app.frame_actualizar.winfo_children():
            widget.destroy()
        
        self.app.frame_actualizar.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.98, relheight=0.88)
        self.app.frame_actualizar.lift()
        
        self.app.frame_actualizar.rowconfigure(1, weight=1)
        self.app.frame_actualizar.columnconfigure(0, weight=1)
        self.app.frame_actualizar.columnconfigure(1, weight=0)
        
        # Título
        tk.Label(self.app.frame_actualizar, text="Actualizar Cliente",
            font=("Arial", 14, "bold"), bg="#999999").grid(row=0, column=0, columnspan=2, pady=10)
        
        # Treeview
        self.app.tabla_act = ttk.Treeview(self.app.frame_actualizar, columns=(
            "id", "tipo", "dni", "nombre", "apellido",
            "nacionalidad", "cod_postal", "telefono",
            "email", "domicilio", "cuit", "razon_social"),
            show="headings")
        
        self.app.scroll_y_act = ttk.Scrollbar(self.app.frame_actualizar, orient="vertical", command=self.app.tabla_act.yview)
        self.app.tabla_act.configure(yscrollcommand=self.app.scroll_y_act.set)
        self.app.scroll_x_act = ttk.Scrollbar(self.app.frame_actualizar, orient="horizontal", command=self.app.tabla_act.xview)
        self.app.tabla_act.configure(xscrollcommand=self.app.scroll_x_act.set)
        
        for col, w in [("id",30),("tipo",80),("dni",80),("nombre",80),("apellido",80),
                       ("nacionalidad",80),("cod_postal",60),("telefono",80),
                       ("email",130),("domicilio",130),("cuit",90),("razon_social",200)]:
            self.app.tabla_act.heading(col, text=col.replace("_"," ").title())
            self.app.tabla_act.column(col, width=w)
        
        # actualizar tabla y scroll
        self.app.tabla_act.grid(row=1, column=0, sticky="nsew", padx=(20,0), pady=(0))
        self.app.scroll_y_act.grid(row=1, column=1, sticky="ns", padx=(0,20), pady=(0))
        self.app.scroll_x_act.grid(row=2, column=0, sticky="ew", padx=(20,0), pady=(0))
        
        # Cargar todos los clientes
        clientes = Clientes.listar()
        if clientes:
            for c in clientes:
                self.app.tabla_act.insert("", "end", values=c)
        
        tk.Label(self.app.frame_actualizar, text="Seleccioná un cliente para editar",
            bg="#999999", font=("Arial", 10, "italic")).grid(row=3, column=0, columnspan=2, pady=20)
        
        self.app.tabla_act.bind("<<TreeviewSelect>>", self.cargar_cliente_actualizar)
        
        tk.Button(self.app.frame_actualizar, text="Salir",
            command=self.app.frame_actualizar.place_forget).place(relx=0.99, rely=0.98, anchor="se")


    def cargar_cliente_actualizar(self, event):
        """Carga los datos del cliente seleccionado en un formulario flotante."""
        seleccion = self.app.tabla_act.selection()
        if not seleccion:
            return
        
        valores = self.app.tabla_act.item(seleccion[0])["values"]
        # valores: [id, tipo, dni, nombre, apellido, nacionalidad, cod_postal, telefono, email, domicilio, cuit, razon_social]
        
        # Frame flotante para editar
        self.app.frame_editar = tk.Frame(self.app.frame_derecho, bg="#999999",
            width=550, height=580, relief="raised", bd=2)
        self.app.frame_editar.place(relx=0.5, rely=0.5, anchor="center")
        self.app.frame_editar.grid_propagate(False)
        self.app.frame_editar.lift()
        
        tk.Label(self.app.frame_editar, text="Editar Cliente",
            font=("Arial", 14, "bold"), bg="#999999").grid(row=0, column=0, columnspan=2, pady=10)
        
        # Campos con datos cargados
        campos = [
            ("Tipo cliente:", valores[1]),
            ("DNI:", valores[2]),
            ("Nombre:", valores[3]),
            ("Apellido:", valores[4]),
            ("Nacionalidad:", valores[5]),
            ("Cod. Postal:", valores[6]),
            ("Teléfono:", valores[7]),
            ("Email:", valores[8]),
            ("Domicilio:", valores[9]),
        ]
        
        self.app.entries_editar = {}
        
        # Combobox para tipo
        tk.Label(self.app.frame_editar, text="Tipo cliente:", bg="#999999").grid(row=1, column=0, padx=10, pady=4, sticky="e")
        self.app.combo_tipo_editar = ttk.Combobox(self.app.frame_editar, values=["Particular", "Empresa"], state="readonly", width=20)
        self.app.combo_tipo_editar.set(valores[1])
        self.app.combo_tipo_editar.grid(row=1, column=1, padx=10, pady=4)
        
        # Entradas
        nombres_entry = ["dni", "nombre", "apellido", "nacionalidad", "cod_postal", "telefono", "email", "domicilio"]
        labels = ["DNI:", "Nombre:", "Apellido:", "Nacionalidad:", "Cod. Postal:", "Teléfono:", "Email:", "Domicilio:"]
        
        for i, (label, nombre, valor) in enumerate(zip(labels, nombres_entry, valores[2:10]), start=2):
            tk.Label(self.app.frame_editar, text=label, bg="#999999").grid(row=i, column=0, padx=10, pady=4, sticky="e")
            entry = tk.Entry(self.app.frame_editar, width=22)
            entry.insert(0, valor if valor else "")
            entry.grid(row=i, column=1, padx=10, pady=4)
            self.app.entries_editar[nombre] = entry
        
        # CUIT
        tk.Label(self.app.frame_editar, text="CUIT:", bg="#999999").grid(row=10, column=0, padx=10, pady=4, sticky="e")
        self.app.entry_cuit_editar = tk.Entry(self.app.frame_editar, width=22)
        self.app.entry_cuit_editar.insert(0, valores[10] if valores[10] and valores[10] != "None" else "")
        self.app.entry_cuit_editar.grid(row=10, column=1, padx=10, pady=4)
        
        # Razon Social
        tk.Label(self.app.frame_editar, text="Razón Social:", bg="#999999").grid(row=11, column=0, padx=10, pady=4, sticky="e")
        self.app.entry_razon_editar = tk.Entry(self.app.frame_editar, width=22)
        self.app.entry_razon_editar.insert(0, valores[11] if valores[11] and valores[11] != "None" else "")
        self.app.entry_razon_editar.grid(row=11, column=1, padx=10, pady=4)
        
        # Guardar el id para usarlo al actualizar
        self.app.id_cliente_editar = valores[0]
        
        # Botones
        frame_btn = tk.Frame(self.app.frame_editar, bg="#999999")
        frame_btn.grid(row=12, column=0, columnspan=2, pady=10)
        
        tk.Button(frame_btn, text="Guardar", command=self.ejecutar_actualizar).pack(side="left", padx=10)
        tk.Button(frame_btn, text="Cancelar", command=self.app.frame_editar.destroy).pack(side="left", padx=10)


    def ejecutar_actualizar(self):
        """Toma los datos del formulario de edición y llama al método actualizar."""
        
        tipo = self.app.combo_tipo_editar.get()
        dni = self.app.entries_editar["dni"].get()
        nombre = self.app.entries_editar["nombre"].get()
        apellido = self.app.entries_editar["apellido"].get()
        nacionalidad = self.app.entries_editar["nacionalidad"].get()
        cod_postal = self.app.entries_editar["cod_postal"].get()
        telefono = self.app.entries_editar["telefono"].get()
        email = self.app.entries_editar["email"].get()
        domicilio = self.app.entries_editar["domicilio"].get()
        cuit = self.app.entry_cuit_editar.get() or None
        razon_social = self.app.entry_razon_editar.get() or None
        
        # Validaciones
        if not tipo:
            messagebox.showwarning("Atención", "El tipo de cliente es obligatorio")
            return
        if not dni:
            messagebox.showwarning("Atención", "El DNI es obligatorio")
            return
        if not dni.isdigit():
            messagebox.showwarning("Atención", "El DNI debe contener solo números")
            return
        if not nombre:
            messagebox.showwarning("Atención", "El nombre es obligatorio")
            return
        if not apellido:
            messagebox.showwarning("Atención", "El apellido es obligatorio")
            return
        if tipo == "Empresa" and not cuit:
            messagebox.showwarning("Atención", "El CUIT es obligatorio para empresas")
            return
        if tipo == "Empresa" and not razon_social:
            messagebox.showwarning("Atención", "La razón social es obligatoria para empresas")
            return
        
        Clientes.actualizar_completo(self.app.id_cliente_editar, tipo, dni, nombre, apellido,
                            nacionalidad, cod_postal, telefono, email, domicilio, cuit, razon_social)
        
        messagebox.showinfo("Éxito", "Cliente actualizado exitosamente")
        self.frame_editar.destroy()
        self.mostrar_actualizar()  # refresca el listado
