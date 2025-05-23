print("===========================================")
print("|     PROGRAM HITUNG JARAK ANTAR TITIK    |")
print("===========================================")

# INPUT JUMLAH TITIK
n = 0
while n <= 0:
    n_input = input("Masukkan jumlah titik (n): ")
    print()
    hanya_angka = True
    for c in n_input:
        if c < '0' or c > '9':
            hanya_angka = False
            break
    if hanya_angka:
        n = int(n_input)
        if n <= 0:
            print("n harus lebih dari 0!")
    else:
        print("Input tidak valid! Masukkan angka bulat positif.")

# INPUT MASING-MASING TITIK
titik = []
for i in range(n):
    valid = False
    while not valid:
        x_input = input("Masukkan x untuk titik ke-{}: ".format(i+1))
        y_input = input("Masukkan y untuk titik ke-{}: ".format(i+1))

        valid_x = True
        valid_y = True

        if x_input == "" or (x_input[0] == '-' and len(x_input) == 1):
            valid_x = False
        else:
            for j in range(len(x_input)):
                if j == 0 and x_input[j] == '-':
                    continue
                if x_input[j] < '0' or x_input[j] > '9':
                    valid_x = False
                    break

        if y_input == "" or (y_input[0] == '-' and len(y_input) == 1):
            valid_y = False
        else:
            for j in range(len(y_input)):
                if j == 0 and y_input[j] == '-':
                    continue
                if y_input[j] < '0' or y_input[j] > '9':
                    valid_y = False
                    break

        if valid_x and valid_y:
            x = int(x_input)
            y = int(y_input)
            titik.append([x, y])
            valid = True
        else:
            print("Koordinat tidak valid! Harus angka bulat (boleh negatif).")

# MENAMPILKAN KUMPULAN TITIK
print("    \nKumpulan Titik:   ")
print("-------------------------")
for i in range(n):
    print("Titik {}: ({}, {})".format(i+1, titik[i][0], titik[i][1]))

# HITUNG JARAK ANTAR TITIK
print("   \nJarak antar titik:    ")
print("-------------------------")
for i in range(n):
    for j in range(i + 1, n):
        dx = titik[j][0] - titik[i][0]
        dy = titik[j][1] - titik[i][1]
        jarak = (dx * dx + dy * dy) ** 0.5
        print("Jarak Titik {} ke Titik {} = {:.2f}".format(i + 1, j + 1, jarak))
    