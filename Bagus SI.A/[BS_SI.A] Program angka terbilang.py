#program angka terbilang
def Terbilang(bil):
    angka = ["nol","Satu","Dua","Tiga","Empat","Lima","Enam",
             "Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
    Hasil = ""
    n = int(bil)
    if n>= 0 and n <= 11:
        Hasil = angka[n]
    elif n <20:
        Hasil = Terbilang (n-10) + " Belas "
    elif n <100:
        Hasil = Terbilang (n/10) + " Puluh " + Terbilang (n%10)
    else:
        Hasil = "Angka Hanya Sampai Seratus"
    return Hasil
a=1
while a!= 0:
    a = input('Masukan angka dari 0 sampai 99: ')
    huruf = Terbilang(a)
    print (''+huruf)
    

