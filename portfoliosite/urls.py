
from django.urls import path
from quote_generator import views
urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
