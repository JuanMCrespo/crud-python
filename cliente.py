# v3
# CRUD - Juan M. Crespo
# proyecto 0001
# 23/02/2026

import sqlite3
from conexion import Conexion

class Clientes:
    ### Atributos
    def __init__(self, tipo_cliente, dni, nombre, apellido,
                nacionalidad, cod_postal, telefono, email,
                domicilio, cuit, razon_social):
    
        self.tipo_cliente = tipo_cliente
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.cod_postal = cod_postal
        self.telefono = telefono
        self.email = email
        self.domicilio = domicilio
        self.cuit = cuit
        self.razon_social = razon_social
    
    ### Metodos
    
# C -- Crear
    def insertar(self):
        try:
            conexion = Conexion.conexionBD()
            cursor = conexion.cursor()
            
            cursor.execute("""
                INSERT INTO cliente (tipo_cliente, dni, nombre, apellido,
                nacionalidad, cod_postal, telefono, email,
                domicilio, cuit, razon_social)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (self.tipo_cliente, self.dni, self.nombre, self.apellido, self.nacionalidad,
                          self.cod_postal, self.telefono, self.email, self.domicilio, self.cuit, self.razon_social
                           ))
            
            conexion.commit()
            
        except sqlite3.Error as error:
            print(f"Error al insertar cliente {error}")
        
        finally:
            conexion.close()
   
# R -- Leer
    @staticmethod
    def listar():
        try:
            conexion = Conexion.conexionBD()
            cursor = conexion.cursor()
            
            cursor.execute("SELECT * FROM cliente")
            
            clientes = cursor.fetchall()
            
            return clientes
            
        except sqlite3.Error as error:
            print(f"Error al listar cliente: {error}")
                    
        finally:
            conexion.close()   
    
# S -- Buscar
    @staticmethod
    def buscar(campo, valor):
        try:
            conexion = Conexion.conexionBD()
            cursor = conexion.cursor()
            cursor.execute(f"SELECT * FROM cliente WHERE {campo} LIKE ?", (f"%{valor}%",))
            
            clientes = cursor.fetchall()
            
            if clientes:
                return clientes
            else:
                print("Cliente inexistente")
                           
            
        except sqlite3.Error as error:
            print(f"Error al buscar cliente: {error}")
            
        finally:
            conexion.close()    
    
# U -- Actualizar
    @staticmethod
    def actualizar_completo(id_cliente, tipo_cliente, dni, nombre, apellido,
                            nacionalidad, cod_postal, telefono, email,
                            domicilio, cuit, razon_social):
        try:
            conexion = Conexion.conexionBD()
            cursor = conexion.cursor()
            cursor.execute("""
                UPDATE cliente SET tipo_cliente=?, dni=?, nombre=?, apellido=?,
                nacionalidad=?, cod_postal=?, telefono=?, email=?,
                domicilio=?, cuit=?, razon_social=?
                WHERE id_cliente=?
            """, (tipo_cliente, dni, nombre, apellido, nacionalidad,
                  cod_postal, telefono, email, domicilio, cuit, razon_social, id_cliente))
            conexion.commit()
        except sqlite3.Error as error:
            print(f"Error al actualizar: {error}")
        finally:
            conexion.close()
            
# D -- Eliminar
    @staticmethod
    def eliminar_por_id(id_cliente):
        try:
            conexion = Conexion.conexionBD()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM cliente WHERE id_cliente = ?", (id_cliente,))
            conexion.commit()
        except sqlite3.Error as error:
            print(f"Error al eliminar: {error}")
        finally:
            conexion.close()
            
# Verificar si DNI ya existe
    @staticmethod
    def verificar_dni(dni):
        try:
            conexion = Conexion.conexionBD()
            cursor = conexion.cursor()
            cursor.execute("SELECT 1 FROM cliente WHERE dni = ?" , (dni,))
            resultado = cursor.fetchone()
            return resultado is not None
        except sqlite3.Error as error:
            print(f"Error al verificar: {error}")
        finally:
            conexion.close()
    
# Verificar si email ya existe
    @staticmethod
    def verificar_email(email):
        try:
            conexion = Conexion.conexionBD()
            cursor = conexion.cursor()
            cursor.execute("SELECT 1 FROM cliente WHERE email = ?" , (email,))
            resultado = cursor.fetchone()
            return resultado is not None
        except sqlite3.Error as error:
            print(f"Error al verificar: {error}")
        finally:
            conexion.close()

