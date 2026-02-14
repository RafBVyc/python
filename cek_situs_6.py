import os
import platform

website = input("masukkan nama situs yang ingin di-cek (contoh: google.com): ")
respons = os.system(f"ping -c 1 {website} > /dev/null 2>&1  ")

STATUS = "ONLINE" if respons == 0 else "OFFLINE"

print(f"{website}: {STATUS}")