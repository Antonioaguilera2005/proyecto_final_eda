import sqlite3

# Crear la base de datos y la tabla para recomendaciones
conn = sqlite3.connect('recomendaciones.db')
c = conn.cursor()

# Crear tabla de recomendaciones
c.execute('''
    CREATE TABLE IF NOT EXISTS recomendaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        producto TEXT NOT NULL,
        supermercado TEXT NOT NULL,
        precio REAL NOT NULL
    )
''')

conn.commit()
conn.close()
