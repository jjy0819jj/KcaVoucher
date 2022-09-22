from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', auth_views.LoginView.as_view(template_name='main/signin.html'), name='signin'),
    path('signout', auth_views.LogoutView.as_view(), name='signout'),
    path('signup', views.signup, name='signup'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]