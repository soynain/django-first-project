from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def index(request):
    return HttpResponse("hola mundo")

def simplequery(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM pruebaproductos")
        row = cursor.fetchall()
        tuple_list=row
        context={'consulta':tuple_list}
    print(row[0])
    return render(request,'index.html',context)