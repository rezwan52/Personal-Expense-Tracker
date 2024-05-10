from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('submit_expense',views.submit_expense, name='submit_expense'),
    

]
