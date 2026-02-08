import platform
import os
import json

#fungsi untuk mengecek sistem operasi dan arsitektur
def cek_sistem():
    print(f"OS: {platform.system()} | Arsitektur: {platform.machine()}")

def cek_situs(daftar_situs):
    for s in daftar_situs:
        respons = os.system(f"ping -c 1 {s} > /dev/null 2>&1")
        if respons == 0:
            print(f"website {s} Online")
        else:
            print(f"website {s} Offline")

#fungsi untuk memuat data server dari file JSON
def load_data():
    try:
        with open("servers.json", "r") as f:
            servers = json.load(f)
    except FileNotFoundError:
        servers = {}
    return servers

#fungsi untuk menyimpan data server ke file JSON
def save_data(data):
    with open("servers.json", "w") as f:
        json.dump(data, f, indent=4)
        
# fungsi untuk menambah server baru
def tambah_server(data):
    nama_baru = input("Masukkan nama server baru: ").strip().lower()
    if nama_baru in data:
        print(f"\n ERROR: Server dengan nama {nama_baru} sudah terdaftar dengan IP {data[nama_baru]}.")
        return

    ip_baru = input(f"Masukkan IP untuk {nama_baru}: ").strip()
    if ip_baru in data.values():
        for nama, ip in data.items():
            if ip == ip_baru:
                print(f"\n ERROR: IP {ip_baru} sudah terdaftar untuk server {nama}.")
                break
        return

    data[nama_baru] = ip_baru
    save_data(data)
    print(f"\nServer {nama_baru} dengan IP {ip_baru} telah ditambahkan.")


# fungsi untuk mencari server dan menambahkannya jika tidak ditemukan
def cari_dan_tambah_server(data):
    print("\n=== Pencarian ===")
    cari = input("ketik nama server yang ingin dicek: ").strip().lower()

    if cari in data:
        print(f"\nditemukan, IP {cari} adalah {data[cari]}\n")   
    else:
        print(f"maaf, {cari} belum terdaftar di server...")
        tambah_kah = input("apa mau ditambahkan sekarang? (y/n): ")
        if tambah_kah == "y":
            ip_tambahan = input(f"masukkan IP untuk {cari}: ")
            data[cari] = ip_tambahan
            save_data(data)
            print(f"\nserver {cari} sudah ditambahkan...\n")
        else:
            print("oke, tidak jadi ditambahkan.\n")

# fungsi untuk menampilkan inventory server
def tampilkan_inventory(data):
    print("=== Inventory Sekarang ===")
    for nama, ip in data.items():
        print(f"- {nama} : {ip}")
