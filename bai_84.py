def them_phan_tu(x, s):
    ket_qua = []
    for i in range(0, len(s), x):
        ket_qua.extend(s[i: i +x])
        ket_qua.append('Kteam')
    ket_qua.pop()
    return ket_qua


try:
    a = input().split()
    if a == []:
        print('Danh sach rong')
    else:
        n = int(input())
        print(*them_phan_tu(n, a))
except:
    print('Dinh dang dau vao khong hop le')


    




        
    