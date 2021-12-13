# Proceso de ingeniería de características.
## Proyecto final de la materia de Ingeniería de Características de la Maestría en Ciencia de Datos de la Universidad de Sonora.
### Análisis de trayectorias escolares

La finalidad de este proyecto es el de poner en práctica un proceso simple de ingeniería de características. Este proceso busca el analizar un conjunto de datos pertenecientes a dos programas de licenciatura de la Universidad de Sonora:
- Licenciatura en Enfermería
- Licenciatura en Administración

Estas licenciaturas representan el mejor y el peor programa, en términos de indicadores de trayectorias escolares:
- Tasa de retención del primero al segundo semestre
- Índice de reprobación por materia
- Porcentaje de alumnos regulares
- Eficiencia terminal
- Entre otros.

Pretendemos con este análisis, intentar encontrar patrones o características que nos pudieran mostrar que hace que un programa tenga buenos resultados en los indicadores de trayectorias y el otro no. Sin embargo, para esta primera entrega, limitaremos el alcance a una comparacion simple entre ambas carreras para confirmar lo que en este momento ya sabemos.

El proyecto consta de varios pasos o secciones:

#### Obtención de los datos.
En este caso la información fue proporcionada por la dirección de servicios escolares a través de la Secretaria General Académica. Esta información se encuentra en 2 archivos en formato .xlsx comprimidos en formato .7z los cuales se encuentran en este repositorio en la carpeta 'Datos':
- HISTORIAL-Calificaciones-2212-21112021-enviar.7z
- Calificaciones-2212-21112021-enviar.7z
Pueden ser descargados de manera manual o a través del script [obtener_datos](https://github.com/m-valenzuela-arce/Proceso-de-Ing-de-Caracteristicas/blob/main/obtener_datos.py).

#### Limpieza de datos
Se realizó un análisis exploratorio y un proceso de limpieza de datos. En este paso se identifican la parte incorrecta, incompleta, inexacta, irrelevante o faltante de los datos para luego modificarlos, reemplazarlos o eliminarlos según sea necesario. Se Eliminaron columnas las cuales no tenían ninguna información, otras que tenían información irrelevante para nuestro análisis, se realizó un proceso de armonización de variables donde modificamos nombres de columnas para la correcta unión de las dos fuentes de datos, así como un mejor entendimiento de su contenido. Se modifico el tipo de dato de algunas características para su mejor representación y manejo.

#### Analisis Exploratorio y generación de un conjunto de datos tidy data
Se realiza un analisis exploratprio de datos utilizando la herramienta Pandas-Profiling, esta nos generó el sigiente [Reporte](https://github.com/m-valenzuela-arce/Proceso-de-Ing-de-Caracteristicas/blob/2854477ab0af78597d59c2e65192ddecb48a611c/Reporte_EDA.html). Se creó además un una libreta de Juyter Notebook en Python la cual se encuentra en este repositorio, en ella, se realiza la lectura, limpieza y análisis de los datos y cual devuelva un subconjunto de datos en forma tidy y en formato csv para poder ser utilizaso en la siguiente fase de este proceso. Se creo también un diccionario de datos con la descripcion de los atributo. La libreta con estas acciones se encuentra [aqui](https://github.com/m-valenzuela-arce/Proceso-de-Ing-de-Caracteristicas/blob/2854477ab0af78597d59c2e65192ddecb48a611c/Proceso_Ingenieria.ipynb).

#### Dashboard
Publicación de un dashboar mostrando una comparación simple entre ambos programas. 
[Dashboard](https://public.tableau.com/app/profile/manuel.valenzuela/viz/Trayectorias/Dashboard1?publish=yes)
