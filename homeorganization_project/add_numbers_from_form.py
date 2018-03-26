def add_numbers_from_form(value, category):
    if category == "...":
        return "Nie zaznaczyłeś kategorii"
    else:
        list_of_values = value.split('+')
        sum_of_values = 0
        empty_str =''
        for v in list_of_values:
            if v != '':
                if v.find(','):
                    empty_str = str(v)
                    sum_of_values += float(empty_str.replace(",", "."))
                elif float(v):
                    sum_of_values += float(v)
        dict_to_return = {}
        dict_to_return[category] = sum_of_values
        return dict_to_return
