from django.urls import path
from .views import *

urlpatterns = [
    path('cadastro/', RegisterView.as_view(), name='cadastro'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
