from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='expenses'),
   # path('add_expense', views.index, name='add_expense'),
]