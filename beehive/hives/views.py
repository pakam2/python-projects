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

    def get(self, request):
        ctx = HiveModel.objects.all()
        return render(request, 'hive_list.html', {'ctx': ctx})


class DetailedView(View):

    def get(self, request, num):
        #print(num)
        hiveInformation = HiveModel.objects.all().filter(numberOfHive=num)
        return render(request, 'detailed.html', {'ul_id': num,
                                                 'ul_info': hiveInformation,})

class AddHivesData(View):

    def get(self, request):
        ctx = HiveModel.objects.all()
        return render(request, 'add_data_to_hives.html', {'ctx': ctx})


class AddData(View):

    def get(self, request, hive_id):
        pass
