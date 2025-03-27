n = int(input("Masukkan Jumlah Pendaftar: "))
for i in range(n):
    print(f"Data Pendaftar ke- {i+1}")
    nama = input("Nama: ")
    mata_kuliah = input("Mata Kuliah yang  diminati: ")

    penilaian_wawancara = 0
    while penilaian_wawancara < 1:
         penilaian_wawancara = float(input("Penilaian wawancara (1-100): "))
         if penilaian_wawancara < 1:
            print("Nilai harus diantara 1-100. Silahkan input ulang.")
         if penilaian_wawancara > 100:
            print("Nilai harus diantara 1-100. Silahkan input ulang.")
            penilaian_wawancara = 0

    penilaian_tes_tulis = 0
    while penilaian_tes_tulis < 1:
        penilaian_tes_tulis = float(input("Penilaian tes tulis (1-100): "))
        if penilaian_tes_tulis < 1:
            print("Nilai harus diantara 1-100. Silahkan input ulang.")
        if penilaian_tes_tulis > 100:
            print("Nilai harus diantara 1-100. Silahkan input ulang. ")
            penilaian_tes_tulis = 0

    penilaian_mengajar = 0
    while penilaian_mengajar < 1:
        penilaian_mengajar = float(input("Penilaian mengajar (1-100): "))
        if penilaian_mengajar < 1:
            print("Nilai harus diantara 1-100. Silahkan input ulang.")
        if penilaian_mengajar > 100:
            print("Nilai harus diantara 1-100. Silahkan input ulang.")
            penilaian_mengajar = 0

    total_penilaian = penilaian_wawancara + penilaian_tes_tulis + penilaian_mengajar
    rata_rata = total_penilaian / 3
    print(f"{rata_rata}")
    if rata_rata > 80:
        predikat = "LULUS"
    else:
        predikat = "TIDAK LULUS"
    print(predikat)
    print()