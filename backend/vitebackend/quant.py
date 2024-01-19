
# DATA FEED - UN TICKER

def getDataYf(ticker, tipo, interval, data_from = None, data_to = None, period = None):
    """
    Es una función para descargar market data de Yahoo Finance con la librería yfinance.
    
    ## Inputs:
        >ticker: el nombre del ticker.
        >tipo: si es "no end" no se indica hasta cuándo (data_to), se obtiene hasta el último día disponible. Si es "end" es
        necesario indicar hasta cuánto (data_to). En ambos casos hay que indicar desde qué fecha (data_from). Si es "period" 
        no se indica ni desde cuándo ni hasta cuándo, sólo el argumento "period" con la cantidad de tiempo a obtener.
        >now : si es True, no se indica hasta cuándo (data_to), se obtiene hasta el último día disponible. Si se indica False, es
        necesario indicar hasta cuánto (data_to).
        >interval: el timeframe (ej. 1m, 1h, 1d, 1w, etc)
        >data_from: data desde qué fecha.
        >data_to: data hasta qué fecha (no inclusive el día). Sólo es aplicable si now == True.
        >period : en caso de tipo = "period", se pasa este argumento que refiere a la cantidad de tiempo a obtener. Ej. 1y, 2y, 3y, etc.
        
    ## Outputs:
        >series OHLC ajustadas del ticker.
    """
    import yfinance as yf
    
    if tipo == "no end":
        data = yf.download(ticker, start = data_from, interval = interval, progress = False, auto_adjust = True)
    elif tipo == "end":
        data = yf.download(ticker, start = data_from, end = data_to, interval = interval, progress = False, auto_adjust = True)
    elif tipo == "period":
        data = yf.download(ticker, interval = interval, period= period, progress = False, auto_adjust = True)
    return data


# DATA FEED - MULTI TICKERS

def getDataYfMulti(activos, tipo, interval, data_from = None, data_to = None, period = None, swap = True):
    """
    Función para hacer batch requests (varios tickers a la vez), que será la fx que más voy a utilizar para market data.
    
    ## Inputs:
        >tickers: es una lista con los tickers de los cuales se va a obtener market data.
        >tipo: si es "no end" no se indica hasta cuándo (data_to), se obtiene hasta el último día disponible. Si es "end" es
        necesario indicar hasta cuánto (data_to). En ambos casos hay que indicar desde qué fecha (data_from). Si es "period" 
        no se indica ni desde cuándo ni hasta cuándo, sólo el argumento "period" con la cantidad de tiempo a obtener.
        >now : si es True, no se indica hasta cuándo (data_to), se obtiene hasta el último día disponible. Si se indica False, es
        necesario indicar hasta cuánto (data_to).
        >interval: el timeframe (ej. 1m, 1h, 1d, 1w, etc)
        >data_from: data desde qué fecha.
        >data_to: data hasta qué fecha (no inclusive el día). Sólo es aplicable si now == True.
        >period : en caso de tipo = "period", se pasa este argumento que refiere a la cantidad de tiempo a obtener. Ej. 1y, 2y, 3y, etc.
        >swap : si es True, divide el df en tickers y cada uno tiene su OHLC. Si es False, tenemos cada columna OHLC y dentro todos los tickers.
        
    ## Outputs:
        >series OHLC ajustadas del ticker.
    """
    import yfinance as yf
    import pandas as pd
    
    lideres_arg = ["ALUA.BA", "BBAR.BA", "BMA.BA", "BYMA.BA", "CEPU.BA", "COME.BA", "CRES.BA", "CVH.BA", "EDN.BA", 
                   "GGAL.BA", "LOMA.BA", "MIRG.BA", "PAMP.BA", "SUPV.BA", "TECO2.BA", "TGNO4.BA", "TGSU2.BA", "TRAN.BA", 
                   "TXAR.BA", "VALO.BA", "YPFD.BA"]

    general_arg = ["AGRO.BA", "AUSO.BA", "BHIP.BA", "BOLT.BA", "BPAT.BA", "CADO.BA", "CAPX.BA", "CARC.BA", "CECO2.BA", 
                   "CELU.BA", "CGPA2.BA", "CTIO.BA", "DGCU2.BA", "FERR.BA", "FIPL.BA", "GAMI.BA", "GCDI.BA", "GCLA.BA", 
                   "HARG.BA", "HAVA.BA", "INVJ.BA", "IRSA.BA", "LEDE.BA", "LONG.BA", "METR.BA", "MOLA.BA", "MOLI.BA", 
                   "MORI.BA", "OEST.BA", "PATA.BA", "RICH.BA", "RIGO.BA", "SAMI.BA", "SEMI.BA"]

    cedears = ["AAL", "AAPL", "ABBV", "ABEV", "ABNB", "ABT", "ADBE", "ADGO", "ADI", "ADP", "AEM", "AIG", "AMAT", "AMD", 
               "AMGN", "AMZN", "AOCA", "ARCO", "ARKK", "ASR", "AUY", "AVGO", "AXP", "AZN", "BA", "BA.C", "BABA", "BB", 
               "BBD", "BBV", "BCS", "BHP", "BIDU", "BIIB", "BIOX", "BITF", "BK", "BMY", "BNG", "BP", "BRFS", "BRKB", "BSBR", 
               "C", "CAAP", "CAH", "CAR", "CAT", "CBRD", "CDE", "CL", "COIN", "COST", "CRM", "CS", "CSCO", "CVX", "CX", "DD", 
               "DE", "DESP", "DIA", "DISN", "DOCU", "DOW", "E", "EA", "EBAY", "EEM", "EFX", "ERIC", "ERJ", "ETSY", "EWZ", "F", 
               "FCX", "FDX", "FMX", "FSLR", "GE", "GFI", "GGB", "GILD", "GLOB", "GLW", "GM", "GOLD", "GOOGL", "GPRK", "GRMN", 
               "GS", "HAL", "HD", "HL", "HMC", "HMY", "HOG", "HON", "HPQ", "HSBC", "HSY", "HUT", "HWM", "IBM", "IFF", "INTC", 
               "ITUB", "IWM", "JD", "JMIA", "JNJ", "JPM", "KMB", "KO", "KOFM", "LLY", "LMT", "LRCX", "LVS", "LYG", "MA", "MCD", 
               "MDT", "MELI", "META", "MMM", "MO", "MOS", "MRK", "MSFT", "MSI", "MSTR", "MU", "NEM", "NFLX", "NGG", "NIO", "NKE", 
               "NOKA", "NTCO", "NTES", "NUE", "NVDA", "NVS", "ORAN", "ORCL", "OXY", "PAAS", "PAC", "PANW", "PBI", "PBR", "PCAR", 
               "PEP", "PFE", "PG", "PHG", "PKS", "PSX", "PYPL", "QCOM", "QQQ", "RBLX", "RIO", "RTX", "SAN", "SAP", "SATL", "SBUX", 
               "SCCO", "SE", "SHEL", "SHOP", "SI", "SID", "SLB", "SNAP", "SNOW", "SONY", "SPGI", "SPOT", "SPY", "SQ", "SYY", "T", 
               "TEFO", "TEN", "TGT", "TM", "TMO", "TRIP", "TRVV", "TSLA", "TSM", "TTE", "TV", "TWLO", "TXN", "TXR", "UAL", "UBER", 
               "UGP", "UL", "UNH", "UNP", "UPST", "USB", "V", "VALE", "VIST", "VIV", "VOD", "VZ", "WBA", "WFC", "WMT", "X", "XLE", 
               "XLF", "XOM", "XP", "YY", "ZM"]

    adrs = ["BBAR", "BMA", "CEPU", "CRESY", "EDN", "GGAL", "IRS", "LOMA", "PAM", "SUPV", "TEO", "TGS", "TS", "TX", "YPF"]

    sectors = ["XLC", "XLP", "XLY", "XLF", "XLV", "XLI", "XLRE", "XLU", "XBI", "XLB", "XLK", "XLE"]
    
    precarga = ["lideres", "general", "cedears", "adrs", "sectores"]
    precarga_dict = {"lideres" : lideres_arg, "general" : general_arg, "cedears" : cedears, "adrs" : adrs, "sectores" : sectors}
    
    if activos in precarga:
        activos = precarga_dict[activos]
    
    if tipo == "no end":
        data = yf.download(activos, start = data_from, interval = interval, progress = False, auto_adjust = True)
    elif tipo == "end":
        data = yf.download(activos, start = data_from, end = data_to, interval = interval, progress = False, auto_adjust = True)
    elif tipo == "period":
        data = yf.download(activos, interval = interval, period= period, progress = False, auto_adjust = True)
    
    if swap:
        #data = data.swaplevel(i = 0, j = 1, axis = 1)
        # Algoritmo para procesar el MultipleTicker download de yfinance
        dicto = {}
        low = data["Low"]
        high = data["High"]
        close = data["Close"]
        open = data["Open"]
        volume = data["Volume"]

        tickers = list(data["Close"].columns)

        for ticker in tickers:
            dicto[ticker] = {
                "Open" : open[ticker],
                "High" : high[ticker],
                "Low" : low[ticker],
                "Close" : close[ticker],
                "Volume" : volume[ticker]
            }

            dicto[ticker] = pd.DataFrame(dicto[ticker])
        return dicto
    return data



# OPTIMIZACIÓN DE CARTERA

def optimizarMonteCarlo(activos, period = "5y", q=1000, metrica = "sharpe"):
    """
    Esta función utiliza el método de MonteCarlo para determinar las ponderaciones óptimas de una cartera de activos especificada.
    Se pueden optimizar las siguientes métricas:
        - Riesgo (minimizarla lo más posible)          => "riesgo"
        - Rentabilidad (maximizarla lo más posible)    => "rentabilidad"
        - Sharpe Ratio (relación riesgo rentabilidad)  => "sharpe"
        - Sortino Ratio (relación riesgo rentabilidad sólo de volatilidad negativa) => "sortino"
        
    # Inputs:
        - activos: es una lista de activos a analizar. Ej.: adrs = ["GGAL", "BBAR", "LOMA", "CEPU"]. También hay sets de activos preconfigurados en la función:
            - "lideres": si se desea cargar todo el panel lider de Argentina;
            - "general": si se desea cargar todo el panel general de Argentina;
            - "adrs": si se desea cargar todo el listado de ADRs argentinos (en usd);
            - "sectors": si se desea cargar el listado de sectores de la economía (ETFs representativos de USA);
            - "cedears": si se desea cargar todo el listado de certificados de depósito de activos del exterior que cotizan en Argentina (puede demorar bastante).
        - period: período de tiempo pasado tomado de base para hacer los estudios. Ej. "1y" (1 año), "5y" (5 años), etc.
        - q : cantidad de simulaciones de MonteCarlo a realizar.
        - metrica: métrica a optimizar. Puede ser: "riesgo" (minimizar), "rentabilidad" (maximizar), "sharpe" (maximizar) 
        y "sortino" (maximizar).
        
    # Outputs:
        - carteras: tabla con todas las simulaciones ordenadas de mejor a peor.
        - rta: cartera óptima en formato de diccionario.
        - rta_df: cartera óptima en formato de tabla.
    """
    
    
    import yfinance as yf
    import pandas as pd
    import numpy as np
    from datetime import datetime, timedelta
    import time
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.style.use('dark_background')
    
    # Obtenemos retornos logarítmicos:
    data = getDataYfMulti(activos, tipo = "period", interval = "1d", period = period, swap = False)["Close"]
    data = pd.DataFrame(data)
    data.dropna(inplace = True)
    ret_log = np.log((data / data.shift(1)).dropna())
    
    pond = np.array(np.random.random(len(data.columns)))
    pond = pond / np.sum(pond)
    carteras = []
    
    for i in range(q):
        # Genero n (de n activos) ponderaciones aleatorias entre 0 y 1
        pond = np.array(np.random.uniform(0, 1, len(data.columns)))
        # Proporciono cada ponderación según su peso sobre el total de la suma de las ponderaciones aleatorias (es que va a dar más que 1)
        pond = pond / np.sum(pond)  # <== ya tengo mis ponderaciones aleatorias.
        r = {}
        # Calculo retorno ponderado de cada activo: retorno esperado (ret_log.mean()) por su ponderación (pond) y lo anualizo (* 252)
        r["retorno"] = np.sum((ret_log.mean() * pond * 252))
        # Calculo covarianza anualizada (ret_log.cov() * 252) ponderada (* pond) de cada activo y le saco raíz cuadrada para desv estandar
        r["volatilidad"] = np.sqrt(np.dot(pond, np.dot(ret_log.cov() * 252, pond)))
        r["volatilidad_neg"] = np.sqrt(np.dot(pond, np.dot(ret_log[ret_log < 0].cov() * 252, pond)))
        # Calculo Sharpe ratio: retorno / volatilidad
        r["sharpe"] = r["retorno"] / r["volatilidad"]
        r["sortino"] = r["retorno"] / r["volatilidad_neg"]
        # Anoto las ponderaciones
        r["weights"] = pond.round(4)
        # Agrego la simulación (cartera) al listado de carteras
        carteras.append(r)
    
    carteras = pd.DataFrame(carteras)
    # Ordeno para obtener la optimización según la métrica elegida:
    if metrica == "sharpe":
        carteras.sort_values(by = "sharpe", ascending = False, inplace = True)
    elif metrica == "rentabilidad":
        carteras.sort_values(by = "retorno", ascending = False, inplace = True)
    elif metrica == "riesgo":
        carteras.sort_values(by = "volatilidad", ascending = True, inplace = True)
    elif metrica == "sortino":
        carteras.sort_values(by = "sortino", ascending = False, inplace = True)
    
    rta = {}
    i = 0
    for activo in data.columns:
        rta[activo] = round(carteras["weights"].iloc[0][i]*100, 2)
        i += 1
    keys = rta.keys()
    pondss = rta.values()
    rta_df = pd.DataFrame(index = keys)
    rta_df["ponds %"] = pondss
    
    #fig, ax = plt.subplots()
    #grafico = ax.pie(rta_df["ponds %"], labels= rta_df["ponds %"].index, autopct='%1.1f%%', colors=sns.color_palette('Set2'))
    
    #plt.close()
    
    return rta