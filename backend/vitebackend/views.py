from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from vitebackend.quant import optimizarMonteCarlo, getDataYfMulti, getDataYf
import json

import yfinance as yf
import datetime as dt
import numpy as np


@api_view(['GET'])
def prueba(request):
    if request.method == 'GET':
        return Response({"message" : "es una prueba"})


@api_view(['POST'])
def generate_portfolio(request):
    if request.method == 'POST':
        print(f"La data llega así: {request.data}")
    
        rta = optimizarMonteCarlo(activos = request.data["activos"], period = "5y", q=500, metrica = request.data["metrica"])
        rta = json.dumps(rta)
        return Response({"activos elegidos": request.data, "Objetivo": "Cartera optima", "carteraOptima": rta})
        #return Response({"message": "Algo salió mal!", "enviaste" : request.data})


@api_view(['GET'])
def get_tenencia(request):
    activos=['DOT-USD', "MATIC-USD", 'ADA-USD', 'HBAR-USD', 'ALGO-USD',
    'VET-USD', 'XTZ-USD', 'XLM-USD', 'ZIL-USD', 'ONT-USD', 'OGN-USD', 'XRP-USD']

    nominales = {'DOT-USD' : 1.18, "MATIC-USD": 139, 'ADA-USD' : 272.9, 'HBAR-USD' : 837.50, 'ALGO-USD' : 169.1,
    'VET-USD' : 2974.10, 'XTZ-USD' : 32.2, 'XLM-USD' : 629.61, 'ZIL-USD' : 1869.30, 'ONT-USD' : 68.6, 'OGN-USD' : 25.3, 'XRP-USD' : 1801.31}

    tenencias = {}

    if request.method == 'GET':
        for activo in activos:
            try:
                precio = yf.download(activo, period="5d")['Close'][activo].iloc[-1]
                tenencias[activo] = round(precio * nominales[activo],2)
            except:
                continue

        arr = np.array(tenencias)

        valores_tenencia = list(tenencias.values())
        arr = np.array(valores_tenencia)
        suma = round(arr.sum(),2)

        msg = f'La tenencia al día de hoy es de U$D {suma}'

        return Response({"message" : msg, "tenencias" : tenencias})