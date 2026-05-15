# Informe de entrega

## Actividad 4: Aplicación web interactiva para el análisis de mortalidad en Colombia

**Estudiante:** Jean Paul Pineda Pinzón  
**Año analizado:** 2019  
**Tecnologías utilizadas:** Python, Dash, Plotly, Pandas, Render y GitHub

## Introducción

La presente actividad desarrolla una aplicación web interactiva orientada al análisis de la mortalidad no fetal en Colombia durante el año 2019. A través de herramientas de visualización como Plotly y Dash, se construyen gráficos dinámicos que permiten interpretar el comportamiento de los fallecimientos desde diferentes perspectivas: territorial, temporal, demográfica y causal.

## Objetivo

Construir una aplicación web dinámica que permita explorar los datos de mortalidad en Colombia para el año 2019, identificando patrones relevantes por departamento, mes, ciudad, sexo, grupo de edad y causa de muerte.

## Descripción de la aplicación

La aplicación fue desarrollada en Python utilizando Dash como framework para la construcción de la interfaz web y Plotly para la generación de gráficos interactivos. Los datos utilizados corresponden a mortalidad no fetal 2019, códigos CIE-10 de causas de muerte y la división político-administrativa de Colombia.

## Visualizaciones e interpretación

### 1. Mapa de mortalidad por departamento

El mapa permite observar la distribución territorial de las muertes registradas en Colombia durante 2019. Los departamentos con mayor número de registros se destacan mediante burbujas de mayor tamaño e intensidad visual.

### 2. Muertes por mes

El gráfico de líneas evidencia la evolución mensual de los fallecimientos durante el año. Esta visualización permite identificar meses con incrementos o disminuciones en el número de muertes registradas.

### 3. Top 5 ciudades más violentas

El gráfico de barras presenta las cinco ciudades con mayor número de homicidios asociados al código X95, correspondiente a agresión con disparo de arma de fuego y casos relacionados. Esta visualización permite focalizar el análisis de mortalidad violenta.

### 4. Ciudades con menor mortalidad

El gráfico circular muestra las diez ciudades con menor registro de mortalidad. Este análisis permite identificar territorios con baja frecuencia de registros dentro de la base de datos.

### 5. Principales causas de muerte

La tabla resume las diez principales causas de muerte en Colombia durante el año 2019, incluyendo el código CIE-10, el nombre de la causa y el total de casos registrados.

### 6. Mortalidad por sexo y departamento

El gráfico de barras apiladas compara la mortalidad por sexo en cada departamento. Esta visualización permite identificar diferencias importantes entre hombres y mujeres en la distribución de fallecimientos.

### 7. Mortalidad por grupo de edad

El gráfico por grupos de edad clasifica los registros según la variable GRUPO_EDAD1, agrupándolos en categorías como infancia, juventud, adultez, vejez y longevidad. Esta visualización permite comprender en qué etapas del ciclo de vida se concentra la mortalidad.

## Repositorio del proyecto

**URL GitHub:** pendiente de diligenciar después de subir el proyecto.

## Aplicación desplegada

**URL pública Render:** pendiente de diligenciar después del despliegue.

## Conclusión

La aplicación desarrollada cumple con el objetivo de transformar datos complejos de mortalidad en visualizaciones interactivas y comprensibles. El uso de Dash y Plotly facilita la exploración de la información y permite identificar patrones relevantes para el análisis territorial, demográfico y causal de la mortalidad en Colombia durante el año 2019.
