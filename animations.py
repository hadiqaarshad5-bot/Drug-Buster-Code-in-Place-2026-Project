"""
animations.py - Frame-by-frame animations
"""

import time
import sys
from ui import *


def animate_frames(frames, color=WHITE, frame_delay=0.3, loops=1):
    """Play frames like a flipbook."""
    for _ in range(loops):
        for frame in frames:
            clear_screen()
            print(color + frame)
            time.sleep(frame_delay)


# ===== INTRO ANIMATION =====

def intro_animation():
    """Big dramatic intro."""
    clear_screen()
    pause(0.3)

    # Heartbeat animation
    heartbeats = [
        """
        
        
                  .--.
                 /    \\
                |      |
                 \\    /
                  '--'
        """,
        """
        
        
                .------.
               /        \\
              |          |
               \\        /
                '------'
        """,
        """
        
        
              .----------.
             /            \\
            |              |
             \\            /
              '----------'
        """,
    ]

    for _ in range(2):
        for frame in heartbeats:
            clear_screen()
            print(RED + frame)
            time.sleep(0.15)

        for frame in reversed(heartbeats):
            clear_screen()
            print(RED + frame)
            time.sleep(0.15)

    clear_screen()
    pause(0.3)

    # Title reveal
    title = """
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║   ██████╗ ██████╗ ██╗   ██╗ ██████╗                 ║
    ║   ██╔══██╗██╔══██╗██║   ██║██╔════╝                 ║
    ║   ██║  ██║██████╔╝██║   ██║██║  ███╗                ║
    ║   ██║  ██║██╔══██╗██║   ██║██║   ██║                ║
    ║   ██████╔╝██║  ██║╚██████╔╝╚██████╔╝                ║
    ║   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝                 ║
    ║                                                      ║
    ║   ██████╗ ██╗   ██╗███████╗████████╗███████╗██████╗ ║
    ║   ██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗║
    ║   ██████╔╝██║   ██║███████╗   ██║   █████╗  ██████╔╝║
    ║   ██╔══██╗██║   ██║╚════██║   ██║   ██╔══╝  ██╔══██╗║
    ║   ██████╔╝╚██████╔╝███████║   ██║   ███████╗██║  ██║║
    ║   ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
    """

    print(MAGENTA + title)
    pause(0.5)
    typewriter("        💊 The Pharmacology Comedy Quest 💊", YELLOW, 0.04)
    pause(0.5)
    typewriter("              ~ Press ENTER to begin ~", CYAN, 0.04)
    input()


# ===== AMBULANCE ANIMATION =====

def ambulance_arrives():
    """Ambulance drives across the screen!"""
    width = 60

    for offset in range(0, width, 3):
        clear_screen()
        print(RED + "\n" * 3)
        print(YELLOW + "🚨 *WEE-OOO* *WEE-OOO* 🚨".center(width))
        print()
        print(" " * offset + RED + "🚑💨")
        print(WHITE + "_" * width)
        time.sleep(0.05)

    clear_screen()


# ===== PATIENT ARRIVAL =====

def patient_walks_in(patient_emoji="(•_•)"):
    """Patient walks in from the right side."""
    width = 50

    for offset in range(width, -1, -4):
        clear_screen()
        print(CYAN + "\n  🏥 EMERGENCY ROOM 🏥\n")
        print(WHITE + "  " + "_" * width)
        print("  |" + " " * (width - 2) + "|")
        print(
            "  |"
            + " " * offset
            + YELLOW
            + patient_emoji
            + WHITE
            + " " * (width - offset - len(patient_emoji) - 2)
            + "|"
        )
        print("  |" + " " * (width - 2) + "|")
        print(WHITE + "  " + "‾" * width)
        time.sleep(0.08)

    pause(0.4)


# ===== CORRECT ANSWER ANIMATION =====

def correct_answer_animation():
    """Celebration with sparkles!"""

    frames = [
        """
        ✨        ✨
            \\O/
             |
            / \\
        ✨   CURED!   ✨
        """,
        """
         ✨    ✨    ✨
              O/
             /|
             / \\
          ✨ CURED! ✨
        """,
        """
        ✨ ✨ ✨ ✨ ✨
            \\O
             |\\
             / \\
         ✨✨ CURED! ✨✨
        """,
        """
       🎉 ✨ 🎉 ✨ 🎉
            \\O/
             |
            / \\
        🎉 CURED! 🎉
        """,
    ]

    animate_frames(frames, GREEN, 0.2, loops=3)

    clear_screen()
    print(GREEN + "\n" + "🎉" * 30)
    typewriter("    ✅ CORRECT DIAGNOSIS! Patient saved! ✅", GREEN, 0.03)
    print(GREEN + "🎉" * 30 + "\n")


# ===== WRONG ANSWER ANIMATION =====

def wrong_answer_animation():
    """Patient suffers comically."""

    frames = [
        """
            (x_x)
             |
            / \\
         "Ohhh nooo..."
        """,
        """
            (X_X)
            /|\\
            / \\
         "Why doctor?!"
        """,
        """
            (@_@)
             |/
            / \\
        "I see colors..."
        """,
        """
           ~(*_*)~
            \\|/
            / \\
        "Is that a unicorn?!"
        """,
    ]

    animate_frames(frames, RED, 0.25, loops=2)

    clear_screen()
    flash("❌ WRONG DRUG! ❌", RED, times=3)


# ===== PATIENT DIES =====

def patient_dies_animation():
    frames = [
        """
            (x_x)
             |
            / \\
        """,
        """
            (X_X)
            _|_
        """,
        """
            R.I.P
            ⚰️
        """,
        """
            ⚰️
          ~~~~~~~~
         "Here lies
          a patient"
        """,
    ]

    animate_frames(frames, RED, 0.5, loops=1)
    pause(1)


# ===== HEARTBEAT MONITOR =====

def heartbeat_monitor(beats=5, healthy=True):
    """Animated EKG line."""

    if healthy:
        line = "____/\\____/\\____/\\____/\\____"
        color = GREEN
        sound = "beep... beep... beep..."
    else:
        line = "____/\\__/\\/\\_/\\__/\\___"
        color = RED
        sound = "BEEP BEEP BEEP!!!"

    for i in range(beats):
        clear_screen()
        print(color + "\n  💓 PATIENT VITALS 💓\n")
        visible = line[: i * 5 + 5]
        print(color + "  " + visible)
        print(color + f"\n  {sound}")
        time.sleep(0.3)

    pause(0.5)


# ===== PILL DISPENSING =====

def pill_animation(drug_name):
    """Pills drop down the screen."""

    clear_screen()
    print(CYAN + f"\n  💊 Dispensing {drug_name}... 💊\n")

    for row in range(8):
        line = ""

        for col in range(10):
            if (row + col) % 3 == 0:
                line += random_pill()
            else:
                line += "  "

        print(YELLOW + line)
        time.sleep(0.1)

    pause(0.5)


def random_pill():
    import random
    return random.choice(["💊", "💉", "🧪"])


# ===== CHAOS EVENT FLASH =====

def chaos_flash(event_name):
    """Big dramatic chaos event reveal."""

    clear_screen()

    for _ in range(4):
        print(RED + Back.YELLOW + "\n" + "⚠️ " * 20)
        print(
            RED
            + Back.YELLOW
            + f"  CHAOS EVENT: {event_name}  ".center(60)
        )
        print(RED + Back.YELLOW + "⚠️ " * 20 + RESET)

        time.sleep(0.2)
        clear_screen()
        time.sleep(0.15)

    print(RED + f"\n  💥 {event_name} 💥\n")
    pause(1)


# ===== GAME OVER =====

def game_over_animation():
    clear_screen()
    pause(0.5)

    text = """
    ╔════════════════════════════════════╗
    ║                                    ║
    ║     ☠️   GAME  OVER   ☠️          ║
    ║                                    ║
    ║   The hospital has been closed.   ║
    ║   It is now a Chipotle. 🌯        ║
    ║                                    ║
    ╚════════════════════════════════════╝
    """

    for line in text.split("\n"):
        print(RED + line)
        time.sleep(0.1)

    pause(2)
    