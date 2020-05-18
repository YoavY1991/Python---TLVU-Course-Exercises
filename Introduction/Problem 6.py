def findpass(string):
    spass = string.lower().find('#pass#') + 6
    password = ''
    for i, l in enumerate(string):
        if i >= spass:
            password += l
        else:
            continue

    print(password)


findpass("#PaSs#David!")