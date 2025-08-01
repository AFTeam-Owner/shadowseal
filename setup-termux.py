#!/usr/bin/env python3
"""
Lightweight setup script for Termux/Android installation
Skips heavy dependencies like psutil, cython, and rust
"""

import os
import sys
from setuptools import setup, find_packages

def is_android():
    """Check if running on Android/Termux environment"""
    try:
        if os.path.exists("/system/build.prop") or os.path.exists("/system/bin/getprop"):
            return True
        if "TERMUX" in os.environ.get("PREFIX", ""):
            return True
        return False
    except:
        return False

# Lightweight requirements for Termux
install_requires = [
    'cryptography>=41.0.0',  # Core encryption
    # Skip: psutil, cython, rust - too heavy for Termux
]

setup(
    name="shadowseal",
    version="1.0.4-termux",
    description="Secure Python encryption tool - Termux optimized",
    long_description="Lightweight version optimized for Termux/Android installation",
    author="Monarch of Shadows",
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        "console_scripts": ["shadowseal=shadowseal.cli:main"],
    },
    python_requires='>=3.7',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Security :: Cryptography",
    ],
    keywords='encryption, security, python, termux, android',
)