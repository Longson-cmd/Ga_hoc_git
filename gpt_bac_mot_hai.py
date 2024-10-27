


import math
# nhập các giá trị đầu vào
dong_mot = int(input())
dong_hai = input()
# hàm giải phương trình bậc 1
def gpt_bac_mot(a,b):   
    if a == 0:
        if b == 0:
            return 'phuong trinh co vo so nghiem!'
        return 'phuong trinh vo nghiem!'
    
    return f'Phuong trinh co mot nghiem duy nhat x = {-b/a}'
       
# hàm giải phương trình bậc 2
def gpt_bac_hai(a,b,c):
    delta = b*b - 4*a*c
    if a == 0:
        return gpt_bac_mot(b,c)
    if delta < 0:
        return 'Phuong trinh vo nghiem'
    elif delta == 0:
        return f'Phuong trinh co nghiem kep: x1 = x2 = {-b/(2*a)}'
    return f'Phuong trinh co hai nghiem phan biet la:\nx1 = {(-b +math.sqrt(delta))/(2*a)}\nx2 = {(-b - math.sqrt(delta))/(2*a)}'

# in kết quả
if dong_mot == 1:
    a, b = map(float, dong_hai.split())
    print(gpt_bac_mot(a,b))
elif dong_mot == 2:
    a, b, c = map(float, dong_hai.split())
    print(gpt_bac_hai(a,b,c))
else:
    print('Vui long chon mot trong hai chuc nang:\n1. Giai phuong trinh bac nhat\n2. Giai phuong trinh bac hai')




       



    