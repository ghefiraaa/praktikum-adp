print("==============================")
print("  MENGHITUNG TAGIHAN LISTRIK  ")
print("==============================")

def hitung_tagihan(pemakaian, golongan=3):
    tarif = [ [1500, 2000], [2500, 3000], [4000, 5000], [5000, 7000]]   #data [tarif awal, tarif setelah 100kWh]

    #validasi golongan (jika tidak ada, gunakan golongan 3)
    if golongan < 1 or golongan > 4:
        golongan = 3

    tarif_awal = tarif[golongan - 1][0]     #dikurang 1, karena indeks dimulai 0
    tarif_lanjut = tarif[golongan - 1][1]
    
    #perhitungan pemakaian listrik
    tagihan = 0
    
    if pemakaian <= 100:
        tagihan = pemakaian * tarif_awal
    else:
        tagihan = 100 * tarif_awal + (pemakaian -100) * tarif_lanjut
    return tagihan

pemakaian_list = []
golongan_list = []

jumlah_pelanggan = int(input("Jumlah pelanggan: "))

for i in range(jumlah_pelanggan):
    print(f"\nData pelanggan ke-{i+1}")
    kWh = int(input("Pemakaian listrik (kWh): "))
    gol = input("Golongan tarif (1-4): ")

    pemakaian_list.append(kWh)

    #jika input golongan kosong, gunakan golongan 3
    if gol == "":
        golongan_list.append(3)
    else:
        golongan_list.append(int(gol))

print("\n----- HASIL TAGIHAN LISTRIK -----")
for i in range(jumlah_pelanggan):
    tagihan = hitung_tagihan(pemakaian_list[i], golongan_list[i])
    print(f"Pelanggan {i+1}: Rp. {tagihan:,}")