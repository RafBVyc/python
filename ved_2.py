import os
import platform

website = ["google.com", "youtube.com", "instagram.com"]


print(f"--- PENGECEKAN WEB ---")

# my traditional learning code
# for w in website:
#     respons = os.system(f"ping -c 1 {w} > /dev/null 2>&1")
#     if respons == 0:
#         print(f"{w} : online")
#     else:
#         print(f"{w} : offline")

#another code from gemini
with open("log_server.txt", "a") as file:
    for w in website:
        respons = os.system(f"ping -c 1 {w} > /dev/null 2>&1")
        status = "ONLINE" if respons == 0 else "OFFLINE"
        
        # Simpan ke file .txt
        file.write(f"Website: {w} | Status: {status}\n")
        
        # Tetap tampilkan di layar terminal
        print(f"Mengecek {w}... selesai.")

