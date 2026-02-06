# Database server sederhana dalam bentuk dictionary

from func_3 import tambah_server, cari_dan_tambah_server, tampilkan_inventory

servers = {
    "web" : "192.168.1.10",
    "db"  : "192.168.1.20",
    "app" : "192.168.1.30"
}

while True:    
    print("==== pilihan menu =====")
    print("1. Menambah Server terbaru")
    print("2. Pencarian Server ")
    print("3. Keluar")
    print("4. Tampilkan Inventory")
    
    try:    
        pilihan = input("Pilih menu (1/2/3/4): ")
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh user.")
        break
        
    if pilihan == "1":
        tambah_server()
    elif pilihan == "2":
        cari_dan_tambah_server()
    elif pilihan == "3":
        print("\nProgram berakhir")
        break
    elif pilihan == "4":
        tampilkan_inventory()
    else:
        print("\nPilihan tidak valid, silakan coba lagi.\n")