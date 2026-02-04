from func import cek_sistem, cek_situs

daftar_situs = ["google.com", "github.com", "nonexistentsite.xyz"]

while True:
    print("======= Menu =======")
    print("1. Cek Sistem")
    print("2. Cek Situs")
    print("3. cek log file")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "1":
        cek_sistem()
    elif pilihan == "2":
        cek_situs(daftar_situs)
    elif pilihan == "3":
        with open("log_server.txt", "r") as f:
            isi_log = f.read()
            print("\n=== Isi Log File ===")
            print(isi_log)
            print("======================")
    elif pilihan == "4":
        print("Program berakhir")
        break