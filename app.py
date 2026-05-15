import os
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, dash_table

# ============================================================
# Actividad 4 - Aplicación web interactiva
# Análisis de mortalidad en Colombia, año 2019
# Autor: Jean Paul Pineda Pinzón
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")

MESES_ORDEN = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

EDAD_ORDEN = [
    "Mortalidad neonatal", "Mortalidad infantil", "Primera infancia", "Niñez",
    "Adolescencia", "Juventud", "Adultez temprana", "Adultez intermedia",
    "Vejez", "Longevidad / Centenarios", "Edad desconocida"
]


def leer_csv(nombre):
    return pd.read_csv(os.path.join(PROCESSED_DIR, nombre))


# =========================
# CARGA DE DATOS RESUMIDOS
# =========================

mapa_df = leer_csv("mapa_departamento.csv")
mes_df = leer_csv("muertes_mes.csv")
violencia_df = leer_csv("top_violencia.csv")
menor_mortalidad_df = leer_csv("menor_mortalidad.csv")
causas_df = leer_csv("causas_top10.csv")
sexo_df = leer_csv("sexo_departamento.csv")
edad_df = leer_csv("grupos_edad.csv")
kpis_df = leer_csv("kpis.csv")
kpis = kpis_df.iloc[0].to_dict()

# Ordenamientos
mes_df["MES_NOMBRE"] = pd.Categorical(mes_df["MES_NOMBRE"], categories=MESES_ORDEN, ordered=True)
mes_df = mes_df.sort_values("MES_NOMBRE")

edad_df["GRUPO_EDAD_DESC"] = pd.Categorical(edad_df["GRUPO_EDAD_DESC"], categories=EDAD_ORDEN, ordered=True)
edad_df = edad_df.sort_values("GRUPO_EDAD_DESC")

sexo_df["TOTAL_DEPTO"] = sexo_df.groupby("DEPARTAMENTO")["TOTAL_MUERTES"].transform("sum")
sexo_df = sexo_df.sort_values("TOTAL_DEPTO", ascending=False)

# =========================
# FIGURAS
# =========================

fig_mapa = px.scatter_geo(
    mapa_df,
    lat="LATITUD",
    lon="LONGITUD",
    size="TOTAL_MUERTES",
    color="TOTAL_MUERTES",
    hover_name="DEPARTAMENTO",
    hover_data={"TOTAL_MUERTES": ":,", "LATITUD": False, "LONGITUD": False},
    projection="natural earth",
    title="Distribución total de muertes por departamento en Colombia, 2019",
    color_continuous_scale="Reds",
    size_max=45,
)
fig_mapa.update_geos(
    showcountries=True,
    countrycolor="LightGray",
    showland=True,
    landcolor="rgb(245, 245, 245)",
    fitbounds="locations",
)
fig_mapa.update_layout(margin=dict(l=20, r=20, t=70, b=20))

fig_lineas = px.line(
    mes_df,
    x="MES_NOMBRE",
    y="TOTAL_MUERTES",
    markers=True,
    title="Total de muertes por mes en Colombia, 2019",
    labels={"MES_NOMBRE": "Mes", "TOTAL_MUERTES": "Total de muertes"},
)

fig_violencia = px.bar(
    violencia_df,
    x="CIUDAD",
    y="TOTAL_HOMICIDIOS",
    text="TOTAL_HOMICIDIOS",
    title="Top 5 ciudades más violentas según homicidios X95",
    labels={"CIUDAD": "Ciudad / Municipio", "TOTAL_HOMICIDIOS": "Casos"},
)
fig_violencia.update_traces(textposition="outside")
fig_violencia.update_layout(xaxis_tickangle=-30)

fig_pie = px.pie(
    menor_mortalidad_df,
    names="CIUDAD",
    values="TOTAL_MUERTES",
    title="10 ciudades con menor registro de mortalidad",
    hole=0.35,
)

fig_sexo = px.bar(
    sexo_df,
    x="DEPARTAMENTO",
    y="TOTAL_MUERTES",
    color="SEXO_NOMBRE",
    barmode="stack",
    title="Comparación del total de muertes por sexo en cada departamento",
    labels={"DEPARTAMENTO": "Departamento", "TOTAL_MUERTES": "Total de muertes", "SEXO_NOMBRE": "Sexo"},
)
fig_sexo.update_layout(xaxis_tickangle=-45)

fig_edad = px.bar(
    edad_df,
    x="GRUPO_EDAD_DESC",
    y="TOTAL_MUERTES",
    text="TOTAL_MUERTES",
    title="Distribución de muertes por grupos de edad DANE",
    labels={"GRUPO_EDAD_DESC": "Grupo de edad", "TOTAL_MUERTES": "Total de muertes"},
)
fig_edad.update_layout(xaxis_tickangle=-35)
fig_edad.update_traces(textposition="outside")

# =========================
# DASH APP
# =========================

app = Dash(__name__, title="Mortalidad Colombia 2019")
server = app.server

app.layout = html.Div([
    html.Div([
        html.P("Actividad 4 ·Aplicación web interactiva", className="eyebrow"),
        html.H1("Análisis de Mortalidad en Colombia 2019"),
        html.P(
            "Proyecto desarrollado por Jean Paul Pineda Pinzón - Maestria en Inteligencia Artificial - Universidad de la salle- datos oficiales de mortalidad no fetal del DANE.",
            className="subtitle",
        ),
    ], className="hero"),

    html.Div([
        html.Div([html.H3(f"{int(kpis['TOTAL_REGISTROS']):,}"), html.P("Registros analizados")], className="kpi"),
        html.Div([html.H3(f"{int(kpis['TOTAL_DEPARTAMENTOS']):,}"), html.P("Departamentos")], className="kpi"),
        html.Div([html.H3(f"{int(kpis['TOTAL_MUNICIPIOS']):,}"), html.P("Municipios")], className="kpi"),
        html.Div([html.H3("2019"), html.P("Año de análisis")], className="kpi"),
    ], className="kpi-grid"),

    html.Div([dcc.Graph(figure=fig_mapa)], className="card"),
    html.Div([dcc.Graph(figure=fig_lineas)], className="card"),

    html.Div([
        html.Div([dcc.Graph(figure=fig_violencia)], className="card"),
        html.Div([dcc.Graph(figure=fig_pie)], className="card"),
    ], className="grid-two"),

    html.Div([
        html.H2("10 principales causas de muerte en Colombia"),
        html.P("La tabla presenta el código CIE-10, el nombre de la causa y el total de casos registrados, ordenados de mayor a menor."),
        dash_table.DataTable(
            data=causas_df.to_dict("records"),
            columns=[
                {"name": "Código", "id": "COD_MUERTE"},
                {"name": "Causa de muerte", "id": "NOMBRE_MUERTE"},
                {"name": "Total de casos", "id": "TOTAL_CASOS", "type": "numeric"},
            ],
            page_size=10,
            style_table={"overflowX": "auto"},
            style_cell={
                "textAlign": "left",
                "padding": "12px",
                "fontFamily": "Arial",
                "whiteSpace": "normal",
                "height": "auto",
            },
            style_header={"backgroundColor": "#0f172a", "color": "white", "fontWeight": "bold"},
            style_data_conditional=[{"if": {"row_index": "odd"}, "backgroundColor": "#f8fafc"}],
        ),
    ], className="card"),

    html.Div([dcc.Graph(figure=fig_sexo)], className="card"),
    html.Div([dcc.Graph(figure=fig_edad)], className="card"),

    html.Footer([
        html.P("Fuente de datos: Estadísticas Vitales DANE 2019 · Mortalidad no fetal."),
        html.P("Desarrollado por Jean Paul Pineda Pinzón"),
    ]),
], className="container")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8050)))
