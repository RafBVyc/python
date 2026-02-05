# Database server sederhana dalam bentuk dictionary
servers = {
    "web" : "192.168.1.10",
    "db"  : "192.168.1.20",
    "app" : "192.168.1.30"
}


def tambah_server():
    nama_baru = input("Masukkan nama server baru: ").strip().lower()

    if nama_baru in servers:
        print(f"\n ERROR: Server dengan nama {nama_baru} sudah terdaftar dengan IP {servers[nama_baru]}.")
        return

    ip_baru = input(f"Masukkan IP untuk {nama_baru}: ").strip()

    if ip_baru in servers.values():
        pemilik = [nama for nama, ip in servers.items() if ip == ip_baru][0]
        print(f"\n ERROR: IP {ip_baru} sudah digunakan oleh server lain.")
        return

    servers[nama_baru] = ip_baru
    print(f"\nServer {nama_baru} dengan IP {ip_baru} telah ditambahkan.")

def cari_dan_tambah_server():
    print("\n=== Pencarian ===")
    cari = input("ketik nama server yang ingin dicek: ").strip().lower()

    if cari in servers:
        print(f"\nditemukan, IP {cari} adalah {servers[cari]}\n")
    else:
        print(f"maaf, {cari} belum terdaftar di server...")
        tambah_kah = input("apa mau ditambahkan sekarang? (y/n): ")
        if tambah_kah == "y":
            ip_tambahan = input(f"masukkan IP untuk {cari}: ")
            servers[cari] = ip_tambahan
            print(f"\nserver {cari} sudah ditambahkan...\n")
        else:
            print("oke, tidak jadi ditambahkan.\n")

def tampilkan_inventory():        
    print("=== Inventory Sekarang ===")
    for nama, ip in servers.items():
        print(f"- {nama} : {ip}")

    # print("\nInventory Akhir:", servers)

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