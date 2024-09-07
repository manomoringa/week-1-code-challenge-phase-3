
math = {'ann':50,'sam':89,'ernest':2}
eng = {'sarah':58,'sam':96,'ernest':1}

def merge_dicts(dict1,dict2):
    totals_dict = dict1.copy()

    for key, value in dict2.items():
        if key in totals_dict:
            totals_dict[key] += value
        else:
            totals_dict[key] = value

    return totals_dict

print(merge_dicts(math,eng))