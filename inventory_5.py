# Database server sederhana dalam bentuk dictionary


from func_3 import tambah_server, cari_dan_tambah_server, tampilkan_inventory, load_data, hapus_server, cek_situs_input, cek_status_server

inventory_data = load_data()



while True:
    print("==== pilihan menu =====")
    print("1. Menambah Server terbaru")
    print("2. Pencarian Server ")
    print("3. Cek Status Semua Server")
    print("4. Tampilkan Inventory")
    print("5. Hapus Server")
    print("6. Cek Situs")
    print("7. Keluar")

    try:
        pilihan = input("Pilih menu (1/2/3/4/5/6/7): ")
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh user.")
        break
    if pilihan == "1":
        tambah_server(inventory_data)
    elif pilihan == "2":
        cari_dan_tambah_server(inventory_data)
    elif pilihan == "3":
        cek_status_server(inventory_data)
    elif pilihan == "4":
        tampilkan_inventory(inventory_data)
    elif pilihan == "5":
        hapus_server(inventory_data)
    elif pilihan == "6":
        cek_situs_input()
    elif pilihan == "7":
        print("\n Program dihentikan")
        break
    else:
        print("\nPilihan tidak valid, silakan coba lagi.\n")