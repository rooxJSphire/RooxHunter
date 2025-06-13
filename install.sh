---

### 🛠️ `install.sh`
```bash
#!/bin/bash
echo "🔧 Menginstall dependency..."
pkg update && pkg upgrade -y
pkg install python git nmap -y
pip install requests
chmod +x roox.py
chmod +x modules/*.py
echo "✅ Selesai. Jalankan dengan: python roox.py"
