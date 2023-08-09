from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DeleteView
from .forms import NewUserForm, ProfileUpdateForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Catigory, CustomUser
from .models import Profile
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

cats = Catigory.objects.all()

class RegisterView(View):
    def get(self, request):
        form = NewUserForm()
        return render(request, "auth/register.html", {"form":form, "cats":cats})
    
    def post(self, request):
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('index')
        # else:
        messages.error(request, f"{form.errors}")
        return render(request, "auth/register.html", {"form":form, "cats":cats})
        

class LogoutView(LoginRequiredMixin, View):
    login_url = '/auth/register/'
    redirect_field_name = 'index'
    
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect('index')

class LogInView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "auth/login.html", {"form":form, "cats":cats})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('index') 
        else:
              messages.error(request, "Invalid username or password")
              return render(request, "auth/login.html", {"form":form, "cats":cats})
        return render(request, "auth/login.html", {"form":form, "cats":cats})
    
class ProfileUpdatedView(View):
    def get(self, request):
        profile = Profile.objects.filter(user=request.user).first()
        if profile:
            form = ProfileUpdateForm(instance=profile)
            return render(request, "auth/profileU.html", {"form":form})
    
    def post(self, request):
        profile = Profile.objects.filter(user=request.user).first()
        if profile:
            form = ProfileUpdateForm(data=request.POST, files=request.FILES, instance=profile)
            if form.is_valid():
                form.save()
            return redirect("userinfo")
        
class DeleteUser(DeleteView):
    model = CustomUser
    queryset = CustomUser.objects.all()
    template_name = "auth/delete.html"
    success_url = reverse_lazy("index")
    def get_object(self, queryset=None):

        # Получаем объект аккаунта, который будет удален
        obj = super().get_object(queryset=queryset)
        
        # Получаем текущего пользователя
        current_user = self.request.user
        
        # Сравниваем pk аккаунта и pk текущего пользователя
        if obj.pk != current_user.pk:
            raise PermissionDenied("Вы не можете удалить этот аккаунт.")
        
        return obj