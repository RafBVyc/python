# Database server sederhana dalam bentuk dictionary

servers = {
    "web" : "192.168.1.10",
    "db"  : "192.168.1.20",
    "app" : "192.168.1.30"
}

nama = input("Masukkan nama server (web/db/app): ").lower()

if nama in servers:
    print(f"IP address server {nama} adalah {servers[nama]}")
else:
    print("Server tidak ditemukan dalam database.")