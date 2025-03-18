n = int(input("masukkan nilai n: "))
a = 1   #batas bawah
b = 3   #batas atas
delta_x = (b-a)/n
luas = 0
for i in range (1, n+1):
    xi = a + i * delta_x
    #fx = x**2 + 2*x
    fxi = xi**2 + 2*xi
    luas += fxi * delta_x

print(f"Luas daerah dari fungsi x**2 + 2*x dengan batas daerah {a} dan {b} dan jumlah partisi {n} adalah {luas}")

