# v2
# CRUD - Juan M. Crespo
# proyecto 0001
# 23/02/2026

import sqlite3

class Conexion:
   
    @staticmethod
    def conexionBD():
        try:
            conexion = sqlite3.connect("clientesBD.db")
            return conexion
        except sqlite3.Error as error:
            print(f"Error en la conexión {error}")
            return None