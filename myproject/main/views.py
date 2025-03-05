from django.http import HttpResponse
from django.shortcuts import render


def data_view(request):
    return HttpResponse("<h1>Содержимое страницы Data</h1><p>Здесь вы можете увидеть данные.</p>")

def test_view(request):
    return HttpResponse("<h1>Содержимое страницы Test</h1><p>Это тестовая страница.</p>")

def main_view(request):
    return render(request, 'main.html')



# Create your views here.
