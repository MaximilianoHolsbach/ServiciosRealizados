from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from Bitacora.models import BitacoraModel
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm

class BitacoraLogin(LoginView):
    template_name = 'Bitacora/Bitacora_login.html'
    next_page = reverse_lazy("BitacoraList")

class Bitacorainicio(TemplateView):
    model = BitacoraModel
    template_name = "Bitacora/index.html"

class BitacoraList(ListView):

    model = BitacoraModel
    template_name = "Bitacora/bitacora_list.html"


class BitacoraDetail(DetailView):

    model = BitacoraModel
    template_name = "Bitacora/bitacora_detail.html"


class BitacoraCreate(CreateView):

    model = BitacoraModel
    success_url = reverse_lazy("BitacoraList")
    fields = ["modelo","serie", "contador", "trabajos", "tecnico"]


class BitacoraUpdate(UpdateView):

    model = BitacoraModel
    success_url = reverse_lazy("BitacoraList")
    fields = ["modelo","serie", "contador", "trabajos", "tecnico"]


class BitacoraDelete(DeleteView):

    model = BitacoraModel
    success_url = reverse_lazy("BitacoraList")

class BitacoraLogin(LoginView):
    template_name = 'Bitacora/Bitacora_login.html'
    next_page = reverse_lazy("BitacoraList")

class BlogLogout(LogoutView):
    template_name = 'Bitacora/bitacora_logout.html'

class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'Bitacora/bitacora_crear_cuenta_form.html'
  success_url = reverse_lazy('BitacoraLogin')
  form_class = UserCreationForm
  success_message = "Your profile was created successfully"