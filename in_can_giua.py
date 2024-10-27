

a = input()
my_list = a.split('.')
list_moi = list(map(lambda x: ' '.join(x.split()), my_list))

len_max = 0
for i in list_moi:
    if len(i) > len_max:
        len_max = len(i)

for i in list_moi:
    do_dai_chenh_lech = len_max -len(i)
    khoang_trang_truoc = do_dai_chenh_lech // 2
    print((' ' * khoang_trang_truoc) + i)

