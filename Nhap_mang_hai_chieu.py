

M, N = map(int, input().split())
if M <= 0 or N <= 0:
    print('Vui long nhap kich thuoc danh sach la so nguyen duong!')
else:
    my_list = []
    for i in range(M):
        my_list.append(input().split())

    print(my_list)
    kiem_tra = all(len(my_list[i]) == N for i in range(M))

    print(kiem_tra)
