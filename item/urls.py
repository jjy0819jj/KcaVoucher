from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.create_item, name='create_item'),
]