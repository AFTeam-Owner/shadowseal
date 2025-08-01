# Termux Installation Guide

## Quick Install (Recommended)

### 1. Install with lightweight dependencies
```bash
# Update packages
pkg update && pkg upgrade

# Install Python and essential tools
pkg install python git

# Install cryptography (pre-compiled)
pip install cryptography

# Install ShadowSeal without heavy dependencies
pip install --no-deps shadowseal
```

### 2. Manual lightweight installation
```bash
# Clone repository
git clone https://github.com/AFTeam-Owner/shadowseal.git
cd shadowseal

# Install only essential dependencies
pip install cryptography

# Install ShadowSeal
python setup-termux.py install
```

## Why Installation Takes Long

### Heavy Dependencies Removed:
- **psutil** - Native compilation issues on Android
- **cython** - Compilation complexity
- **rust** - Very large toolchain
- **build-essential** - Not needed for basic functionality

### Optimized Dependencies:
- **cryptography** - Uses pre-compiled wheels
- **Pure Python** - No compilation required

## Features Available in Termux Version

✅ **Working:**
- File encryption/decryption
- Password protection
- Cross-platform encrypted files
- Basic anti-debugging (Android-optimized)

❌ **Limited:**
- Advanced process monitoring (no psutil)
- Performance optimizations (no Cython)
- Hardware binding features

## Usage Examples

```bash
# Encrypt a Python file
shadowseal encrypt script.py -o script.shc

# Run encrypted file
shadowseal run script.shc

# Decrypt back to Python
shadowseal decrypt script.shc -o original.py
```

## Troubleshooting

### If installation fails:
```bash
# Try with --no-deps
pip install --no-deps shadowseal

# Install cryptography separately
pkg install python-cryptography
```

### If execution fails:
```bash
# Check Python version
python --version  # Should be 3.7+

# Test basic functionality
python -c "from utils.anti_debug import anti_debug; print(anti_debug())"
```

## Alternative: System Python
If Termux Python has issues, try:
```bash
# Use system Python (if available)
python3 -m pip install shadowseal
```

## Performance Notes
- Termux version is ~50% smaller than full version
- Encryption/decryption speed is slightly slower
- All core security features work identically