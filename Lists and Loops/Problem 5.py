def abs_dif(E):
    # The functions if the abs different between 2 follwoing numbers is larger than the abs dif
    # betweeen all following adjacent numbers
    abs_dif_list = []
    for i, x in enumerate(E):
        if i < (len(E) - 1):
            abs_dif_list.append(abs(x - E[i + 1]))
        else:
            pass
    for i, d in enumerate(abs_dif_list):
        if i < len(abs_dif_list) - 1:
            if d <= abs_dif_list[i + 1]:
                return 'NO'
            else:
                pass
        else:
            pass
    return 'YES'


E = [2, 4, 6]
print(abs_dif(E))

E = [5, 3, 2]
print(abs_dif(E))