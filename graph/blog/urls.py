from django.urls import path
from.import views 
#it is function for mapping the all urls to teh fucntion inside views.py
urlpatterns = [
    path('', views.home, name="home"),

    ]
