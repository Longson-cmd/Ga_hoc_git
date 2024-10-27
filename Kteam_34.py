# " r ",for reading
# " w ", for writng
# " a ", for appending
# " r+ ", for both reading and writing

isOK = False
try:
    x = float(input('nhap so x: '))
    n = int(input('nhap so n: '))
    isOK = True
except:
    print('dinh dang dau vao khong hop le')

tong = 1

if isOK == True:
    if n < 0 :
        print('Vui long nhap n la so tu nhien')
    elif n == 0:
        print(1)
    else:
        for i in range(1, 2*n +1):
            giai_thua = 1
            for k in range (1, i +1):
                giai_thua *= k
            tong += (x**i) * (-1)**i / giai_thua
        print(tong)

            
        