from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .models import CustomUser
from .forms import RegisterForm, LoginForm
from django.urls import reverse_lazy

class RegisterView(CreateView):
    model = CustomUser
    form_class = RegisterForm
    template_name = "usuarios/cadastro.html"
    success_url = reverse_lazy("login")
    
class LoginView(LoginView):
    template_name = "usuarios/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy("home")

class LogoutView(LogoutView):
    next_page = "login"
