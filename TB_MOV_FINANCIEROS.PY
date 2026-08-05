from faker import Faker
import pandas as pd
import random

# Configuración de Faker para Colombia
fake = Faker("es_CO")

# Cantidad de movimientos
NUM_MOVIMIENTOS = 500000

# Leer archivos generados anteriormente
clientes = pd.read_csv("TB_CLIENTES_CORE.csv")
productos = pd.read_csv("TB_PRODUCTOS_CAT.csv")

# Tipo de movimiento
tipos_movimiento = [
    "Consignación",
    "Retiro",
    "Transferencia",
    "Pago",
    "Compra"
]

# Canales
canales = [
    "App",
    "Página Web",
    "Cajero",
    "Sucursal",
    "Corresponsal"
]

# Ciudades
ciudades = [
    "Bogotá",
    "Medellín",
    "Cali",
    "Barranquilla",
    "Cartagena",
    "Fusagasugá",
    "Ibagué",
    "Villavicencio",
    "Armenia",
    "San Andrés"
]

# Estado del movimiento
estados = [
    "Aprobado",
    "Pendiente",
    "Rechazado"
]

# Lista donde se almacenarán los movimientos
movimientos = []

# Generar movimientos
for i in range(1, NUM_MOVIMIENTOS + 1):

    movimiento = {

        "id_mov": f"MOV{i:06}",

        "id_cli": random.choice(clientes["id_cli"].tolist()),

        "cod_prod": random.choice(productos["cod_prod"].tolist()),

        "num_cuenta": str(random.randint(1000000000,9999999999)),

        "fec_mov": fake.date_between(
            start_date="-3y",
            end_date="today"
        ),

        "hra_mov": fake.time(),

        "vr_mov": round(random.uniform(10000,10000000),2),

        "tip_mov": random.choice(tipos_movimiento),

        "cod_canal": random.choice(canales),

        "cod_ciudad": random.choice(ciudades),

        "cod_estado_mov": random.choice(estados),

        "id_dispositivo": f"DIS{random.randint(1,5000):05}"

    }

    movimientos.append(movimiento)

# Crear DataFrame
df_movimientos = pd.DataFrame(movimientos)

# Guardar archivo CSV
df_movimientos.to_csv(
    "TB_MOV_FINANCIEROS.csv",
    index=False,
    encoding="utf-8-sig"
)

print("TB_MOV_FINANCIEROS.csv generado correctamente.")