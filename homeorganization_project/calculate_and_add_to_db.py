from datetime import date
from homeorganization.models import Expenses, RepeatableExpenses


def calculate_and_add_to_db(totalvalue, *args):
    list_of_keys = []
    this_month = date.today().month
    this_year = date.today().year

    #sprawdza czy wpisano liczbę z przecinkiem
    if totalvalue.find(','):
        empty_str = str(totalvalue)
        if empty_str == '':
            pass
        else:
            totalvalue = float(empty_str.replace(",", "."))

    for x in args:
        if isinstance(x, dict):
            list_of_keys.append(x)

    if totalvalue != 0:
        #sprawdz czy wartość totalvalue jest pustym stringiem
        if totalvalue == '':
            totalvalue = 0
        if list_of_keys:
            for y in list_of_keys:
                for k, v in y.items():
                    if v > 0:
                        Expenses.objects.create(amount_of_money=v,
                                            type_of_expense=str(k),
                                            month_of_expense=this_month,
                                            year_of_expense=this_year
                                            )
                        totalvalue -= v

            if totalvalue > 0:

                Expenses.objects.create(amount_of_money=totalvalue,
                                    type_of_expense="Jedzenie",
                                    month_of_expense=this_month,
                                    year_of_expense=this_year
                                    )
        else:
            #dodaje do bazy danych, jeśli jest podana tylko wartość paragonu
            if totalvalue != 0:
                Expenses.objects.create(amount_of_money=totalvalue,
                                    type_of_expense="Jedzenie",
                                    month_of_expense=this_month,
                                    year_of_expense=this_year
                                    )
    else:
        print("Nie podałeś wartości paragonu")


def calculate_and_add_to_db_re(argument):
    this_month = date.today().month
    this_year = date.today().year

    print(argument)
    #sprawdz czy wartość totalvalue jest pustym stringiem
    for k, v in argument.items():
        if v == '':
            pass
        else:
            RepeatableExpenses.objects.create(amount_of_money=v,
                                            type_of_expense=str(k),
                                            month_of_expense=this_month,
                                            year_of_expense=this_year)
