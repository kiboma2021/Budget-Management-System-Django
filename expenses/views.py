from django.shortcuts import render

# Create your views here.
def Home(request):
    render(request, 'index.html')
