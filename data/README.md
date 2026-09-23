# Dataset

NYC Yellow Taxi Trip Data (enero 2015). El archivo original (~1.9 GB, ~12.7 millones de registros) no se incluye en el repositorio por su tamaño. Sin embargo, este dataset se puede descargar siguiendo las instrucciones a continuación.

Fuente: [Kaggle - NYC Yellow Taxi Trip Data](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data/)

El dataset se encuentra bajo la licencia de [U.S. Government Works](https://www.usa.gov/government-copyright).

## Instrucciones de descarga

1. Ir a <https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data/>.
2. Hacer clic en **Download** (se descargará un archivo `.zip`).
3. Descomprimir el `.zip`. Dentro encontrarás cuatro archivos CSV:
   - `yellow_tripdata_2015-01.csv`
   - `yellow_tripdata_2016-01.csv`
   - `yellow_tripdata_2016-02.csv`
   - `yellow_tripdata_2016-03.csv`
4. Copiar **solamente** `yellow_tripdata_2015-01.csv` a la carpeta `data/` de este repositorio.

### Opción 2 - Kaggle CLI

Kaggle también cuenta con una herramienta de línea de comandos llamada Kaggle CLI. Si se encuentra instalada, el dataset se puede descargar y mover a esta carpeta con un par de comandos como los siguientes:

```bash
kaggle datasets download -d elemento/nyc-yellow-taxi-trip-data -p /tmp/taxi-data --unzip
mv /tmp/taxi-data/yellow_tripdata_2015-01.csv data/
```

## Archivos resultantes

```
data/
├── README.md
├── yellow_tripdata_2015-01.csv
```

Luego de ejecutar `notebooks/01-eda.ipynb`, se debería generar un nuevo archivo con la data limpia. En ese punto, este directorio quedará de la siguiente forma:

```
data/
├── README.md
├── yellow_tripdata_2015-01.csv
└── yellow_tripdata_2015-01_clean.csv
```
