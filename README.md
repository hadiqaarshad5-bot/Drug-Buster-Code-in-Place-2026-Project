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


•	12+ wildly different patients — each with their own personality, backstory, and questionable life choices.
•	Real pharmacology learning — every disease maps to an actual treatment, with mini-explanations after each round so you learn while you play.
•	ASCII animations — pulsing heartbeats, speeding ambulances, victory sparkles, and dramatic tombstones when things go terribly wrong.
•	Colorful terminal interface — powered by Colorama to transform the command line into a vibrant, engaging game world.
•	Typewriter-style dialogue — cinematic conversations that make every patient encounter feel like a scene from a medical drama.
•	Random chaos events — power outages, zombie outbreaks, surprise visits from Dr. House, and other unpredictable challenges.
•	Progression and ranking system — rise from "Medical Student (Barely)" to the legendary "House M.D. Himself."
•	Persistent high scores — save your best performances and keep challenging yourself to become the ultimate Drug Buster.
•	Medical comedy at every turn — absurd situations, hilarious patient stories, and plenty of questionable decisions.
•	Learn while having fun — a perfect mix of education, strategy, and humor for pharmacology enthusiasts.



Structure:

<img width="560" height="248" alt="Screenshot 2026-06-14 at 7 14 08 PM" src="https://github.com/user-attachments/assets/f55cfb97-eef1-4f31-b6eb-bf404150a5da" />


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
- Clone the repository: https://github.com/hadiqaarshad5-bot/Drug-Buster-Code-in-Place-2026-Project
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
a. Python 3 —> developed as part of Code in Place learning experience
b Colorama —> used for terminal styling and color effects
c. ASCII art —> custom-designed animations for immersive gameplay
d. Coffee —> heavily relied upon during development

  







