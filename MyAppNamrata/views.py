import ast
import json

from django.http import JsonResponse

# Create your views here.
from rest_framework.response import Response
from rest_framework import status

import MongoDb.Basic as basic
import MongoDb.ConnectMongo as conn
from rest_framework.decorators import api_view

from MongoDb.Service.Parse import parseIt


@api_view(["GET"])
def getData(da):
    #http://127.0.0.1:8000/getData/
    conn.connect_db('db_1')
    p = basic.PackageDb
    Dic ={}
    for i in p.objects:
        Dic.update({i.name:i.value})

#In order to allow non-dict objects to be serialized set the safe parameter to False.
    return JsonResponse(Dic,  safe=False)


@api_view(["GET"])
def putData(requests,security_id):
    #http://127.0.0.1:8000/putData/0P000002HD/
    conn.connect_db('db_1')

    # Basic class
    valueList = parseIt(str(security_id))
    ListOfData = []

    for i in valueList:
        i = ast.literal_eval(i)
        x = json.dumps(i)
        ListOfData.append(json.loads(x))

    for i in ListOfData:
        p = basic.PackageDb()
        p.name = i['i']
        p.value = i['v']
        p.save()
    return Response("Done",status.HTTP_200_OK)