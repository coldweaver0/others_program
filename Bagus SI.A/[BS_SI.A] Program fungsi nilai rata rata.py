#program fungsi nilai rata rata

def Input(daftar):
    list_angka = daftar.split(',')
    daftar_baru = [int(x) for x in list_angka]
 
    jumlah = 0
    for angka in daftar_baru:
        jumlah += angka
    rata_rata = jumlah / len(daftar_baru)
 
    print('Nilai rata-rata: {}'.format(rata_rata))
    
Input (input('masukan list bilangan, pisahkan dengan tanda koma : '))
