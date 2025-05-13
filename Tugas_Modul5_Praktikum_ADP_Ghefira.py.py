print("Nama : GHEFIRA RHOUDOTUL JANNAAH")
print("NIM  : 2410431002")
print("SHIFT : 2")
print("TUGAS MODUL 5 PRAKTIKUM ADP")
print()

no_pelanggan = []
nama_pelanggan = []
total_belanja = []

while True:
    print("=== MENU UTAMA ===")
    print("1. Update Data")
    print("2. Hapus Data")
    print("3. Cetak Data")
    print("4. Keluar")
    print()

    pilihan = input("Pilih Menu: ")
    print()

    if pilihan == "1":
        print("------ Tambah Data Pelanggan -----")
        no = input("No Pelanggan: ")
        nama = input("Nama Pelanggan: ")
        total = input("Total Belanja: ")

        no_pelanggan.append(no)
        nama_pelanggan.append(nama)
        total_belanja.append(total)
        print("\nData berhasil ditambahkan!\n")

    elif pilihan == "2":
        print("----- Hapus Data -----")
        hapus_no = input("No Pelanggan yang akan dihapus: ")
        
        no_baru = []
        nama_baru = []
        total_baru = []
        ditemukan = False

        for i in range(len(no_pelanggan)):
            if no_pelanggan[i] != hapus_no:
                no_baru.append(no_pelanggan[i])
                nama_baru.append(nama_pelanggan[i])
                total_baru.append(total_belanja[i])
            else:
                ditemukan = True
        
        if ditemukan: 
            no_pelanggan = no_baru
            nama_pelanggan = nama_baru
            total_belanja = total_baru
            print("\nData berhasil dihapus\n")
        else: 
            print("\nNo Pelanggan tidak ditemukan\n")

    elif pilihan == "3":
        print("\n=== Data Pelanggan ===\n")
        if len(no_pelanggan) == 0:
            print("Belum ada data\n")
        else: 
            for i in range(len(no_pelanggan)):
                print(f"{i+1}. No: {no_pelanggan[i]}, Nama: {nama_pelanggan[i]}, Total Belanja: {total_belanja[i]}")

    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini.\n")
        break

    else:
        print("Pilihan tidak valid. Silahkan input ulang.")

