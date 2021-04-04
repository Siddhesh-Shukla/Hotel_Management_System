from django.urls import path
from staff_login import views as staff_login_views
from home import views as home_views
urlpatterns = [
    path('', staff_login_views.loginPage, name='SignUp'),
    path('home/', home_views.home, name='home')
]