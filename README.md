# Análisis de las Mejores Carreras Universitarias con Orientación Laboral

## 1. Conceptos Clave

**CSV (Comma-Separated Values)**  
Es un formato estándar de datos tabulares utilizado en empresas y compatible con Excel, bases de datos y Python.

**Pandas**  
Librería de Python diseñada para manipular, analizar y limpiar datos de forma rápida y eficiente, especialmente datos estructurados.

**Pathlib**  
Módulo estándar de Python (no requiere instalación) que permite trabajar con rutas de archivos y carpetas de manera segura, clara y multiplataforma.

---

## 2. Objetivo del Proyecto

El objetivo de este proyecto es analizar las 10 universidades a nivel mundial con mejores salidas profesionales, considerando factores como:

- Carrera
- Coste medio anual en USD
- Nivel de empleabilidad
- Nivel de dificultad
- Años de estudio
- Posibilidad de estudios online
- Nota de corte media (0–100)

Se busca realizar este análisis usando únicamente **estructuras nativas de Python**.

---

## 3. Datos

- Los valores son promedios globales aproximados (EE. UU., Europa, Asia desarrollada).  
- El coste es una media anual en USD, considerando universidades públicas y privadas.  
- La nota de corte se normaliza a una escala de 0–100 para permitir comparaciones entre países.  
- Ideal para **data analysis, rankings o modelos de decisión**, no como cifras oficiales exactas.

---

## 4. Requisitos del sistema

Python 3.10 o superior

Anaconda / Miniconda (recomendado)

Librerías Necesarias

pandas

pathlib (incluida en Python estándar)

Todas las dependencias están definidas en el archivo:

environment.yml

## 5. Creación del entorno

Crear el entorno de trabajo con Conda:

conda env create -f environment.yml
conda activate business_intelligence_universities

## 6. Ejecución del proyecto

El archivo principal que debe ejecutarse es:

src/analysis_pandas.py


Desde la raíz del proyecto, ejecutar:

python src/analysis_pandas.py

Al ejecutar el script:

Se cargan los datos desde data/universities_2025.csv

Se realiza el análisis de las universidades

Se genera automáticamente el archivo:

reports/report.txt


## 8. Arquitectura del Proyecto

```plaintext
business_intelligence_universities/
│
├── data/
│   └── universities_2025.csv       # Datos de las universidades
│
├── src/
│   └── analysis_pandas.py          # Script de análisis
│
├── reports/
│   └── report.txt                  # Reporte generado automáticamente
│
├── environment.yml                 # Entorno de Python y dependencias
└── README.md                       # Este archivo
