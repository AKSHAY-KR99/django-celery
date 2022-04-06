from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.test),
    path('sendmail/', views.send_mail_to_all),
    path('mail/', views.send_email_testing),
    path('schedule/', views.schedule_mail),
    path('periodic/', views.get_periodic_tasks),
    path('akshay/', views.print_name_akshay)
]
