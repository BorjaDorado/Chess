# Chess

## Descripción

El ***objetivo*** de de este proyecto es ***realizar una ETL*** (Extract, Transform and Load) para un dataset de estadísticas de los top_100 jugadores profesionales de ajedrez y comparar la performance que realizan en los torneos presenciales con larealizada en partidas online.

[![images.jpg](https://i.postimg.cc/Bb9tWnnk/images.jpg)](https://postimg.cc/Fdph3mcV)



## Restricciones

1. Utilizar ***3 fuentes de datos*** como mínimo.

2. Utilizar al menos ***2 métodos de extracción***.

## Extracción de datos

En primer lugar, se utilizó [Kaggle]( https://www.kaggle.com/datasets/crxxom/chess-gm-players) para descargar un archivo CSV que contiene todas las estadísticas de los jugadores GM (Grandmaster) actuales (2023) de todas las partidas online que han jugado en la plataforma de Chess.com.

En segundo lugar, se empleó una [página web](https://2700chess.com/) para extraer los ratings de los top_100 jugadores en partidas clásicas, rápidas y blitz de torneos presenciales, es decir, su ELO FIDE oficial. 

Además, se utilizó una [base de datos online](https://www.yottachess.com/) de la cual se extrajeron mediante Selenium los porcentajes totales de partidas ganadas, empatadas y perdidas en torneos presenciales.

## Transformación

Una vez obtenidas las fuentes de datos, se procedió a la limpieza de los mismos. En el caso del archivo CSV, este ya venía bastante limpio, por lo que solo se realizaron eliminaciones de columnas que no fueran relevantes, como el día en que se alcanzó la máxima puntuación, el día de registro en la página web, número de seguidores, enlaces a perfiles, etc.

A continuación, se realizó la unión de la tabla final del CSV limpio con las otras dos tablas obtenidas de las otras fuentes, utilizando la columna del nombre como clave de unión. El resultado se guardó como un archivo CSV.

## Carga de datos

Por último, se cargó el archivo CSV en una nueva base de datos creada en SQL.

## Visualización/Análisis de datos.

En el gráfico de barras, se puede observar que los jugadores ganan y pierden más partidas cuando juegan online que cuando juegan en torneos presenciales. Esto puede justificarse debido a que, al jugar un torneo presencial, suelen adoptar una forma de juego más conservadora, ya que hay algo en juego. En cambio, jugar online tiende a ser más casual.

[![live-vs-online.png](https://i.postimg.cc/D0CWRN0Q/live-vs-online.png)](https://postimg.cc/9w7F7JGz)

El gráfico de puntos revela una correlación lineal entre el porcentaje de victorias y derrotas en ambos casos. Al igual que en el gráfico anterior, las partidas online tienen un mayor porcentaje tanto de victorias como de derrotas. Las partidas online suelen ser más caóticas, ya que existen más riesgos al no tener nada que perder y la mayoría de las partidas son del tipo blitz (3 min). Esto implica que los jugadores tienden a cometer más errores durante el juego. Por otro lado, cuando juegan partidas presenciales, la recta de regresión tiene una pendiente positiva, lo que indica que en general los jugadores ganan más partidas de las que pierden, lo cual tiene más sentido en un entorno más controlado y competitivo.

[![wins-vs-losess.png](https://i.postimg.cc/tCMZ58Lp/wins-vs-losess.png)](https://postimg.cc/w7Djx4qG)

