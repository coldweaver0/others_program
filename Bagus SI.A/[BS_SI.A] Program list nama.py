#program list nama
namelist = []
nimlist = []
jklist = []
prolist = []
tllist = []


name = input("Masukkan nama: ")
namelist.append(name)
name = input("Masukkan nim: ")
nimlist.append(name)
name = input("Masukkan jenis kelamin: ")
jklist.append(name)
name = input("Masukkan prodi: ")
prolist.append(name)
name = input("Masukkan tanggal lahir: ")
tllist.append(name)

current = 0
if len(namelist) > 0 :
    while current < len(namelist):
        print (current, ".", namelist[current])
        current = current + 1
else:
    print ("List Kosong")

current = 0
if len(nimlist) > 0 :
    while current < len(nimlist):
        print (current, ".", nimlist[current])
        current = current + 1
else:
    print ("List Kosong")

current = 0
if len(jklist) > 0 :
    while current < len(jklist):
        print (current, ".", jklist[current])
        current = current + 1
else:
    print ("List Kosong")

current = 0
if len(prolist) > 0 :
    while current < len(prolist):
        print (current, ".", prolist[current])
        current = current + 1
else:
    print ("List Kosong")

current = 0
if len(tllist) > 0 :
    while current < len(tllist):
        print (current, ".", tllist[current])
        current = current + 1
else:
    print ("List Kosong")