from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views import View
from django.http import HttpResponse
from hives.forms import AddHiveForm, HiveDataForm, SignInForm
from hives.models import HiveModel, HiveDataModel
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login

# Create your views here.
class LoginView(View):
    
    def get(self, request):
        ctx = SignInForm()
        return render(request, 'login.html', {'ctx': ctx})

    def post(self, request):
        form_data = SignInForm(request.POST)
        user = authenticate(request, username=form_data['login'], password=form_data['password'])
        if user is not None:
            login(request, user)
            return redirect('/main')
        else:
            return HttpResponse("Nie ma takiego użytkownika")



class MainView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'main.html')


class AddHiveView(LoginRequiredMixin, View):
    #View to add a new hive

    def get(self, request):
        form = AddHiveForm()
        return render(request, 'add_hive.html', {'form': form})

    def post(self, request):
        form = AddHiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse("Ul o tym numerze już istnieje")


class HiveListView( LoginRequiredMixin, View):

    #List of all hives

    def get(self, request):
        ctx = HiveModel.objects.all()

        return render(request, 'hive_list.html', {'ctx': ctx})


class HiveListDetailedView(LoginRequiredMixin, View):

    #Detailed view of a specific hive

    def get(self, request, num):

        hiveInformation = HiveModel.objects.all().filter(numberOfHive=num)
        return render(request, 'detailed.html', {'ul_id': num,
                                                 'ul_info': hiveInformation,})

class AddDataDisplayHives(LoginRequiredMixin, View):

    #Displays list of all hives to which we can add data
    def get(self, request):
        ctx = HiveModel.objects.all()
        return render(request, 'display_hives.html', {'ctx': ctx})

    def post(self, request):
        ctx = HiveModel.objects.all()
        return render(request, 'display_hives.html', {'ctx': ctx})


class AddData(LoginRequiredMixin, View):

    #Addiing data to a specific hive
    def get(self, request, num):
        form = HiveDataForm()
        return render(request, 'add_data.html', {'form': form, 'hive_id': num})

    def post(self, request, num):
        form = HiveDataForm(request.POST)
        if form.is_valid():
            print(form)
            #Adding a field to a HiveDataModel that was excluded from in forms.py
            form = form.save(commit=False)
            form.hive_id = int(num)
            form.save()
            return render(request,'display_hives.html', {'ctx': HiveModel.objects.all(), 'success': 'asaa'} )
        else:
            return HttpResponse("Nie dodno danych")

class ShowListOfHives(LoginRequiredMixin, View):

    #displays a list of hives
    #In this view you can choose a hive and see the statistics
    def get(self, request):
        ctx = HiveModel.objects.all()
        return render(request, 'historic_data.html', {'ctx':ctx})


class ShowData(LoginRequiredMixin, View):

    def get(self, request, num):
        #Query gets all data from a chosen hive
        dataOfHive = HiveDataModel.objects.all().filter(hive_id=num)
        return render(request, 'show_data.html', {'hive_id': num, 'dataOfHive': dataOfHive})
