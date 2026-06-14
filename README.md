                     Drug Buster: The Pharmacology Comedy Quest

  "Welcome to St. Bernard's Hospital of Questionable Decisions, where the patients are weird, 
     the diagnoses are real, and the doctor (you!) is just trying to survive the shift."


Introduction:
Drug Buster is a comedy game I built that runs in your terminal. You play a doctor who has to figure out what's wrong with some seriously chaotic 
patients and prescribe the right medication before things go south.

Think of it like a pharmacology quiz, but instead of boring textbook questions, you've got Karen demanding to speak to your manager about her hypertension, 
a gym bro who took 17 scoops of pre-workout, and a toddler who ate the "pretty blue pills" because they "tasted like candy."

The patients are ridiculous. The pharmacology is real. And somewhere between laughing and panicking, you might actually learn something.
As I wanted to make a brudge between my education and coding, I made a project that is a mixture of medicine and code, learning and laughing.


Screenshots:
<img width="1374" height="788" alt="Screenshot 2026-06-14 at 6 55 11 PM" src="https://github.com/user-attachments/assets/f1de000a-8796-43fb-9325-0169a3da3980" />

<img width="1383" height="786" alt="Screenshot 2026-06-14 at 6 55 50 PM" src="https://github.com/user-attachments/assets/47b0e989-319a-4a15-8987-8bc309b5a62f" />

<img width="1389" height="792" alt="Screenshot 2026-06-14 at 6 56 04 PM" src="https://github.com/user-attachments/assets/069ce88f-80ba-4e64-88a6-0b4f72c4d7fe" />

<img width="1387" height="789" alt="Screenshot 2026-06-14 at 6 56 18 PM" src="https://github.com/user-attachments/assets/e0145223-3b4f-40d1-a817-ee87171a9384" />

<img width="1379" height="795" alt="Screenshot 2026-06-14 at 6 56 51 PM" src="https://github.com/user-attachments/assets/f2d4c69b-ffbb-4b60-a29e-5c98a96b941f" />

<img width="1381" height="789" alt="Screenshot 2026-06-14 at 6 57 07 PM" src="https://github.com/user-attachments/assets/30ea4b83-18fa-4b8a-b0c9-0f34fe3685b7" />


Description:
a. A cast of 12+ wildly different patients — each with their own personality, backstory, and questionable life choices
b. Real pharmacology — every disease maps to an actual treatment, with mini-explanations after each round so you actually learn something
c. ASCII animations — pulsing heartbeats, ambulances racing across the screen, sparkles when you save someone, dramatic tombstones when you don't
d. A colorful terminal that doesn't look like a boring black box (thanks, colorama!)
e. Typewriter dialogue so it feels like a movie, not a quiz
f. Random chaos events — power outages, zombie outbreaks, surprise visits from Dr. House
g. scoring system with ranks — start as a "Medical Student (Barely)" and work your way up to "House M.D. Himself"
h. Persistent high scores so you can beat your own record

Structure:
drug-buster/
│
├── main.py              # The game loop. Start here.
├── ui.py                # Colors, banners, and the typewriter effect
├── animations.py        # Every animation (heartbeats, ambulances, etc.)
├── patients.py         # The 12+ patients and their dialogue
├── drugs.py            # The drug-disease database
├── chaos_events.py     # Random events that mess with the player
│
├── requirements.txt     # Just colorama. That's all you need.
├── .gitignore          # Tells Git what to ignore
└── README.md           # This file!

A quick rundown of each file:
- main.py runs the show — the menu, the game loop, lives, scoring, and game over
- ui.py handles anything visual — colors, formatted banners, loading bars, that satisfying typewriter effect
- animations.py is where the cinematic stuff lives — frame-by-frame ASCII art for every dramatic moment
- patients.py holds every patient — their name, age, dialogue, symptoms, the works
- drugs.py is the medical brain of the game — it maps each disease to the correct treatment plus three plausible-but-wrong options
- chaos_events.py keeps things unpredictable with random surprise events

How to Run it?
This project is simple to set up and run. Follow the steps below:
- Python 3 installed on your system (download it from https://www.python.org/downloads/ if needed)
- A terminal (any standard terminal will work)
- Clone the repository:
- Navigate to the project directory: cd drug-buster
- Install dependencies: This project requires only one external library: colorama.
- pip install -r requirements.txt
- Run the game


How to Play
After starting the game, the flow is as follows:

A main menu is displayed — select Start New Game
A patient arrives at the hospital
Read the patient’s story and review their symptoms
Choose the correct treatment from four options
Correct answers earn points and increase your streak
Incorrect answers result in losing a life and the patient’s condition worsening
After three incorrect answers, the game ends
Periodic chaos events occur to increase difficulty and unpredictability
Higher streaks result in higher scores. Players can replay to improve their high score and rank.

Built With
Python 3 — developed as part of Code in Place learning experience
Colorama — used for terminal styling and color effects
ASCII art — custom-designed animations for immersive gameplay
Coffee — heavily relied upon during development

  







