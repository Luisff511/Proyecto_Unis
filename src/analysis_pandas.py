from pathlib import Path
import pandas as pd

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "universities_2025.csv"
REPORT_PATH = BASE_DIR / "reports" / "report.txt"

# Cargar CSV
df: pd.DataFrame = pd.read_csv(DATA_PATH)

if df.empty:
    raise ValueError("El CSV se cargó pero está vacío")

# Mapas
EMPLOYABILITY_MAP = {
    "Muy alta": 5,
    "Alta": 4,
    "Media": 3,
    "Baja": 2
}

DIFFICULTY_MAP = {
    "Muy alta": 5,
    "Alta": 4,
    "Media": 3,
    "Baja": 2
}

ONLINE_MAP = {
    "Si": 2,
    "Parcial": 1,
    "No": 0
}

# Normalizar textos
df["posible_online"] = df["posible_online"].str.strip().str.replace("Sí", "Si")

# Mapear
df["nivel_empleabilidad"] = df["nivel_empleabilidad"].map(EMPLOYABILITY_MAP)
df["nivel_dificultad"] = df["nivel_dificultad"].map(DIFFICULTY_MAP)
df["posible_online"] = df["posible_online"].map(ONLINE_MAP)

# Validar mapping
if df[["nivel_empleabilidad", "nivel_dificultad", "posible_online"]].isnull().any().any():
    raise ValueError("Valores inválidos tras el mapeo")

# Coste (invertido)
df["coste"] = 1 - (
    df["coste_medio_anual_usd"] / df["coste_medio_anual_usd"].max()
)

# Normalizar
df["nota_corte_media_0_100"] /= 100
df["años_estudio"] = 1 - (df["años_estudio"] / df["años_estudio"].max())

# Índice final
df["indice"] = (
    0.30 * df["nivel_empleabilidad"] +
    0.15 * df["coste"] +
    0.15 * df["posible_online"] +
    0.15 * df["nota_corte_media_0_100"] +
    0.15 * df["años_estudio"] -
    0.10 * df["nivel_dificultad"]
)

# Ranking
ranking = df.sort_values("indice", ascending=False).reset_index(drop=False)
print(ranking[["carrera", "indice"]])

# Guardar reporte
with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write("Ranking de Carreras Universitarias 2025\n")
    f.write("=" * 40 + "\n\n")
    for idx, row in ranking.iterrows():
        f.write(f"{idx + 1}. {row['carrera']} - Índice: {row['indice']:.4f}\n") 