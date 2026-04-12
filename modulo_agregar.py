# v3
# CRUD - Juan M. Crespo
# proyecto 0001
# 01/03/2026       
        
import tkinter as tk
from tkinter import ttk, messagebox
from cliente import Clientes


class Agregar:
    def __init__(self, app):
        self.app = app

    # ==================== AGREGAR ====================
    def cambiar_tipo(self, event):
        """Habilita o deshabilita campos según el tipo de cliente."""      
        
        if self.app.combo_tipo.get() == "Empresa":
            self.app.entry_cuit.config(state="normal")
            self.app.entry_razon_social.config(state="normal")
        else:
            self.app.entry_cuit.config(state="disabled")
            self.app.entry_razon_social.config(state="disabled")    
    
    def agregar_formulario(self):
        """Muestra el formulario para cargar clientes dentro del frame derecho."""
        self.app.ocultar_frames()      
        
        for widget in self.app.frame_formulario.winfo_children():
            widget.destroy()
        
        # Mantener tamaño fijo
        self.app.frame_formulario.grid_propagate(False)
        
        # Mostrar el Formulario
        self.app.frame_formulario.place(relx=0.5, rely=0.5, anchor="center")
        self.app.frame_formulario.lift()  # lo trae al frente
        
        # Título
        self.app.label_titulo_form = tk.Label(self.app.frame_formulario, text="Agregar Cliente", 
            font=("Arial", 14, "bold"), bg="#999999")
        self.app.label_titulo_form.grid(row=0, column=0, columnspan=2, pady=10)
    
        # Tipo cliente
        self.app.label_tipo = tk.Label(self.app.frame_formulario, text="Tipo cliente:", bg="#999999")
        self.app.label_tipo.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.app.combo_tipo = ttk.Combobox(self.app.frame_formulario, values=["Particular", "Empresa"], state="readonly", width=20)
        self.app.combo_tipo.grid(row=1, column=1, padx=10, pady=5)
        self.app.combo_tipo.bind("<<ComboboxSelected>>", self.cambiar_tipo)

    
        # DNI
        self.app.label_dni = tk.Label(self.app.frame_formulario, text="DNI:", bg="#999999")
        self.app.label_dni.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.app.entry_dni = tk.Entry(self.app.frame_formulario, width=22)
        self.app.entry_dni.grid(row=2, column=1, padx=10, pady=5)
        
        # Nombre
        self.app.label_nombre = tk.Label(self.app.frame_formulario, text="Nombre:", bg="#999999")
        self.app.label_nombre.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.app.entry_nombre = tk.Entry(self.app.frame_formulario, width=22)
        self.app.entry_nombre.grid(row=3, column=1, padx=10, pady=5)
        
        # Apellido
        self.app.label_apellido = tk.Label(self.app.frame_formulario, text="Apellido:", bg="#999999")
        self.app.label_apellido.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.app.entry_apellido = tk.Entry(self.app.frame_formulario, width=22)
        self.app.entry_apellido.grid(row=4, column=1, padx=10, pady=5)
        
        # Nacionalidad
        self.app.label_nacionalidad = tk.Label(self.app.frame_formulario, text="Nacionalidad:", bg="#999999")
        self.app.label_nacionalidad.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.app.entry_nacionalidad = tk.Entry(self.app.frame_formulario, width=22)
        self.app.entry_nacionalidad.grid(row=5, column=1, padx=10, pady=5)
        
        # Cod. Postal
        self.app.label_cod_postal = tk.Label(self.app.frame_formulario, text="Cod. Postal:", bg="#999999")
        self.app.label_cod_postal.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.app.entry_cod_postal = tk.Entry(self.app.frame_formulario, width=22)
        self.app.entry_cod_postal.grid(row=6, column=1, padx=10, pady=5)
        
        # Telefono
        self.app.label_telefono = tk.Label(self.app.frame_formulario, text="Teléfono:", bg="#999999")
        self.app.label_telefono.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        self.app.entry_telefono = tk.Entry(self.app.frame_formulario, width=22)
        self.app.entry_telefono.grid(row=7, column=1, padx=10, pady=5)
        
        # Email
        self.app.label_email = tk.Label(self.app.frame_formulario, text="Email:", bg="#999999")
        self.app.label_email.grid(row=8, column=0, padx=10, pady=5, sticky="e")
        self.app.entry_email = tk.Entry(self.app.frame_formulario, width=22)
        self.app.entry_email.grid(row=8, column=1, padx=10, pady=5)
        
        # Domicilio
        self.app.label_domicilio = tk.Label(self.app.frame_formulario, text="Domicilio:", bg="#999999")
        self.app.label_domicilio.grid(row=9, column=0, padx=10, pady=5, sticky="e")
        self.app.entry_domicilio = tk.Entry(self.app.frame_formulario, width=22)
        self.app.entry_domicilio.grid(row=9, column=1, padx=10, pady=5)
        
        # CUIT
        self.app.label_cuit = tk.Label(self.app.frame_formulario, text="CUIT:", bg="#999999")
        self.app.label_cuit.grid(row=10, column=0, padx=10, pady=5, sticky="e")
        self.app.entry_cuit = tk.Entry(self.app.frame_formulario, width=22, state="disabled")
        self.app.entry_cuit.grid(row=10, column=1, padx=10, pady=5)
        
        
        # Razon Social
        self.app.label_razon_social = tk.Label(self.app.frame_formulario, text="Razón Social:", bg="#999999")
        self.app.label_razon_social.grid(row=11, column=0, padx=10, pady=5, sticky="e")
        self.app.entry_razon_social = tk.Entry(self.app.frame_formulario, width=22, state="disabled")
        self.app.entry_razon_social.grid(row=11, column=1, padx=10, pady=5)

        #---------------------------------------------------------------------------------------------
        
        # Frame para los botones
        self.app.frame_botones = tk.Frame(self.app.frame_formulario, bg="#999999")
        self.app.frame_botones.grid(row=12, column=1, columnspan=2, pady=15)
        
        # Boton Guardar
        self.app.boton_guardar = tk.Button(self.app.frame_botones, text="Guardar", command=self.guardar_cliente)
        self.app.boton_guardar.pack(side="left", padx=10)
        
        # Boton Limpiar
        self.app.boton_limpiar = tk.Button(self.app.frame_botones, text="Limpiar", command=self.limpiar)
        self.app.boton_limpiar.pack(side="left", padx=10)
        
        # Boton Salir
        self.app.boton_salir = tk.Button(self.app.frame_formulario, text="Salir", 
            command=self.app.frame_formulario.place_forget)
        self.app.boton_salir.place(relx=0.97, rely=0.97, anchor="se")
    
    # ==================== LIMPIAR FORM ===============
    def limpiar(self):
        """Limpia los registros del formulario"""
        self.app.combo_tipo.set("")
        self.app.entry_dni.delete(0, tk.END)
        self.app.entry_nombre.delete(0, tk.END)
        self.app.entry_apellido.delete(0, tk.END)
        self.app.entry_nacionalidad.delete(0, tk.END)
        self.app.entry_cod_postal.delete(0, tk.END)
        self.app.entry_telefono.delete(0, tk.END)
        self.app.entry_email.delete(0, tk.END)
        self.app.entry_domicilio.delete(0, tk.END)

        # Limpiar y deshabilitar CUIT y Razon Social
        self.app.entry_cuit.config(state="normal")
        self.app.entry_cuit.delete(0, tk.END)
        self.app.entry_cuit.config(state="disabled")
    
        self.app.entry_razon_social.config(state="normal")
        self.app.entry_razon_social.delete(0, tk.END)
        self.app.entry_razon_social.config(state="disabled")

    # ==================== AGREGAR ====================
    def guardar_cliente(self):
        """Toma los datos del formulario, valida y llama al método insertar."""
    
        # Obtener datos
        tipo = self.app.combo_tipo.get()
        dni = self.app.entry_dni.get()
        nombre = self.app.entry_nombre.get()
        apellido = self.app.entry_apellido.get()
        nacionalidad = self.app.entry_nacionalidad.get()
        cod_postal = self.app.entry_cod_postal.get()
        telefono = self.app.entry_telefono.get()
        email = self.app.entry_email.get()
        domicilio = self.app.entry_domicilio.get()
        cuit = self.app.entry_cuit.get() or None
        razon_social = self.app.entry_razon_social.get() or None
        
        # Validaciones
        if not tipo:
            messagebox.showwarning("Atención", "El tipo de cliente es obligatorio")
            return
        if not dni:
            messagebox.showwarning("Atención", "El DNI es obligatorio")
            return
        if Clientes.verificar_dni(dni):
            messagebox.showwarning("Atención", "Dni ya existe en la base de datos")
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
        if Clientes.verificar_email(email):
            messagebox.showwarning("Atención", "El email ya existe en la base de datos")
            return
        if tipo == "Empresa" and not cuit:
            messagebox.showwarning("Atención", "El CUIT es obligatorio para empresas")
            return
        if tipo == "Empresa" and not razon_social:
            messagebox.showwarning("Atención", "La razón social es obligatoria para empresas")
            return
        

        
        # Insertar
        cliente = Clientes(tipo, dni, nombre, apellido, nacionalidad,
                           cod_postal, telefono, email, domicilio, cuit, razon_social)
        
        cliente.insertar()
        messagebox.showinfo("Éxito", "Cliente ingresado exitosamente")
        self.limpiar()