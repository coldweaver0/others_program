#segitiga sama kaki
baris = int(15)

print("Segitiga bintang sama kaki") 

for i in range(0, baris):
    for j in range(0, baris - i - 1):
        print(end = ' ')
    for k in range(0, i + 1):
        print('*', end = ' ')
    print()