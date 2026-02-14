# Database server sederhana dalam bentuk dictionary


from func_3 import tambah_server, cari_dan_tambah_server, tampilkan_inventory, load_data, hapus_server, cek_situs_input

inventory_data = load_data()



while True:
    print("==== pilihan menu =====")
    print("1. Menambah Server terbaru")
    print("2. Pencarian Server ")
    print("3. Keluar")
    print("4. Tampilkan Inventory")
    print("5. Hapus Server")
    print("6. Cek Internet")

    try:
        pilihan = input("Pilih menu (1/2/3/4): ")
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh user.")
        break

    if pilihan == "1":
        tambah_server(inventory_data)
    elif pilihan == "2":
        cari_dan_tambah_server(inventory_data)
    elif pilihan == "3":
        print("\nProgram berakhir")
        break
    elif pilihan == "4":
        tampilkan_inventory(inventory_data)
    elif pilihan == "5":
        hapus_server(inventory_data)
    elif pilihan == "6":
        cek_situs_input()
    else:
        print("\nPilihan tidak valid, silakan coba lagi.\n")