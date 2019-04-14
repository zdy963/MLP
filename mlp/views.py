from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from .services import obj2json, errorRep
from fetch_data.conn import dbconn
from pymysql.err import ProgrammingError


# Index
def index(request):
    return render(request, 'index.html')


def dtcc(request):
    comSwap = ComSwap.objects.all()
    comOption = ComOption.objects.all()
    data = {'comSwap': comSwap, 'comOption':comOption}
    return render(request, 'dtcc.html', data)


# Federal Reserve Economic Data
def fred(request):
    return render(request, 'fred.html')


def fred_search(request, name):
    print("Searching for ", name)
    with dbconn() as db:
        try:
            cur = db.cursor()
            name = 'FRED/' + name.upper()
            sql = "select * from `{}`".format(name)
            cur.execute(sql)
            data = cur.fetchall()

            print('Sending to front-end')
            return HttpResponse(obj2json(data), content_type="application/json")
        except ProgrammingError:
            error = "Cannot find table {}. Please try again.".format(name)
            return HttpResponse(errorRep(error), content_type="application/json")