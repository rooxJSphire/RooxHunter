import os

def banner():
    os.system("clear")
    print("""
██████   ██████   ██████  ██   ██ ██    ██ ██    ██ ███    ██ ████████ ██████  
██   ██ ██       ██    ██ ██  ██  ██    ██ ██    ██ ████   ██    ██    ██    ██ 
██████  ██   ███ ██    ██ █████   ██    ██ ██    ██ ██ ██  ██    ██    ██    ██ 
██      ██    ██ ██    ██ ██  ██  ██    ██ ██    ██ ██  ██ ██    ██    ██    ██ 
██       ██████   ██████  ██   ██  ██████   ██████  ██   ████    ██    ██████  
                            RooxHunter v1.0
                🔥 For your own site power testing only 🔥
""")

def menu():
    print("""
[1] Brutal Header Flood
[2] Path Discovery (Brute Dir)
[3] Port Scanner (Nmap)
[4] HTTP Method Checker
[0] Exit
""")

def main():
    while True:
        banner()
        menu()
        choice = input("Pilih menu > ")

        if choice == '1':
            os.system("python modules/flood.py")
        elif choice == '2':
            os.system("python modules/dirbrute.py")
        elif choice == '3':
            os.system("python modules/portscan.py")
        elif choice == '4':
            os.system("python modules/methodcheck.py")
        elif choice == '0':
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
