def red_list(str_list):
    # Generates a list of strings from strings in str_list that contains RED as a seperate word.
    # the new list is sorted lexicographically
    str_list_RED = []
    for s in str_list:
        if 'RED' in s.split():
            str_list_RED.append(s)
        else:
            pass

    str_list_RED.sort()
    return str_list_RED[::-1]


str_list = ["The RED ball", "A RED ball", "A red ball", "FRED", "AAA RED"]
red_list(str_list)