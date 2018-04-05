from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from datetime import date, datetime


#Imported functions that are made to calculate data
from calculate_and_add_to_db import calculate_and_add_to_db, calculate_and_add_to_db_re
from add_numbers_from_form import add_numbers_from_form
#Imported models
from .models import Expenses, RepeatableExpenses, Income, ToDoModel
from django.db.models import Sum
#Imported forms
from .forms import LoginForm, ToDoForm, RepeatableExpensesForm
#RepeatableExpensesForm, ToDoForm

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

    shoppinglist = {}

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'shoppinglist.html')

    def post(self, request):


        if 'n' in request.POST:
            return render(request, 'shoppinglist.html', {'shoppinglist': self.shoppinglist.clear()})

        if 'addtolist' and 'amountofproduct' in request.POST:

            product = request.POST['addtolist']
            amount = request.POST['amountofproduct']
            self.shoppinglist[product] = amount


            return render(request, 'shoppinglist.html', {'shoppinglist': self.shoppinglist})

        return render(request, 'shoppinglist.html')



class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('login-view')

#from old project


class MonthlyStatistics(LoginRequiredMixin, View):

    def get(self, request):
        this_month = date.today().month
        this_year = date.today().year

        monthName = {'1': 'styczeń', '2': "luty", "3": "marzec", "4": "kwiecień", "5": "maj",
                    '6': 'czerwiec', '7': 'lipiec', '8': 'sierpień', '9': 'wrzesień', "10": 'październik',
                    '11': 'listopad', '12': 'grudzień'}

        data_from_db_jedzenie = Expenses.objects.filter(month_of_expense=this_month,
                                                        year_of_expense=this_year,
                                                        type_of_expense='Jedzenie').aggregate(Sum('amount_of_money'))
        jedzenie = ''
        for x in data_from_db_jedzenie.values():
            jedzenie = x


        data_from_db_wio = Expenses.objects.filter(month_of_expense=this_month,
                                                        year_of_expense=this_year,
                                                        type_of_expense='Warzywa i owoce').aggregate(Sum('amount_of_money'))
        wio = ''
        for x in data_from_db_wio.values():
            wio = x

        data_from_db_jwp = Expenses.objects.filter(month_of_expense=this_month,
                                                   year_of_expense=this_year,
                                                   type_of_expense='Jedzenie w pracy').aggregate(Sum('amount_of_money'))
        jedzenie_w_pracy = ''
        for x in data_from_db_jwp.values():
            jedzenie_w_pracy = x

        data_from_db_jnm = Expenses.objects.filter(month_of_expense=this_month,
                                                        year_of_expense=this_year,
                                                        type_of_expense='Jedzenie na miescie').aggregate(Sum('amount_of_money'))

        jedzenie_na_miescie = ''
        for x in data_from_db_jnm.values():
            jedzenie_na_miescie = x

        data_from_db_soda = Expenses.objects.filter(month_of_expense=this_month,
                                                        year_of_expense=this_year,
                                                        type_of_expense='Woda sodowa').aggregate(Sum('amount_of_money'))

        woda_sodowa = ''
        for x in data_from_db_soda.values():
            woda_sodowa = x

        data_from_db_przekaski = Expenses.objects.filter(month_of_expense=this_month,
                                                        year_of_expense=this_year,
                                                        type_of_expense='Przekaski').aggregate(Sum('amount_of_money'))
        przekaski = ''
        for x in data_from_db_przekaski.values():
            przekaski = x

        data_from_db_sweets = Expenses.objects.filter(month_of_expense=this_month,
                                                        year_of_expense=this_year,
                                                        type_of_expense='Slodycze').aggregate(Sum('amount_of_money'))
        sweets = ''
        for x in data_from_db_sweets.values():
            sweets = x

        data_from_db_h = Expenses.objects.filter(month_of_expense=this_month,
                                                        year_of_expense=this_year,
                                                        type_of_expense='Zdrowie (leki etc)').aggregate(Sum('amount_of_money'))
        zdrowie = ''
        for x in data_from_db_h.values():
            zdrowie = x

        data_from_db_art = Expenses.objects.filter(month_of_expense=this_month,
                                                        year_of_expense=this_year,
                                                        type_of_expense='Artykuly papiernicze').aggregate(Sum('amount_of_money'))
        art = ''
        for x in data_from_db_art.values():
            art = x

        data_from_db_books = Expenses.objects.filter(month_of_expense=this_month,
                                                        year_of_expense=this_year,
                                                        type_of_expense='Ksiazki i gazety').aggregate(Sum('amount_of_money'))
        books = ''
        for x in data_from_db_books.values():
            books = x

        data_from_db_toys = Expenses.objects.filter(month_of_expense=this_month,
                                                        year_of_expense=this_year,
                                                        type_of_expense='Zabawki/puzzle etc').aggregate(Sum('amount_of_money'))
        toys = ''
        for x in data_from_db_toys.values():
            toys = x

        data_from_db_alkohol = Expenses.objects.filter(month_of_expense=this_month,
                                                        year_of_expense=this_year,
                                                        type_of_expense='Alkohol').aggregate(Sum('amount_of_money'))
        alkohol = ''
        for x in data_from_db_alkohol.values():
            alkohol = x

        data_from_db_kos = Expenses.objects.filter(month_of_expense=this_month,
                                                        year_of_expense=this_year,
                                                        type_of_expense='Kosmetyki').aggregate(Sum('amount_of_money'))
        kos = ''
        for x in data_from_db_kos.values():
            kos = x

        data_from_db_chemia = Expenses.objects.filter(month_of_expense=this_month,
                                                        year_of_expense=this_year,
                                                        type_of_expense='Chemia').aggregate(Sum('amount_of_money'))
        chemia = ''
        for x in data_from_db_chemia.values():
            chemia = x

        data_from_db_clothes = Expenses.objects.filter(month_of_expense=this_month,
                                                        year_of_expense=this_year,
                                                        type_of_expense='Ubrania').aggregate(Sum('amount_of_money'))
        clothes = ''
        for x in data_from_db_clothes.values():
            clothes = x

        data_from_db_gifts = Expenses.objects.filter(month_of_expense=this_month,
                                                                 year_of_expense=this_year,
                                                                type_of_expense='Prezenty').aggregate(Sum('amount_of_money'))
        prezenty = ''
        for x in data_from_db_gifts.values():
            prezenty = x

        data_from_db_other = Expenses.objects.filter(month_of_expense=this_month,
                                                        year_of_expense=this_year,
                                                        type_of_expense='inne wydatki').aggregate(Sum('amount_of_money'))
        other = ''
        for x in data_from_db_other.values():
            other = x

        data_from_db_suma = Expenses.objects.filter(month_of_expense=this_month,
                                                        year_of_expense=this_year).aggregate(Sum('amount_of_money'))
        suma = ''
        for x in data_from_db_suma.values():
            suma = x

        data_from_db_czynsz = RepeatableExpenses.objects.filter(month_of_expense=this_month,
                                                                 year_of_expense=this_year,
                                                                type_of_expense='czynsz').aggregate(Sum('amount_of_money'))
        czynsz = ''
        for x in data_from_db_czynsz.values():
            czynsz = x

        data_from_db_abonament = RepeatableExpenses.objects.filter(month_of_expense=this_month,
                                                                 year_of_expense=this_year,
                                                                type_of_expense='abonament').aggregate(Sum('amount_of_money'))
        abonament = ''
        for x in data_from_db_abonament.values():
            abonament = x

        data_from_db_przedszkole = RepeatableExpenses.objects.filter(month_of_expense=this_month,
                                                                 year_of_expense=this_year,
                                                                type_of_expense='przedszkole').aggregate(Sum('amount_of_money'))
        przedszkole = ''
        for x in data_from_db_przedszkole.values():
            przedszkole = x

        data_from_db_kkm = RepeatableExpenses.objects.filter(month_of_expense=this_month,
                                                                 year_of_expense=this_year,
                                                                type_of_expense='kkm').aggregate(Sum('amount_of_money'))
        kkm = ''
        for x in data_from_db_kkm.values():
            kkm = x

        data_from_db_suma_two = RepeatableExpenses.objects.filter(month_of_expense=this_month,
                                                                 year_of_expense=this_year).aggregate(Sum('amount_of_money'))
        suma_two = ''
        for x in data_from_db_suma_two.values():
            suma_two = x

        #income
        data_for_db_money_kasia = Income.objects.filter(month_of_income=this_month,
                                                                    year_of_income=this_year,
                                                                    type_of_income="Kasia").aggregate(Sum('amount_of_money'))
        money_kasia = ''
        for x in data_for_db_money_kasia.values():
            money_kasia = x

        data_for_db_money_pawel = Income.objects.filter(month_of_income=this_month,
                                                                    year_of_income=this_year,
                                                                    type_of_income="Pawel").aggregate(Sum('amount_of_money'))
        money_pawel = ''
        for x in data_for_db_money_pawel.values():
            money_pawel = x

        data_from_db_suma_income = Income.objects.filter(month_of_income=this_month,
                                                                    year_of_income=this_year).aggregate(Sum('amount_of_money'))
        suma_income = ''
        for x in data_from_db_suma_income.values():
            suma_income = x

        return render(request, 'monthlystatistics.html', {'monthName': monthName[str(this_month)],
                                                          'jedzenie': jedzenie,
                                                          'wio': wio,
                                                          'jedzenie_w_pracy': jedzenie_w_pracy,
                                                          'jedzenie_na_miescie': jedzenie_na_miescie,
                                                          'woda_sodowa': woda_sodowa,
                                                          'prezenty': prezenty,
                                                          'przekaski': przekaski,
                                                          'slodycze': sweets,
                                                          'zdrowie': zdrowie,
                                                          'art': art,
                                                          'books': books,
                                                          'toys': toys,
                                                          'alkohol': alkohol,
                                                          'kosmetyki': kos,
                                                          'chemia': chemia,
                                                          'ubrania': clothes,
                                                          'inne': other,
                                                          'suma': suma,
                                                          'czynsz': czynsz,
                                                          'abonament': abonament,
                                                          'przedszkole': przedszkole,
                                                          'kkm': kkm,
                                                          'suma_two': suma_two,
                                                          'money_kasia': money_kasia,
                                                          'money_pawel': money_pawel,
                                                          'suma_income': suma_income,
                                                          })
    def post(self, request):

            this_month = date.today().month
            this_year = date.today().year

            monthName = {'1': 'styczeń', '2': "luty", "3": "marzec", "4": "kwiecień", "5": "maj",
                        '6': 'czerwiec', '7': 'lipiec', '8': 'sierpień', '9': 'wrzesień', "10": 'październik',
                        '11': 'listopad', '12': 'grudzień'}

            data_from_db_jedzenie = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Jedzenie').aggregate(Sum('amount_of_money'))
            jedzenie = ''
            for x in data_from_db_jedzenie.values():
                jedzenie = x

            data_from_db_wio = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Warzywa i owoce').aggregate(Sum('amount_of_money'))
            wio = ''
            for x in data_from_db_wio.values():
                wio = x

            data_from_db_jwp = Expenses.objects.filter(month_of_expense=this_month,
                                                       year_of_expense=this_year,
                                                       type_of_expense='Jedzenie w pracy').aggregate(Sum('amount_of_money'))
            jedzenie_w_pracy = ''
            for x in data_from_db_jwp.values():
                jedzenie_w_pracy = x

            data_from_db_jnm = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Jedzenie na miescie').aggregate(Sum('amount_of_money'))

            jedzenie_na_miescie = ''
            for x in data_from_db_jnm.values():
                jedzenie_na_miescie = x

            data_from_db_soda = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Woda sodowa').aggregate(Sum('amount_of_money'))

            woda_sodowa = ''
            for x in data_from_db_soda.values():
                woda_sodowa = x

            data_from_db_przekaski = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Przekaski').aggregate(Sum('amount_of_money'))
            przekaski = ''
            for x in data_from_db_przekaski.values():
                przekaski = x

            data_from_db_sweets = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Slodycze').aggregate(Sum('amount_of_money'))
            sweets = ''
            for x in data_from_db_sweets.values():
                sweets = x

            data_from_db_h = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Zdrowie (leki etc)').aggregate(Sum('amount_of_money'))
            zdrowie = ''
            for x in data_from_db_h.values():
                zdrowie = x

            data_from_db_art = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Artykuly papiernicze').aggregate(Sum('amount_of_money'))
            art = ''
            for x in data_from_db_art.values():
                art = x

            data_from_db_books = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Ksiazki i gazety').aggregate(Sum('amount_of_money'))
            books = ''
            for x in data_from_db_books.values():
                books = x

            data_from_db_toys = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Zabawki/puzzle etc').aggregate(Sum('amount_of_money'))
            toys = ''
            for x in data_from_db_toys.values():
                toys = x

            data_from_db_alkohol = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Alkohol').aggregate(Sum('amount_of_money'))
            alkohol = ''
            for x in data_from_db_alkohol.values():
                alkohol = x

            data_from_db_kos = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Kosmetyki').aggregate(Sum('amount_of_money'))
            kos = ''
            for x in data_from_db_kos.values():
                kos = x

            data_from_db_chemia = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Chemia').aggregate(Sum('amount_of_money'))
            chemia = ''
            for x in data_from_db_chemia.values():
                chemia = x

            data_from_db_clothes = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Ubrania').aggregate(Sum('amount_of_money'))
            clothes = ''
            for x in data_from_db_clothes.values():
                clothes = x

            data_from_db_gifts = Expenses.objects.filter(month_of_expense=this_month,
                                                                     year_of_expense=this_year,
                                                                    type_of_expense='Prezenty').aggregate(Sum('amount_of_money'))
            prezenty = ''
            for x in data_from_db_gifts.values():
                prezenty = x

            data_from_db_other = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='inne wydatki').aggregate(Sum('amount_of_money'))
            other = ''
            for x in data_from_db_other.values():
                other = x

            data_from_db_suma = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year).aggregate(Sum('amount_of_money'))
            suma = ''
            for x in data_from_db_suma.values():
                suma = x

            data_from_db_czynsz = RepeatableExpenses.objects.filter(month_of_expense=this_month,
                                                                     year_of_expense=this_year,
                                                                    type_of_expense='czynsz').aggregate(Sum('amount_of_money'))
            czynsz = ''
            for x in data_from_db_czynsz.values():
                czynsz = x

            data_from_db_abonament = RepeatableExpenses.objects.filter(month_of_expense=this_month,
                                                                     year_of_expense=this_year,
                                                                    type_of_expense='abonament').aggregate(Sum('amount_of_money'))
            abonament = ''
            for x in data_from_db_abonament.values():
                abonament = x

            data_from_db_przedszkole = RepeatableExpenses.objects.filter(month_of_expense=this_month,
                                                                     year_of_expense=this_year,
                                                                    type_of_expense='przedszkole').aggregate(Sum('amount_of_money'))
            przedszkole = ''
            for x in data_from_db_przedszkole.values():
                przedszkole = x

            data_from_db_kkm = RepeatableExpenses.objects.filter(month_of_expense=this_month,
                                                                     year_of_expense=this_year,
                                                                    type_of_expense='kkm').aggregate(Sum('amount_of_money'))
            kkm = ''
            for x in data_from_db_kkm.values():
                kkm = x

            data_from_db_suma_two = RepeatableExpenses.objects.filter(month_of_expense=this_month,
                                                                     year_of_expense=this_year).aggregate(Sum('amount_of_money'))
            suma_two = ''
            for x in data_from_db_suma_two.values():
                suma_two = x

            #Income
            data_for_db_money_kasia = Income.objects.filter(month_of_income=this_month,
                                                            year_of_income=this_year,
                                                            type_of_income="Kasia").aggregate(Sum('amount_of_money'))

            money_kasia = ''
            for x in data_for_db_money_kasia.values():
                money_kasia = x

            data_for_db_money_pawel = Income.objects.filter(month_of_income=this_month,
                                                            year_of_income=this_year,
                                                            type_of_income="Pawel").aggregate(Sum('amount_of_money'))
            money_pawel = ''
            for x in data_for_db_money_pawel.values():
                money_pawel = x

            return render(request, 'chart.html',   {'monthName': monthName[str(this_month)],
                                                    'jedzenie': jedzenie,
                                                    'wio': wio,
                                                    'jedzenie_w_pracy': jedzenie_w_pracy,
                                                    'jedzenie_na_miescie': jedzenie_na_miescie,
                                                    'woda_sodowa': woda_sodowa,
                                                    'prezenty': prezenty,
                                                    'przekaski': przekaski,
                                                    'slodycze': sweets,
                                                    'zdrowie': zdrowie,
                                                    'art': art,
                                                    'books': books,
                                                    'toys': toys,
                                                    'alkohol': alkohol,
                                                    'kosmetyki': kos,
                                                    'chemia': chemia,
                                                    'ubrania': clothes,
                                                    'inne': other,
                                                    'suma': suma,
                                                    'czynsz': czynsz,
                                                    'abonament': abonament,
                                                    'przedszkole': przedszkole,
                                                    'tickets': kkm,
                                                    'suma_two': suma_two,
                                                    'money_kasia': money_kasia,
                                                    'money_pawel': money_pawel,
                                                    })

class ChooseMonthlyStatistics(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'choosemonthlystatistics.html')

    def post(self,request):
        dateOfStatistic = request.POST['myMonth'].split("-")
        chosenYear = dateOfStatistic[0]
        chosenMonth = dateOfStatistic[1]
        #print(dateOfStatistic[1])
        data_from_db_jedzenie = Expenses.objects.filter(month_of_expense=chosenMonth,
                                                        year_of_expense=chosenYear,
                                                        type_of_expense='Jedzenie').aggregate(Sum('amount_of_money'))
        if data_from_db_jedzenie['amount_of_money__sum'] is None:

            return render(request, 'choosemonthlystatistics.html', {'error_msg': "Nie mam statystyk na wybrany okres!"})
        else:

            this_month = chosenMonth
            this_year = chosenYear

            monthName = {'01': 'styczeń', '02': "luty", "03": "marzec", "04": "kwiecień", "05": "maj",
                        '06': 'czerwiec', '07': 'lipiec', '08': 'sierpień', '09': 'wrzesień', "10": 'październik',
                        '11': 'listopad', '12': 'grudzień'}

            data_from_db_jedzenie = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Jedzenie').aggregate(Sum('amount_of_money'))
            jedzenie = ''
            for x in data_from_db_jedzenie.values():
                jedzenie = x

            data_from_db_wio = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Warzywa i owoce').aggregate(Sum('amount_of_money'))
            wio = ''
            for x in data_from_db_wio.values():
                wio = x

            data_from_db_jwp = Expenses.objects.filter(month_of_expense=this_month,
                                                       year_of_expense=this_year,
                                                       type_of_expense='Jedzenie w pracy').aggregate(Sum('amount_of_money'))
            jedzenie_w_pracy = ''
            for x in data_from_db_jwp.values():
                jedzenie_w_pracy = x

            data_from_db_jnm = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Jedzenie na miescie').aggregate(Sum('amount_of_money'))

            jedzenie_na_miescie = ''
            for x in data_from_db_jnm.values():
                jedzenie_na_miescie = x

            data_from_db_soda = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Woda sodowa').aggregate(Sum('amount_of_money'))

            woda_sodowa = ''
            for x in data_from_db_soda.values():
                woda_sodowa = x

            data_from_db_przekaski = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Przekaski').aggregate(Sum('amount_of_money'))
            przekaski = ''
            for x in data_from_db_przekaski.values():
                przekaski = x

            data_from_db_sweets = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Slodycze').aggregate(Sum('amount_of_money'))
            sweets = ''
            for x in data_from_db_sweets.values():
                sweets = x

            data_from_db_h = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Zdrowie (leki etc)').aggregate(Sum('amount_of_money'))
            zdrowie = ''
            for x in data_from_db_h.values():
                zdrowie = x

            data_from_db_art = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Artykuly papiernicze').aggregate(Sum('amount_of_money'))
            art = ''
            for x in data_from_db_art.values():
                art = x

            data_from_db_books = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Ksiazki i gazety').aggregate(Sum('amount_of_money'))
            books = ''
            for x in data_from_db_books.values():
                books = x

            data_from_db_toys = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Zabawki/puzzle etc').aggregate(Sum('amount_of_money'))
            toys = ''
            for x in data_from_db_toys.values():
                toys = x

            data_from_db_alkohol = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Alkohol').aggregate(Sum('amount_of_money'))
            alkohol = ''
            for x in data_from_db_alkohol.values():
                alkohol = x

            data_from_db_kos = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Kosmetyki').aggregate(Sum('amount_of_money'))
            kos = ''
            for x in data_from_db_kos.values():
                kos = x

            data_from_db_chemia = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Chemia').aggregate(Sum('amount_of_money'))
            chemia = ''
            for x in data_from_db_chemia.values():
                chemia = x

            data_from_db_clothes = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='Ubrania').aggregate(Sum('amount_of_money'))
            clothes = ''
            for x in data_from_db_clothes.values():
                clothes = x

            data_from_db_gifts = Expenses.objects.filter(month_of_expense=this_month,
                                                                     year_of_expense=this_year,
                                                                    type_of_expense='Prezenty').aggregate(Sum('amount_of_money'))
            prezenty = ''
            for x in data_from_db_gifts.values():
                prezenty = x

            data_from_db_other = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year,
                                                            type_of_expense='inne wydatki').aggregate(Sum('amount_of_money'))
            other = ''
            for x in data_from_db_other.values():
                other = x

            data_from_db_suma = Expenses.objects.filter(month_of_expense=this_month,
                                                            year_of_expense=this_year).aggregate(Sum('amount_of_money'))
            suma = ''
            for x in data_from_db_suma.values():
                suma = x

            data_from_db_czynsz = RepeatableExpenses.objects.filter(month_of_expense=this_month,
                                                                     year_of_expense=this_year,
                                                                    type_of_expense='czynsz').aggregate(Sum('amount_of_money'))
            czynsz = ''
            for x in data_from_db_czynsz.values():
                czynsz = x

            data_from_db_abonament = RepeatableExpenses.objects.filter(month_of_expense=this_month,
                                                                     year_of_expense=this_year,
                                                                    type_of_expense='abonament').aggregate(Sum('amount_of_money'))
            abonament = ''
            for x in data_from_db_abonament.values():
                abonament = x

            data_from_db_przedszkole = RepeatableExpenses.objects.filter(month_of_expense=this_month,
                                                                     year_of_expense=this_year,
                                                                    type_of_expense='przedszkole').aggregate(Sum('amount_of_money'))
            przedszkole = ''
            for x in data_from_db_przedszkole.values():
                przedszkole = x

            data_from_db_kkm = RepeatableExpenses.objects.filter(month_of_expense=this_month,
                                                                     year_of_expense=this_year,
                                                                    type_of_expense='kkm').aggregate(Sum('amount_of_money'))
            kkm = ''
            for x in data_from_db_kkm.values():
                kkm = x

            data_from_db_suma_two = RepeatableExpenses.objects.filter(month_of_expense=this_month,
                                                                     year_of_expense=this_year).aggregate(Sum('amount_of_money'))
            suma_two = ''
            for x in data_from_db_suma_two.values():
                suma_two = x

            #Income
            data_for_db_money_kasia = Income.objects.filter(month_of_income=this_month,
                                                            year_of_income=this_year,
                                                            type_of_income="Kasia").aggregate(Sum('amount_of_money'))

            money_kasia = ''
            for x in data_for_db_money_kasia.values():
                money_kasia = x

            data_for_db_money_pawel = Income.objects.filter(month_of_income=this_month,
                                                            year_of_income=this_year,
                                                            type_of_income="Pawel").aggregate(Sum('amount_of_money'))
            money_pawel = ''
            for x in data_for_db_money_pawel.values():
                money_pawel = x

            return render(request, 'chosenmonthlystatistics.html', {'monthName': monthName[str(this_month)],
                                                                    'jedzenie': jedzenie,
                                                                    'wio': wio,
                                                                    'jedzenie_w_pracy': jedzenie_w_pracy,
                                                                    'jedzenie_na_miescie': jedzenie_na_miescie,
                                                                    'woda_sodowa': woda_sodowa,
                                                                    'prezenty': prezenty,
                                                                    'przekaski': przekaski,
                                                                    'slodycze': sweets,
                                                                    'zdrowie': zdrowie,
                                                                    'art': art,
                                                                    'books': books,
                                                                    'toys': toys,
                                                                    'alkohol': alkohol,
                                                                    'kosmetyki': kos,
                                                                    'chemia': chemia,
                                                                    'ubrania': clothes,
                                                                    'inne': other,
                                                                    'suma': suma,
                                                                    'czynsz': czynsz,
                                                                    'abonament': abonament,
                                                                    'przedszkole': przedszkole,
                                                                    'tickets': kkm,
                                                                    'suma_two': suma_two,
                                                                    'money_kasia': money_kasia,
                                                                    'money_pawel': money_pawel,
                                                                    })

class AddExpense(LoginRequiredMixin, View):

    def get(self,request):
        return render(request, 'addexpense.html')

    def post(self, request):
        result = {}
        #pobranie zmiennych
        firstcategory = request.POST['firstcategory']
        firstcategoryvalue = request.POST['firstcategoryvalue']
        secondcategory = request.POST['secondcategory']
        secondcategoryvalue = request.POST['secondcategoryvalue']
        thirdcategory = request.POST['thirdcategory']
        thirdcategoryvalue = request.POST['thirdcategoryvalue']
        fourthcategory = request.POST['fourthcategory']
        fourthcategoryvalue = request.POST['fourthcategoryvalue']
        fifthcategory = request.POST['fifthcategory']
        fifthcategoryvalue = request.POST['fifthcategoryvalue']
        sixcategory = request.POST['sixcategory']
        sixcategoryvalue = request.POST['sixcategoryvalue']
        totalvalue = request.POST['totalvalue']

        #policzenie sumy z pola formularza
        try:
            first_dict = add_numbers_from_form(firstcategoryvalue, firstcategory)
            second_dict = add_numbers_from_form(secondcategoryvalue, secondcategory)
            third_dict = add_numbers_from_form(thirdcategoryvalue, thirdcategory)
            fourth_dict = add_numbers_from_form(fourthcategoryvalue, fourthcategory)
            fifth_dict = add_numbers_from_form(fifthcategoryvalue, fifthcategory)
            six_dict = add_numbers_from_form(sixcategoryvalue, sixcategory)

            calculate_and_add_to_db(totalvalue, first_dict, second_dict, third_dict, fourth_dict, fifth_dict, six_dict)
            return render(request, 'addexpense.html')
        except:
            return render(request, 'addexpense.html', {'error_msg': "Nie można dodać tych danych do bazy!"})


class AddRepeatable(LoginRequiredMixin, View):

    def get(self,request):
        form = RepeatableExpensesForm()
        return render(request, 'addrepeatable.html', {'form': form})

    def post(self, request):
        #pobranie zmiennych
        firstcategory = request.POST['firstcategory']
        firstcategoryvalue = request.POST['firstcategoryvalue']

        test_variable = True

        if firstcategory == "...":
            test_variable = False
        else:
            try:
                this_month = date.today().month
                this_year = date.today().year
                value_to_insert = int(firstcategoryvalue)
                RepeatableExpenses.objects.create(amount_of_money=value_to_insert, type_of_expense=str(firstcategory), month_of_expense=this_month, year_of_expense=this_year)
                return render(request, 'addrepeatable.html', {'test': test_variable})
            except:
                return render(request, 'addrepeatable.html', {'test': "Została podana zbyt duża kwota!"})

        return render(request, 'addrepeatable.html', {'test': "Wybierz typ wydatku!"})

class IncomeView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'addincome.html')

    def post(self, request):
        test_variable = False
        income_who = request.POST['firstcategory']
        income_amount = request.POST['income_amount']

        #function to check if the income is connected to a person
        try:
            def check_add_to_db(who, amount):
                if who == "...":
                    return None
                else:
                    return [who, amount]

            input = check_add_to_db(income_who, income_amount)
            if type(input) is list and not isinstance(input[1], int):
                this_month = date.today().month
                this_year = date.today().year
                #Adding to db
                test_variable = True
                Income.objects.create(amount_of_money=int(input[1]),
                                     type_of_income=str(input[0]),
                                     month_of_income=this_month,
                                     year_of_income=this_year)

            return render(request, 'addincome.html', {'test': test_variable})
        except:
            return render(request, 'addincome.html', {'test': "Z"})

class ToDoAddView(LoginRequiredMixin, View):

    def get(self, request):
        form = ToDoForm()
        return render(request, 'todoadd.html', {'form': form})

    def post(self, request):
        form = ToDoForm(request.POST)
        if form.is_valid():
            end_date = request.POST['endDate']
            if end_date == '':
                new_form = ToDoForm()
                return render(request, 'todoadd.html', {'form': new_form,
                                                     'msg': "Wybierz datę zakończnie zadania!"})
            else:
                today = date.today()
                if datetime.strptime(end_date, '%Y-%m-%d') > datetime.strptime(str(today), '%Y-%m-%d'):
                    text_field = form.cleaned_data['text_field']
                    whos_task = form.cleaned_data['whos_task']
                    ToDoModel.objects.create(task_text=text_field,
                                            whos_task=whos_task,
                                            end_date=end_date)

                    new_form = ToDoForm()
                    return render(request, 'todoadd.html', {'form': new_form,
                                                        'msg': "Dodano zadanie!"})
                else:
                    new_form = ToDoForm()
                    return render(request, 'todoadd.html', {'form': new_form,
                                                        'msg': "Nie można wybrać daty wcześniejszej niż dzisiejsza!"})

class ToDoListView(LoginRequiredMixin, View):

    def get(self, request):
        list_of_tasks = ToDoModel.objects.all()
        return render(request, 'todolist.html', {'list_of_tasks': list_of_tasks})


class ToDoDelete(DeleteView):
    model = ToDoModel
    success_url = reverse_lazy('todo-list-view')
