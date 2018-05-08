from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from hives.forms import AddHiveForm

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
            return HttpResponse("Dodano nowy ul")
        else:
            return HttpResponse("Dane są nie poprawne")
