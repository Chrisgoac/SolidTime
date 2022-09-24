import sqlite3 as sql

def create_database():
    connection = sql.connect("solidtime.db")
    connection.commit()
    connection.close()
    