import platform
import os

def cek_sistem():
    print(f"OS: {platform.system()} | Arsitektur: {platform.machine()}")

def cek_situs(daftar_situs):
    for s in daftar_situs:
        respons = os.system(f"ping -c 1 {s} > /dev/null 2>&1")
        if respons == 0:
            print(f"website {s} Online")
        else:
            print(f"website {s} Offline")
