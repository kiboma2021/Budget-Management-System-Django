from django.shortcuts import render

# Create your views here.
def Home(request):
    render(request, 'index.html')

def AddExpense(request):
    render(request, 'add_expense.html')