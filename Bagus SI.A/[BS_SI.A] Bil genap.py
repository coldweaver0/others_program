#program menampilkan bilangan  genap 1 - 100
nilai_awal = 0
nilai_akhir = 100


for x in range(nilai_awal, nilai_akhir + 1):
    if x % 2 == 0:
        print(x ,end=" ")
    else:
        print("")