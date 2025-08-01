# ShadowSeal - Termux/Android Optimized

## 🚀 Quick Install for Termux

```bash
# Install in 30 seconds
pkg install python git
pip install cryptography
pip install --no-deps shadowseal
```

## 📱 Features
- ✅ Fast installation (30s vs 5+ minutes)
- ✅ File encryption/decryption
- ✅ Password protection
- ✅ Cross-platform encrypted files
- ✅ Android-optimized anti-debugging

## 🛠️ Usage
```bash
# Encrypt
shadowseal encrypt script.py -o script.shc

# Run encrypted
shadowseal run script.shc

# Decrypt
shadowseal decrypt script.shc -o original.py
```

## 📦 Installation Options

### Option 1: Lightweight (Recommended)
```bash
pip install --no-deps shadowseal
```

### Option 2: Manual install
```bash
git clone https://github.com/AFTeam-Owner/shadowseal.git
cd shadowseal
pip install cryptography
python setup-termux.py install
```

## 🔧 Requirements
- Python 3.7+
- cryptography package
- Termux (Android 7+)

## ⚡ Performance
- 50% smaller installation
- No compilation required
- Works on all Android architectures