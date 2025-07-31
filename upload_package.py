#!/usr/bin/env python3
"""
Automated upload script for ShadowSeal package
Handles both GitHub and PyPI uploads
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(cmd, check=True):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=check)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {cmd}")
        print(f"Error: {e.stderr}")
        return None

def check_git():
    """Check if git is available and configured"""
    git_version = run_command("git --version", check=False)
    if not git_version:
        print("❌ Git is not installed or not in PATH")
        return False
    
    # Check if git is configured
    user_name = run_command("git config --global user.name", check=False)
    user_email = run_command("git config --global user.email", check=False)
    
    if not user_name or not user_email:
        print("⚠️  Git is not configured. Please run:")
        print("   git config --global user.name 'Your Name'")
        print("   git config --global user.email 'your.email@example.com'")
        return False
    
    return True

def init_git_repo():
    """Initialize git repository if not already done"""
    if os.path.exists(".git"):
        print("✅ Git repository already initialized")
        return True
    
    if not check_git():
        return False
    
    # Initialize git
    run_command("git init")
    run_command("git add .")
    run_command("git commit -m 'Initial commit: Cross-platform ShadowSeal with Android support'")
    print("✅ Git repository initialized")
    return True

def build_package():
    """Build the Python package"""
    print("🔨 Building package...")
    
    # Clean previous builds
    for folder in ['build', 'dist', '*.egg-info']:
        path = Path(folder)
        if path.exists():
            shutil.rmtree(path)
    
    # Install build tools
    run_command("pip install build twine setuptools-rust")
    
    # Build the package
    result = run_command("python -m build")
    if result is None:
        print("❌ Build failed")
        return False
    
    print("✅ Package built successfully")
    return True

def upload_to_pypi(test=True):
    """Upload package to PyPI"""
    print("📦 Uploading to PyPI...")
    
    # Check if package was built
    dist_path = Path("dist")
    if not dist_path.exists() or not list(dist_path.glob("*.whl")):
        print("❌ No distribution files found. Run build first.")
        return False
    
    # Upload to PyPI
    if test:
        cmd = "python -m twine upload --repository testpypi dist/*"
        print("🧪 Uploading to Test PyPI...")
    else:
        cmd = "python -m twine upload dist/*"
        print("🚀 Uploading to Production PyPI...")
    
    result = run_command(cmd, check=False)
    if result is None:
        print("❌ Upload failed")
        return False
    
    print("✅ Upload completed successfully")
    return True

def create_pypirc():
    """Create .pypirc file for authentication"""
    pypirc_path = Path.home() / ".pypirc"
    
    if pypirc_path.exists():
        print("✅ .pypirc already exists")
        return
    
    print("⚠️  Creating .pypirc file...")
    
    content = """[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = YOUR_PYPI_TOKEN_HERE

[testpypi]
username = __token__
password = YOUR_TEST_PYPI_TOKEN_HERE
"""
    
    with open(pypirc_path, "w") as f:
        f.write(content)
    
    print("✅ .pypirc created. Please edit ~/.pypirc to add your tokens")

def main():
    """Main upload process"""
    print("🚀 ShadowSeal Package Upload Tool")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("setup.py").exists():
        print("❌ setup.py not found. Please run from project root")
        return 1
    
    # Initialize Git
    if not init_git_repo():
        return 1
    
    # Build package
    if not build_package():
        return 1
    
    # Create PyPI config
    create_pypirc()
    
    print("\n📋 Upload Options:")
    print("1. Upload to Test PyPI (recommended first)")
    print("2. Upload to Production PyPI")
    print("3. Skip PyPI upload")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        upload_to_pypi(test=True)
    elif choice == "2":
        upload_to_pypi(test=False)
    elif choice == "3":
        print("⏭️  Skipping PyPI upload")
    
    print("\n📋 Next Steps:")
    print("1. Edit ~/.pypirc to add your PyPI tokens")
    print("2. Run: python upload_package.py again")
    print("3. For GitHub: git remote add origin YOUR_REPO_URL")
    print("4. Push: git push -u origin main")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())