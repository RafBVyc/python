import platform
import os

def cek_sistem():
    print(f"OS : {platform.system()} | Arsitektur : {platform.machine()}")

def cek_situs(daftar_web):
    for w in daftar_web:
        respons = os.system(f"ping -c 1 {w} > /dev/null 2>&1")
        status = "ONLINE" if respons == 0 else "OFFLINE"
        print(f"{w} -> {status}")