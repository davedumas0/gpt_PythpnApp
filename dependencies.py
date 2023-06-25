import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_dependencies():
    dependencies = ["openai", "requests", "tkinter", "pygments", "python-dotenv"]
    for dependency in dependencies:
        try:
            __import__(dependency)
        except ImportError:
            install(dependency)

check_and_install_dependencies()
