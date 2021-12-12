# Proceso de ingeniería de características.
## Proyecto final de la materia de Ingeniería de Características de la Maestría en Ciencia de Datos de la Universidad de Sonora.
### Análisis de trayectorias escolares

La finalidad de este proyecto es el de poner en práctica un proceso simple de ingeniería de características. Este proceso busca el analizar un conjunto de datos pertenecientes a dos programas de licenciatura de la Universidad de Sonora:
- Licenciatura en Enfermería
- Licenciatura en Administración

Estas licenciaturas representan el mejor y el peor programa, en términos de indicadores de trayectorias escolares:
•	Tasa de retención del primero al segundo semestre
•	Índice de reprobación por materia
•	Porcentaje de alumnos regulares
•	Eficiencia terminal
•	Entre otros.

Pretendemos con este análisis, intentar encontrar patrones o características que nos pudieran mostrar que hace que un programa tenga buenos resultados en los indicadores de trayectorias y que hace al otro que no sean tan buenos.
El proyecto consta de varios pasos o secciones:

#### Obtención de los datos.
En este caso la información fue proporcionada por la dirección de servicios escolares a través de la Secretaria General Académica. Esta información se encuentra en 2 archivos en formato .xlsx comprimidos en formato .7z los cuales se encuentran en este repositorio en la carpeta 'Datos':
- HISTORIAL-Calificaciones-2212-21112021-enviar.7z
- Calificaciones-2212-21112021-enviar.7z

#### Análisis exploratorio y limpieza de datos
Armonización de variables Manejo correcto y codificación de datos cuantitativos, cualitativos, fechas y horas. Manejo de valores perdidos Detección y manejo de valores anómalos (outliers)

#### Generación de un conjunto de datos arreglados (tidy data)
Un script (R o Python) de limpieza básica que lea los datos crudos y devuelva los datos acomodados Los datos en forma tidy, ya sea en csv, parquet, o SQlite Un diccionario de datos especificando las descripciones de cada atributo y sus unidades Limpieza de datos, la cual debe incluir:

#### Presentación de un Dashboard



Data extraction and data tidying processes: Data about video games platforms and video games ratings is extracted from IGDB using its API, then, retrieved data is tydified and stored in raw_data folder. Also, data dictionaries are created and stored in data_dicts folder. The details are in 1_problem_statement_and_data_extraction.ipynb.

Data cleaning: Raw data is processed, column types are adjusted, repeated and missing values are handled, and outliers detection is performed. Finally, cleaned data is stored in cleaned_data folder. The details are in 2_data_cleaning.ipynb.

Exploratory Data Analysis: An exploratory data analysis is performed over platforms and video games data. Details in 3_eda.ipynb.

Report generation: Data is used to answer the main questions of the analyis and automatically a pdf report is generated. Images and the pdf report file are stored in report folder. All the details are in 4_report_generation.ipynb.

To reproduce the results is recommended to create an anaconda environment from the videogames.yml file.
