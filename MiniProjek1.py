data_sepatu = []

while True :
    print("\n===== KOLEKSI SEPATU =====")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan menu: ")

    if pilihan == "1":
        while True:
            merek = input("Masukkan merek sepatu (Asics/Adidas/Nike/Puma/Ortuseight): ")

            if merek == "Asics":
                jenis = "Novablast"
                break
            elif merek == "Adidas":
                jenis = "Evo SL"
                break
            elif merek == "Nike":
                jenis = "Vaporfly"
                break
            elif merek == "Puma":
                jenis = "Fast Nitro"
                break
            elif merek == "Ortuseight":
                jenis = "Hyperblast"
                break
            else:
                print("Merek tidak tersedia, silakan masukkan kembali")
        ukuran = input("Masukkan ukuran sepatu: ")
        data_sepatu.append([merek, jenis, ukuran])
        print("Data berhasil ditambahkan.")

    elif pilihan == "2":
        if data_sepatu == []:
            print("Data belum tersedia.")
        else:
            print("===== DATA KOLEKSI SEPATU =====")
            nomor = 1
            for data in data_sepatu:
                print("Data", nomor)
                print("Merek:", data[0])
                print("Jenis:", data[1])
                print("Ukuran:", data[2])
                print()
                nomor = nomor + 1

    elif pilihan == "3":
        if data_sepatu == []:
            print("Data belum tersedia.")
        else:
            nomor = input("Masukkan nomor data yang ingin diubah: ")
            if nomor == "1":
                while True:
                    merek = input("Masukkan merek baru (Asics/Adidas/Nike/Puma/Ortuseight)")
                    if merek == "Asics":
                        jenis = "Novablast"
                        break
                    elif merek == "Adidas":
                        jenis = "Evo SL"
                        break
                    elif merek == "Nike":
                        jenis = "Vaporfly"
                        break
                    elif merek == "Puma":
                        jenis = "Fast Nitro"
                        break
                    elif merek == "Ortuseight":
                        jenis = "Hyperblast"
                        break
                    else:
                        print("Merek tidak tersedia, silakan masukkan kembali. ")
                ukuran = input("Masukkan ukuran baru: ")
                data_sepatu[0] = [merek, jenis, ukuran]
                print("Data berhasil diubah.")
            else:
                print("Data tidak ditemukan")

    elif pilihan == "4":
        if data_sepatu == []:
            print("Data belum tersedia.")
        else:
            nomor = input("Masukkan nomor data yang ingin dihapus: ")
            if nomor == "1":
                del data_sepatu[0]
                print("Data berhasil dihapus.")
            else:
                print("Data tidak ditemukan.")

    elif pilihan == "5":
        print("Program selesai.")
        break 
    else:
        print("Pilihan tidak valid, silakan pilih 1-5.")
