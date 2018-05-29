from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from hives.forms import AddHiveForm, HiveDataForm
from hives.models import HiveModel


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
            return HttpResponse("Dodano nowy ul")
        else:
            return HttpResponse("Dane są nie poprawne")


class HiveListView(View):
    #List of all hives
    def get(self, request):
        ctx = HiveModel.objects.all()
        return render(request, 'hive_list.html', {'ctx': ctx})


class DetailedView(View):
    #Detailed view of a specific hive
    def get(self, request, num):
        #print(num)
        hiveInformation = HiveModel.objects.all().filter(numberOfHive=num)
        return render(request, 'detailed.html', {'ul_id': num,
                                                 'ul_info': hiveInformation,})

class DisplayHives(View):

    #Displays list of all hives to which we can add data
    def get(self, request):
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
            #Adding a filed to a HiveDataModel that was excluded from in forms.py
            form = form.save(commit=False)
            form.hive_id = int(num)
            form.save()
            return HttpResponse("Dodano dane")
        else:
            return HttpResponse("Nie dodno danych")
        #first_frame = form['first_frame']
        #second_frame = form['second_frame']
        #third_frame = form['third_frame']
