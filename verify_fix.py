#!/usr/bin/env python3
import os
import sys

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Import the anti-debug module
from utils.anti_debug import anti_debug, is_android

# Test the fix
print("ShadowSeal Android Anti-Debug Fix Verification")
print("=" * 50)
print(f"Platform: {sys.platform}")
print(f"Android detected: {is_android()}")
print(f"Anti-debug triggered: {anti_debug()}")
print("=" * 50)

if is_android():
    print("✅ Android/Termux environment detected")
    print("✅ Anti-debug checks disabled for Android")
else:
    print("ℹ️  Non-Android environment - anti-debug checks active")

# Test with a simple encrypted file
try:
    from runner.loader import run_shc
    print("\nTesting encrypted file execution...")
    result = run_shc("test_simple.shc")
    if result:
        print("✅ Encrypted file executed successfully")
    else:
        print("❌ Encrypted file execution failed")
except Exception as e:
    print(f"❌ Error testing encrypted file: {e}")