from dis import Instruction
from multiprocessing import connection
import sqlite3 as sql
import time


def create_database():
    connection = sql.connect("solidtime.db")
    connection.commit()
    connection.close()


def create_table():
    connection = sql.connect("solidtime.db")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE control(
            dni integer,
            epoch integer,
            type text
        )"""
    )


def registro_entrada(dni):
    connection = sql.connect("solidtime.db")
    cursor = connection.cursor()
    instruction = f"SELECT * FROM control WHERE dni = {dni} ORDER BY epoch DESC LIMIT 1"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    if datos[0][2] == "entrada":
        print(
            "No se puede generar un registro de entrada ya que el último registro existente que tiene su usuario es un registro de entrada.")
    else:
        instruction = f"INSERT INTO control VALUES ({dni}, {time.time()}, 'entrada')"
        cursor.execute(instruction)
        connection.commit()
    connection.close()


def registro_salida(dni):
    connection = sql.connect("solidtime.db")
    cursor = connection.cursor()
    instruction = f"SELECT * FROM control WHERE dni = {dni} ORDER BY epoch DESC LIMIT 1"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    if datos[0][2] == "salida":
        print(
            "No se puede generar un registro de salida ya que el último registro existente que tiene su usuario es un registro de salida.")
    else:
        instruction = f"INSERT INTO control VALUES ({dni}, {time.time()}, 'salida')"
        cursor.execute(instruction)
        connection.commit()
    connection.close()


def obtener_registros(dni):
    connection = sql.connect("solidtime.db")
    cursor = connection.cursor()
    instruction = f"SELECT * FROM control WHERE dni = {dni} ORDER BY epoch DESC"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    connection.close()
    return datos

# create_database()
# create_table()