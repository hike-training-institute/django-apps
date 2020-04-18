from django.urls import path


from . import views

urlpatterns = [
    path('', views.HomePage.as_view()),
    path('login', views.LoginPage.as_view(), name='login')
]