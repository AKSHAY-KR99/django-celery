from django.urls import path
from . import views

urlpatterns = [
    path('fib/', views.FibonacciView.as_view()),
    path('get/', views.FibonacciList.as_view())
]
