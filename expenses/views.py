from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def AddExpense(request):
    return render(request, 'add_expense.html')