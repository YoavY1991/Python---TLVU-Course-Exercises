def special_printer(my_string):
    string1 = ''
    if len(my_string) > 10:
        for i, l in enumerate(my_string):
            if i == 0:
                string1 += l.upper()
            elif i % 2 == 0:
                string1 += l.upper()
            else:
                continue
        print(string1)

    else:
        while len(string1 + my_string) <= 10:
            string1 += my_string
        print(string1)


special_printer('aBc')
