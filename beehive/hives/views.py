from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views import View
from django.http import HttpResponse
from hives.forms import AddHiveForm, HiveDataForm
from hives.models import HiveModel, HiveDataModel
from django.db.models import Sum

# Create your views here.

class MainView(View):

    def get(self, request):
        return render(request, 'main.html')


class AddHiveView(View):
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


class HiveListView(View):

    #List of all hives

    def get(self, request):
        ctx = HiveModel.objects.all()
        return render(request, 'hive_list.html', {'ctx': ctx})


class HiveListDetailedView(View):

    #Detailed view of a specific hive

    def get(self, request, num):

        hiveInformation = HiveModel.objects.all().filter(numberOfHive=num)
        return render(request, 'detailed.html', {'ul_id': num,
                                                 'ul_info': hiveInformation,})

class AddDataDisplayHives(View):

    #Displays list of all hives to which we can add data
    def get(self, request):
        ctx = HiveModel.objects.all()
        return render(request, 'display_hives.html', {'ctx': ctx})

    def post(self, request):
        ctx = HiveModel.objects.all()
        return render(request, 'display_hives.html', {'ctx': ctx})


class AddData(View):

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

class ShowListOfHives(View):

    #displays a list of hives
    #In this view you can choose a hive and see the statistics
    def get(self, request):
        ctx = HiveModel.objects.all()
        return render(request, 'historic_data.html', {'ctx':ctx})


class ShowData(View):

    def get(self, request, num):
        #Query gets all data from a chosen hive
        dataOfHive = HiveDataModel.objects.all().filter(hive_id=num)
        return render(request, 'show_data.html', {'hive_id': num, 'dataOfHive': dataOfHive})
