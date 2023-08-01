from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name = 'login'),
    path('register/',views.register, name = 'register'),
    path('home/',views.home ,name = 'home'),
    path('logout_out/',views.logout_out,name = "logout_out"),
    path('punch/',views.punch, name = "punch"),
]
