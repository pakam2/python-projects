from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.


class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('main/')
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password= form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main/')
            else:
                return HttpResponse("Nie ma takiego użytkownika")

class MainSite(LoginRequiredMixin, View):

    def get(self, request):
        if request.user.is_authenticated():
            return render(request, 'main.html')


class ShoppingListView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'shoppinglist.html')



class LogoutView(View):


    def get(self, request):
        logout(request)
        return redirect('login-view')
