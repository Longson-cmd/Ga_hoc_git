

my_list = input().split()
my_dict = {}
for tu in my_list:
    if tu in my_dict:
        my_dict[tu].append(tu)
    else:
        my_dict[tu] = [tu]


print(my_dict)