from django.urls import path
from .views import (
    Login,
    SignUp
)


urlpatterns = [
    path('login', Login.as_view(), name='login_url'),
    path('signup', SignUp.as_view(), name='signup_url'),
]
