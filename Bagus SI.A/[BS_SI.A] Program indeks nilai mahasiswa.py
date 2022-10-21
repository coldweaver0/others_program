#program indeks nilai mahasiswa
def indeks(a,b,c):
    nilai_akhir = (0.3*a)+(0.35*b)+(0.35*c)

    if nilai_akhir == 80-100:
        indeks="A"
    elif nilai_akhir == 70-80:
        indeks="B"
    elif nilai_akhir == 55-70:
        indeks="C"
    elif nilai_akhir == 40-55:
        indeks="D"
    else:
        indeks="E"

    print (nilai_akhir)
    print (indeks)

indeks (a = int(input("masukkan nilai tugas: ")), b=int(input("masukkan nilai uts: ")), c=int(input("masukkan nilai uas: ")))