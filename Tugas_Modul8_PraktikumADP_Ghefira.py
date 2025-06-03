catatan_file = "catatan.txt"
lanjut = True

while lanjut:
    print("\n--- MENU UTAMA ---")
    print("1. Lihat Catatan")
    print("2. Buat Catatan Baru")
    print("3. Exit")
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "2":
        judul = input("Masukkan Judul Catatan: ")
        isi = input("Masukkan Isi Catatan: ")

        f = open(catatan_file, "a")
        f.write(judul + "\n")
        f.write(isi + "\n")
        f.write("-----\n")
        f.close()
        print("Catatan berhasil ditambahkan.")

    elif pilihan == "1":
        f = open(catatan_file, "r")
        isi_file = f.readlines()
        f.close()

        judul_list = []
        i = 0
        while i < len(isi_file):
            baris = isi_file[i]
            kondisi_1 = baris == "-----\n"
            kondisi_2 = i == 0
            kondisi_3 = 1 > 0
            if kondisi_1 == False:
                if kondisi_2:
                    judul_list.append(baris[:-1])
                else:
                    if kondisi_3:
                        if isi_file[i-1] == "-----\n":
                            judul_list.append(baris[:-1])
            i = i + 1
        
        if len(judul_list) == 0:
            print("Belum ada catatan.")
        else:
            print("\nDaftar Judul Catatan: ")
            for j in judul_list:
                print("-", j)

            cari = input("Judul catatan yang ingin dilihat: ")
            i = 0
            ditemukan = False

            print("\nIsi Catatan dengan judul: ", cari)
            # print("------------------------------")
            while True:
                cukup = i + 2 < len(isi_file)
                if cukup == False:
                    break

                sama = isi_file[i][:-1] == cari
                pemisah = isi_file[i+2] == "-----\n"

                if sama:
                    if pemisah:
                        print("-->", isi_file[i+1][:-1])
                        ditemukan = True
                i = i + 1

            kosong = ditemukan == False
            if kosong:
                print("Judul catatan tidak ditemukan.")

    elif pilihan == "3":
        print("\nProgram selesai. Terima Kasih!")
        lanjut = False

    else:
        print("\nPilihan tidak valid.")