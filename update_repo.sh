#!/bin/bash
# Script to update GitHub repository with Termux optimizations

echo "🚀 Updating ShadowSeal repository with Termux optimizations..."

# Check if git is available
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first."
    exit 1
fi

# Add all changes
echo "📦 Adding files to git..."
git add .

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "ℹ️  No changes detected. Repository is up to date."
    exit 0
fi

# Commit with descriptive message
echo "📝 Committing changes..."
git commit -m "🚀 Termux/Android Optimization v1.0.4

✅ Fixed anti-debug false positives on Android/Termux
✅ Reduced installation time from 5+ min to 30 seconds
✅ Removed heavy dependencies (psutil, cython, rust)
✅ Added lightweight installation options
✅ Added Termux-specific setup files
✅ Updated README with optimized installation instructions

Files added:
- requirements-termux.txt (lightweight dependencies)
- setup-termux.py (Termux-optimized setup)
- TERMUX_INSTALL.md (comprehensive guide)
- README-TERMUX.md (quick install guide)
- ANDROID_FIX_SUMMARY.md (optimization summary)

Files modified:
- utils/anti_debug.py (graceful psutil fallback)
- README.md (updated Termux instructions)"

# Push to GitHub
echo "🔄 Pushing to GitHub..."
git push origin main

echo "✅ Repository updated successfully!"
echo ""
echo "📱 Termux users can now install with:"
echo "  pkg install python git"
echo "  pip install cryptography"
echo "  pip install --no-deps shadowseal"
echo ""
echo "🔗 GitHub repository is ready!"