from faker import Faker
import pandas as pd
import random

# Configuración de Faker para Colombia
fake = Faker("es_CO")

# Cantidad de obligaciones
NUM_OBLIGACIONES = 30000

# Leer los archivos generados anteriormente
clientes = pd.read_csv("TB_CLIENTES_CORE.csv")
productos = pd.read_csv("TB_PRODUCTOS_CAT.csv")

# Nivel de riesgo
nivel_riesgo = [
    "Bajo",
    "Medio",
    "Alto"
]

# Lista donde se almacenarán las obligaciones
obligaciones = []

# Generar obligaciones
for i in range(1, NUM_OBLIGACIONES + 1):

    id_cliente = random.choice(clientes["id_cli"].tolist())
    codigo_producto = random.choice(productos["cod_prod"].tolist())

    valor_desembolsado = round(random.uniform(1000000, 50000000), 2)
    saldo_capital = round(random.uniform(0, valor_desembolsado), 2)
    valor_cuota = round(valor_desembolsado / random.randint(12, 120), 2)

    fecha_desembolso = fake.date_between(
        start_date="-8y",
        end_date="-30d"
    )

    fecha_vencimiento = fake.date_between(
        start_date="+30d",
        end_date="+10y"
    )

    obligacion = {
        "id_oblig": f"OBL{i:06}",
        "id_cli": id_cliente,
        "cod_prod": codigo_producto,
        "vr_desembolsado": valor_desembolsado,
        "sdo_capital": saldo_capital,
        "vr_cuota": valor_cuota,
        "fec_desembolso": fecha_desembolso,
        "fec_venc": fecha_vencimiento,
        "dias_mora_act": random.randint(0, 180),
        "num_cuotas_pend": random.randint(0, 120),
        "calif_riesgo": random.choice(nivel_riesgo)
    }

    obligaciones.append(obligacion)

# Crear DataFrame
df_obligaciones = pd.DataFrame(obligaciones)

# Guardar archivo CSV
df_obligaciones.to_csv(
    "TB_OBLIGACIONES.csv",
    index=False,
    encoding="utf-8-sig"
)

print("TB_OBLIGACIONES.csv generado correctamente.")