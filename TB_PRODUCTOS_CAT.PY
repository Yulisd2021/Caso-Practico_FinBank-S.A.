from faker import Faker
import pandas as pd
import random

# Configuración para Colombia
fake = Faker("es_CO")

# Cantidad de productos
NUM_PRODUCTOS = 50

# Listas de valores
tipos_producto = [
    "Cuenta de Ahorros",
    "Cuenta Corriente",
    "Credito de libre inversion",
    "Credito Hipotecario",
    "Credito Vehicular",
    "Credito Educativo",
    "Tarjeta de Credito",
    "CDT"
]

estados = [
    "ACTIVO",
    "INACTIVO"
]

productos = []

for i in range(1, NUM_PRODUCTOS + 1):

    producto = {
        "cod_prod": f"PR{i:03}",
        "desc_prod": random.choice(tipos_producto),
        "tip_prod": random.choice([
            "PASIVO",
            "ACTIVO"
        ]),
        "tasa_ea": round(random.uniform(5.00, 35.00), 2),
        "plazo_max_meses": random.choice([12,24,36,48,60,72,84,120,180]),
        "cuota_min": round(random.uniform(50000,300000),2),
        "comision_admin": round(random.uniform(0,50000),2),
        "estado_prod": random.choice(estados)
    }

    productos.append(producto)

# Crear DataFrame
df_productos = pd.DataFrame(productos)

# Guardar CSV
df_productos.to_csv(
    "TB_PRODUCTOS_CAT.csv",
    index=False,
    encoding="utf-8-sig"
)

print("================================")
print("Archivo generado correctamente")
print("TB_PRODUCTOS_CAT.csv")
print("Total de productos:", len(df_productos))
print("================================")