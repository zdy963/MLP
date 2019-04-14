from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dtcc', views.dtcc, name='dtcc'),
    path('fred', views.fred, name='fred'),
    path('fred_search/<str:name>/', views.fred_search, name='fred_search'),
]