D_mb = float(1.44) #инф объем (в мбайтах)
D_by = float(1.44*(1024**2)) #инф объем (в байтах)
ST = 100 # страницы
st = 50 # строки
s = 25 # символы
c_by = 4 # инф объем кода символа (в байтах)

DK_by = ST*st*s*c_by #инф объем одной книги (в байтах)
N = int(D_by//DK_by)






print("Количество книг, помещающихся на дискету:", N)