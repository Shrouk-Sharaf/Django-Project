from django.shortcuts import render  

def index(request):
    return render(request, 'myApp/home.html', {'name': 'Roka'})