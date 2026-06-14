"""
ui.py - The colorful heart of Drug Buster
"""

try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)  # Auto-reset colors after each print
except ImportError:
    class _NoColor:
        def __getattr__(self, name):
            return ""

    Fore = Back = Style = _NoColor()
    def init(autoreset=True):
        pass

import time
import sys
import os

# ===== COLOR SHORTCUTS =====
RED = Fore.RED + Style.BRIGHT
GREEN = Fore.GREEN + Style.BRIGHT
YELLOW = Fore.YELLOW + Style.BRIGHT
BLUE = Fore.BLUE + Style.BRIGHT
MAGENTA = Fore.MAGENTA + Style.BRIGHT
CYAN = Fore.CYAN + Style.BRIGHT
WHITE = Fore.WHITE + Style.BRIGHT
RESET = Style.RESET_ALL


def clear_screen():
    """Clear the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def typewriter(text, color=WHITE, delay=0.03):
    """Print text one character at a time (movie-style)."""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)


def fast_type(text, color=WHITE):
    """Faster typewriter for long text."""
    typewriter(text, color, delay=0.015)


def flash(text, color=RED, times=3):
    """Flash text on and off (for emergencies!)."""
    for _ in range(times):
        clear_screen()
        print("\n" * 10)
        print(color + text.center(60))
        time.sleep(0.2)
        clear_screen()
        time.sleep(0.15)
    clear_screen()


def shake_text(text, color=YELLOW, times=5):
    """Make text shake left and right (screen shake effect)."""
    for i in range(times):
        offset = " " * (i % 3)
        sys.stdout.write("\r" + color + offset + text + " " * 5)
        sys.stdout.flush()
        time.sleep(0.08)
    print(RESET)


def loading_bar(label, duration=2.0, color=CYAN):
    """Animated loading bar."""
    print(color + label)
    bar_length = 30

    for i in range(bar_length + 1):
        percent = int((i / bar_length) * 100)
        bar = "█" * i + "░" * (bar_length - i)

        sys.stdout.write(f"\r{color}[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(duration / bar_length)

    print(RESET + "\n")


def banner(text, color=MAGENTA, width=60):
    """Print a fancy banner."""
    line = "═" * width

    print(color + "╔" + line + "╗")
    print(color + "║" + text.center(width) + "║")
    print(color + "╚" + line + "╝" + RESET)


def pause(seconds=1.0):
    time.sleep(seconds)


def press_enter():
    input(CYAN + "\n   ▶ Press ENTER to continue..." + RESET)