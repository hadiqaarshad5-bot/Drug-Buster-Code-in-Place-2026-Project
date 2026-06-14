

"""
main.py - Drug Buster Main Game
Run this file to play!
"""

import random
import os
from ui import *
from animations import *
from patients import get_random_patient
from drugs import get_drug_options
from chaos_events import trigger_chaos

HIGHSCORE_FILE = "highscores.txt"


def load_highscore():
    if not os.path.exists(HIGHSCORE_FILE):
        return 0
    with open(HIGHSCORE_FILE, "r") as f:
        try:
            return int(f.read().strip())
        except:
            return 0


def save_highscore(score):
    with open(HIGHSCORE_FILE, "w") as f:
        f.write(str(score))


def get_title(score):
    if score < 200:
        return "🥴 Medical Student (Barely)"
    elif score < 500:
        return "😅 Intern Who Googles A Lot"
    elif score < 1000:
        return "😎 Actual Doctor"
    elif score < 2000:
        return "🏆 Chief of Medicine"
    else:
        return "👑 House M.D. Himself"


def show_main_menu():
    clear_screen()
    banner("💊 DRUG BUSTER: PHARMACOLOGY QUEST 💊", MAGENTA)
    print()
    print(CYAN + "  [1] 🎮 Start New Game")
    print(CYAN + "  [2] 🏆 View High Score")
    print(CYAN + "  [3] ❓ How to Play")
    print(CYAN + "  [4] 🚪 Quit")
    print()
    return input(YELLOW + "  > Your choice: " + RESET).strip()


def show_instructions():
    clear_screen()
    banner("📖 HOW TO PLAY", CYAN)

    rules = [
        "👨‍⚕️  You are Dr. You at St. Bernard's Hospital.",
        "🚑  Patients arrive with hilarious problems.",
        "💊  Choose the correct drug from 4 options.",
        "✅  Correct = +100 points (+50 streak bonus).",
        "❌  Wrong = lose a life. 3 strikes = GAME OVER.",
        "🎰  Random CHAOS EVENTS make things crazy!",
        "👑  Beat the high score to become House M.D.!",
    ]

    for line in rules:
        typewriter("  " + line, WHITE, 0.02)

    press_enter()


def show_high_score():
    clear_screen()
    banner("🏆 HIGH SCORE", YELLOW)

    score = load_highscore()

    print()
    typewriter(f"  Best Score: {score} points", GREEN, 0.04)
    typewriter(f"  Title: {get_title(score)}", CYAN, 0.04)

    press_enter()


def play_round(patient, score, streak, chaos_event=None):
    """Play one patient encounter."""
    clear_screen()

    ambulance_arrives()
    patient_walks_in(patient["emoji"])

    banner(f"👤 {patient['name']}, age {patient['age']}", BLUE)

    print()
    typewriter(f"  {patient['emoji']}", YELLOW, 0.05)

    print()
    typewriter(f'  💬 "{patient["story"]}"', BLUE, 0.025)

    pause(0.8)

    # Symptoms
    print()
    print(YELLOW + "  📋 SYMPTOMS:")

    if chaos_event and chaos_event["effect"] == "hide_symptoms":
        print(RED + "  ⚠️  Symptoms hidden due to power outage!")
    else:
        for s in patient["symptoms"]:
            typewriter(f"     • {s}", WHITE, 0.02)

    pause(0.5)

    # Quote
    print()
    quote = random.choice(patient["extra_quotes"])
    typewriter(f'  💭 "{quote}"', MAGENTA, 0.025)

    pause(0.5)

    # Drug options
    options, correct_index, explanation = get_drug_options(patient["disease"])

    print()
    print(CYAN + "  💊 What do you prescribe, Doctor?")
    print()

    for i, opt in enumerate(options, 1):
        print(CYAN + f"     [{i}] {opt}")

    print()

    while True:
        choice = input(YELLOW + "  > Your choice (1-4): " + RESET).strip()
        if choice in ["1", "2", "3", "4"]:
            choice = int(choice)
            break
        print(RED + "  Please enter 1, 2, 3, or 4!")

    print()

    loading_bar("  💉 Administering drug...", 1.5, MAGENTA)

    if choice == correct_index:
        correct_answer_animation()

        points = 100 + (streak * 50)

        if chaos_event and chaos_event["effect"] == "double_points":
            points *= 2
            print(YELLOW + f"  🎰 DOUBLE POINTS from chaos event! +{points}")

        print(GREEN + f"  +{points} points! (Streak: {streak + 1})")

        typewriter(f"  📚 {explanation}", CYAN, 0.02)
        press_enter()

        return points, True

    else:
        wrong_answer_animation()

        print(RED + f"  ❌ Correct answer was: {options[correct_index - 1]}")
        typewriter(f"  📚 {explanation}", CYAN, 0.02)

        patient_dies_animation()
        press_enter()

        return 0, False


def play_game():
    score = 0
    lives = 3
    streak = 0
    round_num = 0

    clear_screen()
    typewriter("  🏥 Welcome to St. Bernard's Hospital, Dr. You!", GREEN, 0.03)
    typewriter("  🩺 Your shift starts NOW. Good luck!", CYAN, 0.03)
    pause(1)

    while lives > 0:
        round_num += 1

        chaos_event = None
        if round_num % 4 == 0:
            chaos_event = trigger_chaos()

        clear_screen()
        print(MAGENTA + "═" * 60)
        print(
            f"  ❤️  Lives: {'❤️ ' * lives}{'🖤 ' * (3 - lives)} | "
            f"💰 Score: {score} | 🔥 Streak: {streak} | 🩺 Round: {round_num}"
        )
        print(MAGENTA + "═" * 60)

        pause(1)

        patient = get_random_patient()
        points, success = play_round(patient, score, streak, chaos_event)

        if success:
            score += points
            streak += 1
        else:
            lives -= 1
            streak = 0

            if lives > 0:
                print(RED + f"\n  ⚠️  {lives} lives remaining!")
                pause(1.5)

    game_over_animation()

    clear_screen()
    banner("📊 FINAL RESULTS", YELLOW)

    print()
    typewriter(f"  💰 Final Score: {score}", GREEN, 0.04)
    typewriter(f"  🩺 Patients Treated: {round_num}", CYAN, 0.04)
    typewriter(f"  👑 Your Title: {get_title(score)}", MAGENTA, 0.04)

    high = load_highscore()

    if score > high:
        print()
        flash("🎉 NEW HIGH SCORE! 🎉", YELLOW, times=4)
        save_highscore(score)
    else:
        print()
        typewriter(f"  🏆 High Score to beat: {high}", YELLOW, 0.03)

    press_enter()


def main():
    intro_animation()

    while True:
        choice = show_main_menu()

        if choice == "1":
            play_game()
        elif choice == "2":
            show_high_score()
        elif choice == "3":
            show_instructions()
        elif choice == "4":
            clear_screen()
            typewriter("  👋 Thanks for playing Drug Buster!", GREEN, 0.04)
            typewriter("  💊 Stay healthy, doctor! 💊", CYAN, 0.04)
            print()
            break
        else:
            print(RED + "  Invalid choice!")
            pause(1)


if __name__ == "__main__":
    main()