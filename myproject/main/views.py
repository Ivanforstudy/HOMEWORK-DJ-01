from django.http import HttpResponse
from django.shortcuts import render


def main_view(request):
    return render(request, 'main/main.html')  # Главная страница

def data_view(request):
    return render(request, 'main/data.html')  # Страница данных

def test_view(request):
    return render(request, 'main/test.html')

# Create your views here.
