import sqlite3
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "veterinaria.settings")
django.setup()

from administracion.models import Animal, Cliente

# Conexion a la base de datos vieja
conn = sqlite3.connect("veterinaria_vieja.sqlite")
cursor = conn.cursor()

cursor.execute("""
                SELECT id, nombre, raza, categoria, dueno
                FROM animal
               """)

animales = cursor.fetchall()
conn.close()

for id, nombre, raza, categoria, dni_dueno in animales:
    cliente = Cliente.objects.get(dni = dni_dueno)
    Animal.objects.create(
        id = id,
        nombre = nombre,
        raza = raza,
        categoria = categoria,
        duenio = cliente
    )
print ("Animales migrados correctamente")