from faker import Faker
import pandas as pd
import random

# Configuración de Faker para Colombia
fake = Faker("es_CO")

# Cantidad de comisiones
NUM_COMISIONES = 80000

# Leer archivos generados anteriormente
clientes = pd.read_csv("TB_CLIENTES_CORE.csv")
productos = pd.read_csv("TB_PRODUCTOS_CAT.csv")

# Tipos de comisión
tipos_comision = [
    "Administración",
    "Manejo",
    "Transferencia",
    "Retiro",
    "Consulta"
]

# Estado del cobro
estados_cobro = [
    "Cobrado",
    "Pendiente",
    "Anulado"
]

# Lista donde se almacenarán las comisiones
comisiones = []

# Generar comisiones
for i in range(1, NUM_COMISIONES + 1):

    comision = {

        "id_comision": f"COM{i:06}",

        "id_cli": random.choice(clientes["id_cli"].tolist()),

        "cod_prod": random.choice(productos["cod_prod"].tolist()),

        "fec_cobro": fake.date_between(
            start_date="-3y",
            end_date="today"
        ),

        "vr_comision": round(random.uniform(1000,50000),2),

        "tip_comision": random.choice(tipos_comision),

        "estado_cobro": random.choice(estados_cobro)

    }

    comisiones.append(comision)

# Crear DataFrame
df_comisiones = pd.DataFrame(comisiones)

# Guardar archivo CSV
df_comisiones.to_csv(
    "TB_COMISIONES_LOG.csv",
    index=False,
    encoding="utf-8-sig"
)

print("TB_COMISIONES_LOG.csv generado correctamente.")