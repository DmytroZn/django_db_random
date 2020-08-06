from django.urls import path, include
from . import views
from .dash_apps.finished_apps import history


urlpatterns = [
    path('', views.start, name='start'),
    path('product/', views.product, name='product'),
    path('subject/', views.subject, name='subject'),
    path('formtest/', views.testform, name='formtest'),

]
