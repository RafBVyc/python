import platform
import os

sistem = platform.system()
arsitektur = platform.machine()

print(f"--- LAPORAN SISTEM ---")
print(f"OS: {sistem}")
print(f"Arsitektur: {arsitektur}")

if sistem == "Linux":
    print("Studi DevOps dimulai di habitat aslinya!")
elif sistem == "Windows":
    print("Gunakan WSL atau segera pindah ke Linux!")

print("\nMengecek koneksi internet...")

# os.system akan menjalankan perintah 'ping' di terminal
# -c 1 artinya hanya mengirim 1 paket saja agar cepat
respons = os.system("ping -c 1 google.com > /dev/null 2>&1")

if respons == 0:
    print("Internet: Terhubung (Online)")
else:
    print("Internet: Terputus (Offline)")