#program ganjil genap

nilai_awal = int(input('Masukkan nilai awal: '))
nilai_akhir = int(input('Masukkan nilai akhir: '))

print("""Tampilkan bilangan
 1. Ganjil
 2. Genap""")

pilihan = int(input('Pilihan: '))
if pilihan not in [1, 2]:
  print('Pilihan salah')
else:
  for x in range(nilai_awal, nilai_akhir + 1):
    if pilihan == 1 and x % 2 == 1:
      print(x, end=' ')
    elif pilihan == 2 and x % 2 == 0:
      print(x, end=' ')
  else:
    print('')
  
