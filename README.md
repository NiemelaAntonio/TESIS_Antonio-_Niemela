# TESIS
Tesis de Licenciatura Antonio E. Niemelä Celeda

AE8MAX:

El archivo AE8MAX tiene incluido datos para 1.6, 1.8 y 2.0 MeV y para dos valores del parámetro B/B0 
(1 y 2, osea cerca de la eclíptica) tomados del modelo RADBELT que se presenta en la pagina del CCMC 
de la NASA (https://ccmc.gsfc.nasa.gov/models/modelinfo.php?model=AE-8/AP-8%20RADBELT). 
El programa ahi dentro plotea los datos medios de Van Allen con su desvío y a su vez plotea en el mismo 
cuadro para la energía de 1,8 MeV (que es la que analizo de Van Allen Probes) los datos del modelo ,para condiciones
de máximo y mínimo solar.

AE8MIN:

Este archivo tiene lo mismo que AE8MAX, pero para el mínimo solar, y no grafica los datos de Van Allen ni su desvío.
A su vez tiene inculidos los datos para B/B0=1 y B/B0=2.

Densidaddepuntoshasta1000.py:

A partir de los datos crudos (.CDF) se queda con las posiciones (xyz,L y L*), los pega uno al lado del otro, calcula la 
distancia a partir de los valores de xyz, y finalmente se queda con los Datos que están por debajo de los 1000km y los que están por debjo de los 2000km, y calcula la fracción de esos datos que se encuentra en esos rangos de distancia.

HISTOGRAMAS_POR_L.py:

A partir de los datos bineados y guardados en formato .npy (formato default en el que numpy guarda los datos cuando se hace un 
np.save), los carga en una matriz, calcula las medias de cada una de las columnas (que cada una corresponde a los datos de cada
bin), enmascara los datos en los cuales hay nan's y hace una figura con muchas ventanas de histogramas por años y para todos los años.


Histograma_Goes_PARA_MOSTRAR.py:

Carga los datos de los sensores de GOES para la energía correspondiente a 2 MeV, enmascara los nan's, calcula la media y los desvios, hace el log10 y realiza el histograma, con un ajuste normal a los datos en el espacio logaritmico.


Histogramas_GOES.py:

Hace lo mismo que el anterior, pero dicierne por años y realiza un histograma por año y finalmente para todos en la misma figura (muchas ventanas)

Histogramas_Zona_Gris.py:

Toma los bines que están entre 3.9 y 4.7 de forma tal que en donde se encuentra el maximo (4.3) queda centrado. Carga todos los datos de los distintos años, fija 11 bines del logaritmo de la energía, entre 2 y 7, y finalmente realiza el histograma, y un ajuste.

Histogramas_por_año_por_bin.py:

A partir de los datos bineados, realiza analogamente a como se hizo en HISTOGRAMAS_POR_L, en vez de hacerlo por año para cada uno de los bines, realiza por año para todos los bines simultaneamente los histogramas. Se podría hacer con menos lineas, y juntando cosas con algunos for, preferí hacerlo "a la nearthental" para hacerlo más rapido.


L_Star_plots.py:

A partir de los datos crudos, pega uno al lado del otro el parámetro de posición L* la posición, el flujo y el tiempo, y realiza el gráfico de flujo vs posicion, con el flujo en escala de colores.

L_plots.py:

lo mismo que el anterior, pero el parámetro para la posición en vez de ser L*, es L. 

LvsL_star.py:

Para poder corroborar que no difieren mucho las posiciones tomadas con L o con L*, y ver que se alinean en la diagonal, pegue todos los datos uno al lado del otro y finalemente grafico uno en funcion del otro.


Media_y_Desvio_NUEVO.py:

Parte de los datos, calcula la media y el desvío por bin de L y grafica en función de L la media, para poder observar el comportamiento en toda la órbita de las sondas Van Allen.


Plot_Datos_Goes_26Ago.py:

Toma los datos crudos de GOES, fijo un treshold fijo que es el que se muestra en www.SolarMonitor.com , cargo el DST y finalmente para los datos rondando el 26 de agosto de 2018, grafica el índice y el flujo para ambos canales de energia.


Tormentas_por_hora.py:

A partir de los datos ya seleccionados de períodos de tormenta, grafica los datos que fueron seleccionados por el programa (PONER PROGRAMA) como se hizo en L_plots.py


de5a8.py:

A partir de los datos de CCMC para B/B0=1 y B/B0=2 y para condiciones de minimo solar, se toman los datos para energías de entre 0,2 y 2,4 y se grafican en funcion de L para conocer como es la sensibilidad del modelo frente a cambios leves de energía.


plot_de_Variables.py:

Toma los datos de GOES y plotea las variables, para poder observar su comportamiento. Luego se usa parte de este programa en  Plot_Datos_Goes_26Ago.py.


sunspot_vs_media.py:

Toma los datos de Manchas solares, carga los .CSV, carga los datos de media por mes calculado antes, para todos los años y los grafica ambos juntos en un twinx


threshold_porbines.py:

Toma los datos de Van Allen, y los binea, y guarda por cada uno de los bines su valor de media.





