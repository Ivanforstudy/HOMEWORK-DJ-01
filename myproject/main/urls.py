
from django.urls import path
from . import views
from .views import data_view, test_view, main_view
urlpatterns = [
    path('data/', views.data_view, name='data_view'),
    path('test/', views.test_view, name='test_view'),
    path('', main_view, name='main_view'),
    ]