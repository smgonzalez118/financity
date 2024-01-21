from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from vitebackend.quant import optimizarMonteCarlo, getDataYfMulti, getDataYf
import json


@api_view(['GET'])
def prueba(request):
    if request.method == 'GET':
        return Response({"message" : "es una prueba"})


@api_view(['POST'])
def generate_portfolio(request):
    if request.method == 'POST':
        print(f"La data llega así: {request.data}")
    
        rta = optimizarMonteCarlo(activos = request.data["activos"], period = "5y", q=1000, metrica = request.data["metrica"])
        rta = json.dumps(rta)
        return Response({"activos elegidos": request.data, "Objetivo": "Cartera optima", "carteraOptima": rta})
        #return Response({"message": "Algo salió mal!", "enviaste" : request.data})
