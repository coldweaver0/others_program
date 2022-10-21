def fungsi(a):

    for x in range(1, a + 1):
        if pilihan == 1 and x % 2 == 1:
            print(x, end=' ')
        elif pilihan == 2 and x % 2 == 0:
            print(x, end=' ')
        else:
            print('')
pilihan = int(input("masukkan pilihan ganjil(1) genap(2): "))
fungsi (int(input("masukkan angka: ")))
