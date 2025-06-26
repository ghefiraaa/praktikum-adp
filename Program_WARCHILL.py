import time
import os
from termcolor import colored

# ==== CLEAR SCREEN ====
def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()

# ==== DATA MENU ====
menu_makanan = {
    1: {"nama": "Nasi Sultan", "deskripsi menu": "Nasi + ayam goreng kremes + telur dadar + sambal terasi + sayur lalapan", "harga": 20000, "waktu": 12},
    2: {"nama": "Nasi Kuli", "deskripsi menu": "Nasi + tempe orek + telur ceplok + sayur asem", "harga": 18000, "waktu": 12},
    3: {"nama": "Nasi Kece", "deskripsi menu": "Nasi + ayam geprek mozarella + sambal matah", "harga": 20000, "waktu": 12},
    4: {"nama": "Nasi Quarter Life Crisis", "deskripsi menu": "Nasi + ayam serundeng + telur balado + sayur lodeh", "harga": 18000, "waktu": 12},
    5: {"nama": "Paket Anak Kost", "deskripsi menu": "Nasi + mie goreng + tahu/tempe + sambal terasi", "harga": 10000, "waktu": 8},
    6: {"nama": "Nasi Circle Toxic", "deskripsi menu": "Nasi + kikil pedas + sambal terasi + kerupuk", "harga": 15000, "waktu": 10},
    7: {"nama": "Nasi Jamet Pedas", "deskripsi menu": "Nasi + ceker mercon + daun singkong + sambal setan", "harga": 15000, "waktu": 8},
    8: {"nama": "Nasi Auto Kenyang", "deskripsi menu": "Porsi jumbo nasi + ayam bakar + lalapan + sambal ijo", "harga": 18000, "waktu": 12}
}

menu_minuman = {
    9: {"nama": "Es Teh Vibes", "deskripsi menu": "Es teh manis khas warteg, segar murah", "harga": 5000, "waktu": 3},
    10: {"nama": "Lemonade Healing", "deskripsi menu": "Es lemon peras + madu", "harga": 6000, "waktu": 3},
    11: {"nama": "Kopi Susu Ngab", "deskripsi menu": "Kopi susu gula aren", "harga": 10000, "waktu": 8},
    12: {"nama": "Es Cincau Santuy", "deskripsi menu": "Cincau hitam + susu + es batu", "harga": 8000, "waktu": 3},
    13: {"nama": "Es Duren No Debat", "deskripsi menu": "Durian + santan + sirup + es", "harga": 10000, "waktu": 10}
}

menu_cemilan = {
    14: {"nama": "Tempe Chips Zone", "deskripsi menu": "Tempe goreng kriuk", "harga": 8000, "waktu": 10},
    15: {"nama": "Sosis Molor", "deskripsi menu": "Sosis goreng isi mozarella", "harga": 12000, "waktu": 15},
    16: {"nama": "Tahu Buzzer", "deskripsi menu": "Tahu pedas cabe bendot", "harga": 5000, "waktu": 7},
    17: {"nama": "Bakwan Closingan", "deskripsi menu": "Bakwan sayur kres nyes", "harga": 8000, "waktu": 15},
    18: {"nama": "Kentang Nyes", "deskripsi menu": "Kentang goreng garing mantul", "harga": 13000, "waktu": 5}
}

semua_menu = {**menu_makanan, **menu_minuman, **menu_cemilan}

# ==== ANIMASI LOADING ====
def loading_bar(teks="Sedang diproses", durasi=7):
    print(f"\n{teks}")
    for i in range(20):
        print("=", end="", flush=True)
        time.sleep(durasi / 20)
    print("\n" + colored("BERHASIL!", "green", attrs=["bold"]))
    print(colored("Tunjukkan struk utuk melakukan pembayaran.", "magenta"))

# ==== JUDUL ====
def judul():
    print("\n" + "="*45)
    print(colored(colored(" =====> ", "red") + colored("SELAMAT DATANG DI ", "white") + colored("WARCHILL!", "magenta", attrs=["bold"]) + colored(" <===== ", "red")))
    print(colored("WARteg Chill - KENIKMATAN DALAM KESEDERHANAAN", "green"))
    print("="*45)

# ==== TAMPILKAN MENU ====
def tampilkan_menu(jenis):
    if jenis == "makanan":
        print(colored("\nM E N U  M A K A N A N", "yellow", attrs=["bold"]))
        tampilkan_list = menu_makanan
    elif jenis == "minuman":
        print(colored("\nM E N U  M I N U M A N", "yellow", attrs=["bold"]))
        tampilkan_list = menu_minuman
    elif jenis == "cemilan":
        print(colored("\nMENU  C E M I L A N", "yellow", attrs=["bold"]))
        tampilkan_list = menu_cemilan
    else:
        return

    for nomor_menu, menu in tampilkan_list.items():
        print(f"{nomor_menu}. {menu['nama']} - Rp {menu['harga']} ({menu['waktu']} menit)")
        print(colored(f"   {menu['deskripsi menu']}", "grey"))

# ==== TAHAP PEMESANAN ====
def pemesanan():
    pesanan = []
    total_harga = 0
    total_waktu = 0

    while True:
        print("\n" + colored("PILIH KATEGORI MENU: ", "cyan", attrs=["bold"]))
        print(colored("1. Makanan", "white"))
        print(colored("2. Minuman", "white"))
        print(colored("3. Cemilan", "white"))
        print(colored("4. Selesai dan Checkout", "white"))

        pilih = input(colored("Masukkan Pilihan Anda: ", "grey"))
        if pilih == "1":
            tampilkan_menu("makanan")
        elif pilih == "2":
            tampilkan_menu("minuman")
        elif pilih == "3":
            tampilkan_menu("cemilan")
        elif pilih == "4":
            if pesanan:
                print(colored("\nRINCIAN PEMESANAN ANDA:", "cyan", attrs=["bold", "underline"]))
                for item in pesanan:
                    print(f"- {item[0]} x {item[1]} = Rp {item[2] * item[1]}")
                print(colored(f"\nTotal Harga           : Rp. {total_harga}", "yellow", attrs = ["bold"]))
                print(colored(f"Estimasi Waktu Tunggu   : {total_waktu} menit", "yellow", attrs=["bold"]))

                print("\n" + "="*40)
                print(colored(" STRUK PEMESANAN WARCHILL ", "cyan", attrs=["bold"]))
                print("="*40)
                for item in pesanan:
                    nama, jumlah, harga, waktu = item
                    subtotal = harga * jumlah
                    print(f"{nama:<25} x{jumlah:<2}  Rp{subtotal}")
                print("-"*40)
                print(colored(f"Total Harga        : Rp {total_harga}", "yellow"))
                print(colored(f"Estimasi Waktu     : {total_waktu} menit", "yellow"))
                print(colored(f"Waktu Pesan        : {time.ctime()}", "grey"))  
                print("="*40)
                print(colored("Terima kasih sudah chill di WARCHILL", "green"))

                loading_bar("Pesanan sedang diproses")

                with open("pesananchill.txt", "w") as f:
                    for item in pesanan:
                        f.write(f"{item[0]} | {item[1]} | {item[2]} | {item[3]}\n")
                    f.write(f"TOTAL | {total_harga} | {total_waktu}")
                break
            else:
                print(colored("Belum ada pesanan yang dipilih.", "red"))
                continue
        else:
            print(colored("Pilihan Tidak Valid. COBA LAGI!", "red"))
            continue

        nomor_menu = input(colored("\nMasukkan Nomor Menu: ", "grey"))
        if nomor_menu.isdigit() and int(nomor_menu) in semua_menu:
            nomor = int(nomor_menu)
            jumlah_input = input(colored(f"Banyak porsi {semua_menu[nomor]['nama']}: ", "grey"))
            if jumlah_input.isdigit() and 1 <= int(jumlah_input) < 100:
                jumlah = int(jumlah_input)
                pesanan.append((semua_menu[nomor]["nama"], jumlah, semua_menu[nomor]["harga"], semua_menu[nomor]["waktu"]))
                total_harga += semua_menu[nomor]["harga"] * jumlah
                total_waktu += semua_menu[nomor]["waktu"] * jumlah
                print(colored(f"{semua_menu[nomor]['nama']} x {jumlah} berhasil ditambahkan!", "green"))
            else:
                print(colored("Jumlah Tidak Valid.", "red"))
        else:
            print(colored("Nomor Menu Tidak Ditemukan!", "red"))

# ==== PEMANGGILAN JUDUL ====
def main():
    judul()
    print("\n" + colored("      M E N U  U T A M A      ", "cyan", attrs=["bold", "underline"]))
    print(colored("1. Lihat Menu dan Pesan", "white"))
    print(colored("2. Keluar", "white"))

    pilih = input(colored("Pilih Menu: ", "grey"))
    if pilih == "1":
        pemesanan()
    elif pilih == "2":
        print(colored("Thank You! Datang lagi ya ke WARCHILL~~", "cyan"))
    else:
        print(colored("Pilihan tidak dikenali.", "red"))

main()
