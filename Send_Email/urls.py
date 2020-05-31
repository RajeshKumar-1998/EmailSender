from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('Send',views.Send,name = 'SendMail'),
    path('result',views.result,name='result')
]