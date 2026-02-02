from func import cek_sistem
from func import cek_situs

list_tujuan = ["music.youtube.com", "github.com"]

while True:
    print("\n=== DEVOPS MINI TOOL ===")
    print("1. Cek Info Sistem")
    print("2. Cek Koneksi Website")
    print("3. Keluar")
    print("4. Cek Log_File")

    pilihan = input("pilihan menu (1/2/3/4): ")

    if pilihan == "1":
        cek_sistem()
    elif pilihan == "2":
        cek_situs(list_tujuan)
    elif pilihan == "3":
        print("program mati")
        break
    elif pilihan == "4":
        with open("log_server.txt", "r") as f:
            isi_log = f.read()
            print("\n--- ISI LOG FILE ---")
            print(isi_log)
            print("--------------------\n")
    else:
        print("pilihan tidak dikenal")