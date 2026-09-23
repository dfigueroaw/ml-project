# Proyecto Machine Learning

Este es el repositorio para un proyecto de Machine Learning que utiliza el dataset de viajes en taxi amarillo de Nueva York (enero de 2015) para predecir la duración de dichos viajes.

## Integrantes

- Diego Alonso Figueroa Winkelried (202410533)
- José Daniel Grayson Tejada (202410372)
- Joaquin Adrian Lopez del Carpio (202410220)

## Estructura del repositorio

```
├── data/
│   ├── README.md                instrucciones para descargar el dataset
├── figures/                     figuras exportadas del notebook
├── notebooks/
│   └── 01-eda.ipynb             análisis exploratorio de datos
├── scripts/
│   └── export_figures.py        script para extraer las figuras del notebook ejecutado
├── requirements.txt             dependencias del proyecto
└── README.md
```

## Instrucciones para ejecutar

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Descargar el dataset

Seguir las instrucciones de `data/README.md`. El archivo final debe ubicarse en `data/yellow_tripdata_2015-01.csv`.

### 3. Ejecutar el notebook

Abrir y ejecutar `notebooks/01-eda.ipynb` de forma completa. Este paso:

- Lee y limpia el dataset original (~12.7 millones de registros).
- Genera `data/yellow_tripdata_2015-01_clean.csv` con los datos procesados.
- Produce las gráficas de análisis exploratorio.

### 4. Exportar figuras

```bash
python scripts/export_figures.py
```

Extrae las figuras embebidas en el notebook y las guarda como archivos `.png` en la carpeta `figures/`.
