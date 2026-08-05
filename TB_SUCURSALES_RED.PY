from faker import Faker
import pandas as pd
import random

# Configuración para Colombia
fake = Faker("es_CO")

# Cantidad de sucursales
NUM_SUCURSALES = 200

# Tipos de punto
tipos_punto = [
    "Sucursal",
    "Corresponsal",
    "Cajero",
    "Oficina Principal"
]

# Estados
estados = [
    "ACTIVO",
    "INACTIVO"
]

# Ciudades y departamentos
ciudades = {
    "Bogotá": "Cundinamarca",
    "Medellín": "Antioquia",
    "Barranquilla": "Atlántico",
    "Cali": "Valle del Cauca",
    "Cartagena": "Bolívar",
    "Ibagué": "Tolima",
    "Fusagasugá": "Cundinamarca",
    "Villavicencio": "Meta",
    "Armenia": "Quindío",
    "San Andrés": "San Andrés y Providencia"
}

# Lista donde se almacenarán las sucursales
sucursales = []

# Generar sucursales
for i in range(1, NUM_SUCURSALES + 1):

    ciudad = random.choice(list(ciudades.keys()))
    departamento = ciudades[ciudad]

    sucursal = {
        "cod_suc": f"SUC{i:03}",
        "nom_suc": f"Sucursal {ciudad} {i}",
        "tip_punto": random.choice(tipos_punto),
        "ciudad": ciudad,
        "depto": departamento,
        "latitud": round(random.uniform(-4.9, 13.4), 5),
        "longitud": round(random.uniform(-81.8, -66.8), 5),
        "activo": random.choice(estados)
    }

    sucursales.append(sucursal)

# Crear DataFrame
df_sucursales = pd.DataFrame(sucursales)

# Guardar CSV
df_sucursales.to_csv(
    "TB_SUCURSALES_RED.csv",
    index=False,
    encoding="utf-8-sig"
)


print("TB_SUCURSALES_RED.csv generado correctamente") 
