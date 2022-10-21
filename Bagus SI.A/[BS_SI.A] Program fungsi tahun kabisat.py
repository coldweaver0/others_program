#program fungsi tahun kabisat
def kabisat(tahun):
    if tahun % 4 == 0 and tahun != 0:
        print (tahun, "adalah tahun kabisat")
    elif tahun % 100 == 0 :
        print (tahun, "bukan tahun kabisat")
    elif tahun % 400 == 0 :
        print (tahun, "adalah tahun kabisat")
    else:
        print (tahun, "bukan tahun kabisat")
    return

kabisat (int(input("masukkan tahun: ")))