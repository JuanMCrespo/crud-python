# v3
# CRUD - Juan M. Crespo
# proyecto 0001
# 23/02/2026

import sqlite3
from conexion import Conexion

def crear_tablas():
    
    try:
        conexion = Conexion.conexionBD()
        cursor = conexion.cursor()       
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cliente (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo_cliente TEXT NOT NULL
                CHECK (tipo_cliente IN ('Particular','Empresa')),
            dni TEXT NOT NULL UNIQUE,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            nacionalidad TEXT,
            cod_postal TEXT,
            telefono TEXT,
            email TEXT UNIQUE,
            domicilio TEXT,
            cuit TEXT UNIQUE,
            razon_social TEXT    
        );
        """)      
        
        conexion.commit()
    
    except sqlite3.Error as error:
        print(f"Error al crear la tabla: {error}")
    
    finally:
        conexion.close()