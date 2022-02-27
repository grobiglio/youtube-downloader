import os
import sys

def clean_console() -> None:
    """Cleans de console regardless the operating system is Windows or Linux."""
    if sys.platform.startswith('win32'):
        os.system("cls")
    elif sys.platform.startswith('linux'):
        os.system("clear")