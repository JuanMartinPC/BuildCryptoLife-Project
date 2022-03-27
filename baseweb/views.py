from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
import os
from cryptosmosweb.settings import BASE_DIR
import requests
from django.template import Template, Context


def index_view(request):
    return render(request, "index.html")

def rewards_view(request):
    return render(request, "rewards.html")

def layout_view(request):
    return render(request, "layout.html")

def finances_view(request):
    return render(request, "finances.html")



class SnippetList(APIView):
    def get(self, request,address, format='json'):
        paths = address
        params=[
            {
        'from': address,
              'to': '0x3673da4B65832499f9669e283eC4c7031BEA7952',
        'gas': '0x66c0', # 30400
        'gasPrice': '0x2710', # 10000000000000
        'value': '0x7184e72a', # 2441406250
        'data':
        '0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675',
        },
        ]
        data = {"params": params}
        return Response(data)



def xdd(request):
    doc_externo=open(os.path.abspath(str(BASE_DIR)+'\static\product.html'))
    plt = Template(doc_externo.read())
    doc_externo.close()
    path = [os.path.abspath(x).split("static")[1] for x in os.scandir(os.path.abspath(str(BASE_DIR)+'\static\houses'))]
    index = ['overlay_'+str(x) for x in list(range(len(path)))]
    ctx = Context({"casas": path, "indexa": index})
    documento = plt.render(ctx)
    return HttpResponse(documento)



    