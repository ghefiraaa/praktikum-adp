print("=== Selamat Datang di Toserba Gepzchill ===")

print("~~~ Daftar Barang dan Harga ~~~")
print("1. Beras : 95000")
print("2. Minyak Goreng : 90000")
print("3. Gula : 85000")
print("4. Susu : 80000")
print("5. Telur : 75000")
print("6. Garam : 70000")
print("7. Kopi : 65000")
print("8. Mie Instan : 60000")
print("9. Tepung Terigu : 55000")
print("10. Teh : 50000")

pilih = int(input("\nPilih nomor barang yang ingin dibeli: "))

if pilih == 1:
    nama_barang = "Beras"
    harga_satuan = 95000
elif pilih == 2:
    nama_barang = "Minyak Goreng"
    harga_satuan = 90000
elif pilih == 3:
    nama_barang = "Gula"
    harga_satuan = 85000
elif pilih == 4:
    nama_barang = "Susu"
    harga_satuan = 80000
elif pilih == 5:
    nama_barang = "Telur"
    harga_satuan = 75000
elif pilih == 6:
    nama_barang = "Garam"
    harga_satuan = 70000
elif pilih == 7:
    nama_barang = "Kopi"
    harga_satuan = 65000
elif pilih == 8:
    nama_barang = "Mie Instan"
    harga_satuan = 60000
elif pilih == 9:
    nama_barang = "Tepung Terigu"
    harga_satuan = 55000
elif pilih == 10:
    nama_barang = "Teh"
    harga_satuan = 50000
else:
    print("Pilihan tidak valid.")

jumlah = int(input(f"Masukkan jumlah {nama_barang} yang ingin dibeli: "))

harga_total = harga_satuan * jumlah

if harga_total < 1000000:
    diskon = 0
elif 1000000 <= harga_total <= 1500000:
    diskon = harga_total * 0.10
else:
    diskon = harga_total * 0.15

total_bayar = harga_total - diskon

print("\n~~~ Struk Pembelian ~~~")
print(f"Nama Barang     : {nama_barang}")
print(f"Jumlah          : {jumlah}")
print(f"Harga Satuan    : {harga_satuan}")
print(f"Harga Total     : {harga_total}")
print(f"Potongan Harga  : Rp{int(diskon)}")
print(f"Total Bayar     : Rp{int(total_bayar)}")
print("Terimakasih sudah berbelanja, dan jangan lupa untuk mampir kembali:> ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")