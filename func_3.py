import platform
import os
import json 
from datetime import datetime

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
    while True:
        nama_baru = input("Masukkan nama server baru: ").strip().lower()
        if not nama_baru:
            print("Nama server tidak boleh kosong. Silakan coba lagi.")
            continue
        if nama_baru in data:
            print(f"\nERROR: Server dengan nama {nama_baru} sudah terdaftar dengan IP {data[nama_baru]}.")
            continue
        break

    while True:
        ip_baru = input(f"Masukkan IP untuk {nama_baru}: ").strip()
        if not ip_baru:
            print("IP tidak boleh kosong. Silakan coba lagi.")
            continue
        if ip_baru.count(".") != 3 :
            print("Format IP tidak valid. Pastikan formatnya seperti 192.168.1.1")
            continue
        if ip_baru in data.values():
            for nama, ip in data.items():
                if ip == ip_baru:
                    print(f"\n ERROR: IP {ip_baru} sudah terdaftar untuk server {nama}.")
                    break
            continue
        break

    data[nama_baru] = ip_baru
    save_data(data)
    tulis_log(f"Menambahkan server baru: {nama_baru} dengan IP {ip_baru}")
    print(f"\nServer {nama_baru} dengan IP {ip_baru} berhasil disimpan.")


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
            tulis_log(f"Menambahkan server baru: {cari} dengan IP {ip_tambahan}")
            print(f"\nserver {cari} sudah ditambahkan...\n")
        else:
            print("oke, tidak jadi ditambahkan.\n")

# fungsi untuk menampilkan inventory server
def tampilkan_inventory(data):
    print("=== Inventory Sekarang ===")
    for nama, ip in data.items():
        print(f"- {nama} : {ip}")

def tulis_log(pesan):
    # Mengambil waktu saat ini dengan format: Tahun-Bulan-Hari Jam:Menit:Detik
    waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # menulis ke file activity.log
    with open("activity.log", "a") as f:
        f.write(f"[{waktu_sekarang}] {pesan}\n")
