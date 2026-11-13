import sqlite3
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "veterinaria.settings")
django.setup()

from administracion.models import Cliente

conn = sqlite3.connect("veterinaria_vieja.sqlite")
cursor = conn.cursor()
cursor.execute(""" 
                SELECT num_dni, nombre, apellido , direccion
                FROM cliente
               """)
clientes = cursor.fetchall()
conn.close()

for dni, nombre, apellido, direccion in clientes:
    Cliente.objects.get_or_create(
        dni=dni,
        nombre = nombre,
        apellido = apellido,
        direccion = direccion
    )
print("Cliente migrados correctamente")



