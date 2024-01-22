NOMBRE DEL PROYECTO: Financity
LINK DEMO: https://financity.vercel.app/

FUNCIONALIDAD PRINCIPAL: optimizador de portafolios de inversión en renta variable (acciones) que utiliza el algoritmo de MonteCarlo por detrás,
recopila información financiera de Yahoo Finance (series de precios históricas), calcula métricas de rentabilidad y riesgo, y buscar la mejor
combinación luego de 1000 simulaciones de los hechos reales acontecidos. Permite elegir entre optimizar riesgo (minizarlo), rentabilidad (maximizarla),
relación riesgo-rentabilidad (obtener la combinación óptima) o bien relación riesgo a la baja-rentabilidad (la mejor rentabilidad ajustada/penalizada
por la volatilidad negativa). Permite seleccionar entre todas las acciones disponibles en el índice norteamericano
S&P 500 (el más importante a nivel mundial). El resultado final son las ponderaciones que debe tener cada acción elegida en la cartera de inversión.

TECNOLOGÍAS UTILIZADAS: esquema cliente-servidor, API REST. Para el backend, se utilizó Django y Django Rest Framework. En el mismo se utilizaron librerías de data science tales como
Numpy, Pandas, yfinance, etc. Se procesó la data de series temporales para obtener las métricas de interés, de modo que se aplicó data science.
Por su parte, en el frontend se utilizó React, haciendo uso de componetización, manejo de estados (useState), peticiones a API (axios).

HOSTING: frontend en Vercel / backend en PythonAnywhere

PENDIENTES:

- Refactorizar código
- Agregar acciones argentinas al listado
- Agregar un gráfico de torta
