from django.urls import path
from Text_test import views

urlpatterns = [
    path('home',views.Home),
    path('text',views.text),
    path('analyze',views.analyze)

]
