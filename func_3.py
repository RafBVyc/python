import platform
import os
import json

def cek_sistem():
    print(f"OS: {platform.system()} | Arsitektur: {platform.machine()}")

def cek_situs(daftar_situs):
    for s in daftar_situs:
        respons = os.system(f"ping -c 1 {s} > /dev/null 2>&1")
        if respons == 0:
            print(f"website {s} Online")
        else:
            print(f"website {s} Offline")

def load_data():
    try:
        with open("servers.json", "r") as f:
            servers = json.load(f)
    except FileNotFoundError:
        servers = {}
    return servers

def save_data(servers):
    with open("servers.json", "w") as f:
        json.dump(servers, f, indent=4)

def tambah_server(servers):
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

def cari_dan_tambah_server(servers):
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

def tampilkan_inventory(servers):        
    print("=== Inventory Sekarang ===")
    for nama, ip in servers.items():
        print(f"- {nama} : {ip}")
