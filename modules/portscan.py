import os
target = input("Masukkan IP atau domain > ")
os.system(f"nmap -F {target}")
