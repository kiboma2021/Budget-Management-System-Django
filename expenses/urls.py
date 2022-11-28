from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='expenses'),
    path('add_expense', views.AddExpense, name='add_expense'),
]