import requests

url = input("Target URL (https://...) > ")
wordlist = ["admin", "login", "dashboard", "config", "upload"]

print("🔍 Memulai brute path...")
for path in wordlist:
    full = f"{url}/{path}"
    r = requests.get(full)
    if r.status_code != 404:
        print(f"✅ Ditemukan: {full} [{r.status_code}]")
    else:
        print(f"❌ {full}")
