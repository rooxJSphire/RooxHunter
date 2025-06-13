import requests

url = input("Masukkan URL > ")
methods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD', 'PATCH']

print("🔎 Mengecek HTTP Methods...")
for m in methods:
    try:
        r = requests.request(m, url)
        print(f"{m}: {r.status_code}")
    except:
        print(f"{m}: Gagal")
