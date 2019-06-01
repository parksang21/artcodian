from django.urls import path

from . import views

urlpatterns = [
    path('', views.ticket, name='ticket'),
    path('check/<code>', views.check_ticket, name="check"),
    path('form/', views.ticket_generation, name="ticketing")
]
