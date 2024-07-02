from django.urls import path
from my_app import views
'''from django.views import list_oportunity'''


urlpatterns =[
    path('home/',views.home,name='home'),
    path('listagem/',views.listagem,name='listagem'), 
    path('salvar/', views.salvar, name="salvar")
]