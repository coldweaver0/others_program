# program ketupat
baris = int(15)

print("Ketupat") 

for i in range(0, baris):
    for j in range(0, baris - i - 1):
        print(end = ' ')
    for k in range(0, i + 1):
        print('*', end = ' ')
    print()
for i in range(0, baris):
    for j in range(0, i + 1):
        print(end = ' ')
    for k in range(0, baris - i - 1):
        print('*', end = ' ')
    print()