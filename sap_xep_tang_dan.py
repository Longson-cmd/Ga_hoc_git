


def sap_xep_day(s):
    try:
        list_s = list(map(float, s))
        list_tan_dan = 0
        if list_s != []:
            for i in range(len(list_s)):
                for k in range(i, len(list_s)):
                    if list_s[i] > list_s[k]:
                        trung_gian = list_s[i]
                        list_s[i] = list_s[k]
                        list_s[k] = trung_gian
            return ' '.join(map(str, list_s))
        return 'Danh sach rong'
    except:
        return 'Vui long nhap cac phan tu la so thuc!'
    
a = input().split()
print(sap_xep_day(a))
    








 



   


    

        

    