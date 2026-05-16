# Análisis de Mortalidad en Colombia 2019

**Autor:** Jean Paul Pineda Pinzón  
**Actividad:** Actividad 4 - Aplicación web interactiva para el análisis de mortalidad en Colombia  
**Herramientas:** Python, Dash, Plotly, Pandas, Render y GitHub

## Introducción

Este proyecto presenta una aplicación web interactiva desarrollada en Python con Dash y Plotly para analizar la mortalidad no fetal en Colombia durante el año 2019. La aplicación permite explorar la información mediante visualizaciones dinámicas que facilitan la interpretación de patrones regionales, temporales, demográficos y causales.

## Objetivo

Analizar los registros de mortalidad no fetal en Colombia para el año 2019, identificando tendencias por departamento, mes, sexo, grupo de edad, causas principales de muerte y municipios con comportamientos relevantes.

## Estructura del proyecto

```text
mortalidad-colombia-2019-jean-pineda/
│
├── app.py
├── requirements.txt
├── README.md
├── render.yaml
├── Procfile
│
├── data/
│   ├── Anexo1.NoFetal2019_CE_15-03-23.xlsx
│   ├── Anexo2.CodigosDeMuerte_CE_15-03-23.xlsx
│   └── Divipola_CE_.xlsx
│
├── data/processed/
│   ├── mapa_departamento.csv
│   ├── muertes_mes.csv
│   ├── top_violencia.csv
│   ├── menor_mortalidad.csv
│   ├── causas_top10.csv
│   ├── sexo_departamento.csv
│   ├── grupos_edad.csv
│   └── kpis.csv
│
└── assets/
    └── style.css
```

## Visualizaciones implementadas

La aplicación incluye los elementos solicitados en la actividad y fue personalizada con el nombre de Jean Paul Pineda Pinzón:

1. Mapa de distribución total de muertes por departamento.
2. Gráfico de líneas con el total de muertes por mes.
3. Gráfico de barras con las 5 ciudades más violentas, considerando homicidios con código X95.
4. Gráfico circular con las 10 ciudades con menor registro de mortalidad.
5. Tabla con las 10 principales causas de muerte, incluyendo código, nombre y total de casos.
6. Gráfico de barras apiladas comparando el total de muertes por sexo en cada departamento.
7. Gráfico de distribución por grupos de edad definidos según la variable GRUPO_EDAD1.

## Requisitos

- Python 3.10 o superior
- Dash
- Plotly
- Pandas
- Openpyxl
- Gunicorn

Las dependencias están definidas en el archivo `requirements.txt`. La aplicación carga archivos CSV resumidos ubicados en `data/processed/`, lo que mejora el tiempo de apertura en Render y evita que el despliegue tenga que leer archivos Excel pesados en cada inicio.

## Instalación local

Clonar el repositorio:

```bash
git clone https://github.com/usuario/mortalidad-colombia-2019-jean-pineda.git
cd mortalidad-colombia-2019-jean-pineda
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:

```bash
python app.py
```

Abrir en el navegador:

```text
http://127.0.0.1:8050
```

## Despliegue en Render

1. Crear un repositorio público en GitHub.
2. Subir todos los archivos del proyecto.
3. Ingresar a Render.
4. Seleccionar **New Web Service**.
5. Conectar el repositorio de GitHub.
6. Configurar el servicio con:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:server`
7. Ejecutar el despliegue.
8. Copiar la URL pública generada por Render.

## Software utilizado

- Python
- Dash
- Plotly
- Pandas
- Openpyxl
- Render
- GitHub

## Resultados esperados

La aplicación permite evidenciar los departamentos con mayor concentración de muertes, las variaciones mensuales de mortalidad, las principales causas de muerte, diferencias por sexo y la distribución por grupos de edad. Estos elementos facilitan una lectura integral del comportamiento de la mortalidad en Colombia durante el año 2019.

<img width="1772" height="561" alt="image" src="https://github.com/user-attachments/assets/6ad561dd-bf45-4b7f-aeff-538240072646" />

