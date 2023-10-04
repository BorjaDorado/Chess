# Chess

[![images.jpg](https://i.postimg.cc/Bb9tWnnk/images.jpg)](https://postimg.cc/Fdph3mcV)

## Descripción
El ***objetivo*** de de este proyecto es ***realizar una ETL*** (Extract, Transform and Load) para un dataset de estadísticas de los top_100 jugadores profesionales de ajedrez y comparar la performance que realizan en los torneos presenciales con larealizada en partidas online.

## Restricciones

1. Utilizar ***3 fuentes*** como mínimo

2. Utilizar al menos ***2 métodos de extracción*** 

## Extracción de datos

La primera fuente que se ha utilizado ha sido [Kaggle]( https://www.kaggle.com/datasets/crxxom/chess-gm-players) para descargar un archivo csv que contiene todos los sats de los GM's actuales (2023) de todas las partidas online que han jugado en la plataforma de Chess.com.

La segunda fuente que se ha empleado para la extracción de datos ha sido una [página web](https://2700chess.com/) de la cual se han obtenido los ratings de los top_100 jugadores en partidas clásicas, rápidas y blitz de torneos presenciales, es decir, su elo oficial. 

Además se ha utilizado una tercera fuente, una [base de datos online](https://www.yottachess.com/) de la que se ha extraido con Selenium los porcentajes totales de partidas ganadas, empatadas y perdidas en torneos presenciales.

## Transformación

Una vez obtenidas las fuentes, se ha procedido a la limpieza de los datos, empezando por el archivo csv. El cual ya viene bastantelimpio y lo único que se hará será eliminar las columnas que no sean relevantes como el día que se alcanzó la máxima puntuación, el día de registro en la página web,los seguidores que tiene cada uno, el link a sus respectivos perfiles, etc.

A continuación se realiza la unión de la tabla final del csv limpio con las otras dos tablas que hemos escrapeado de las otras dos fuentes, mediante la columna nombre, y se guarda como archivo csv.

## Carga de datos

Por último se carga el archivo csv en una base de datos nueva creada en SQL y se guarda como archivo sql.

## Visualización/Análisis de datos.

## Conclusiones
