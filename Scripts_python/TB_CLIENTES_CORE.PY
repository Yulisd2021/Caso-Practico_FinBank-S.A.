from faker import Faker
import pandas as pd
import random

# Configuración de Faker para Colombia
fake = Faker("es_CO")

# Cantidad de registros solicitados
NUM_CLIENTES = 10000

# Listas de valores
segmentos = [
    "BASICO",
    "ESTANDAR",
    "PREMIUM",
    "ELITE"
]

tipos_documento = [
    "CC",
    "CE",
    "TI"
]

estados = [
    "ACTIVO",
    "INACTIVO"
]

canales = [
    "APP",
    "Pagina WEB",
    "OFICINA",
    "CORRESPONSAL"
]

ciudades = [
    "Bogotá",
    "Medellín",
    "Barranquilla",
    "Ibagué",
    "Fusagasugá",
    "Cali",
    "San Andrés",
    "Cartagena",
    "Armenia",
    "Villavicencio"
]

departamentos = [
    "Cundinamarca",
    "Antioquia",
    "Atlántico",
    "Tolima",
    "Cundinamarca",
    "Valle del Cauca",
    "San Andrés y Providencia",
    "Bolívar",
    "Quindío",
    "Meta"
]

# Lista donde se almacenarán los clientes
clientes = []

# Generar clientes
for i in range(1, NUM_CLIENTES + 1):

    cliente = {
        "id_cli": f"CLI{i:06}",
        "nomb_cli": fake.first_name(),
        "apell_cli": fake.last_name(),
        "tip_doc": random.choice(tipos_documento),
        "num_doc": str(random.randint(10000000, 9999999999)),
        "fec_nac": fake.date_of_birth(minimum_age=18, maximum_age=80),
        "fec_alta": fake.date_between(start_date="-10y", end_date="today"),
        "cod_segmento": random.choice(segmentos),
        "score_buro": str(random.randint(300, 950)),
        "ciudad_res": random.choice(ciudades),
        "depto_res": random.choice(departamentos),
        "estado_cli": random.choice(estados),
        "canal_adquis": random.choice(canales)
    }

    clientes.append(cliente)

# Crear DataFrame
df_clientes = pd.DataFrame(clientes)

# Guardar archivo CSV
df_clientes.to_csv(
    "TB_CLIENTES_CORE.csv",
    index=False,
    encoding="utf-8-sig"
)


print("TB_CLIENTES_CORE.cs generado correctamente")
