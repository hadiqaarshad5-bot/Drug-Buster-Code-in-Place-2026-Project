"""
patients.py - Hilarious patient roster
"""

import random

PATIENTS = [
    {
        "name": "Karen the Karen",
        "emoji": "(╬ ಠ益ಠ)",
        "age": 47,
        "story": "I googled my symptoms and WebMD said I'm dying. I demand to see your manager! Also your manager's manager!",
        "symptoms": [
            "headache",
            "high blood pressure",
            "rage",
            "needs to speak to manager"
        ],
        "disease": "hypertension",
        "extra_quotes": [
            "Do you even have a degree?!",
            "I'll be leaving a 1-star Yelp review!",
            "My chiropractor said I have ALL the diseases!"
        ]
    },
    {
        "name": "Bob the Gym Bro",
        "emoji": "(💪◣_◢)💪",
        "age": 24,
        "story": "Bro, I took 17 scoops of pre-workout AND a Red Bull. My heart is doing CrossFit without me, bro. Is that... bad, bro?",
        "symptoms": [
            "palpitations",
            "tremors",
            "extreme swagger",
            "cannot stop flexing"
        ],
        "disease": "caffeine_overdose",
        "extra_quotes": [
            "Do you even lift, doc?",
            "I can bench-press this hospital bed.",
            "My protein shake is calling me."
        ]
    },
    {
        "name": "Grandma Gertrude",
        "emoji": "(つ ͡° ͜ʖ ͡°)つ",
        "age": 84,
        "story": "Sonny, I took my blood pressure pill with a lil' whiskey. For science, dear. Now the wallpaper is talking to me.",
        "symptoms": [
            "dizziness",
            "low blood pressure",
            "wallpaper hallucinations",
            "smells like gin"
        ],
        "disease": "drug_alcohol_interaction",
        "extra_quotes": [
            "Back in my day, we didn't HAVE doctors!",
            "Are you single, dearie?",
            "I once outdrank a sailor."
        ]
    },
    {
        "name": "TikTok Tina",
        "emoji": "(ノ◕ヮ◕)ノ*:・ﾟ✧",
        "age": 19,
        "story": "Bestie, I drank borax because some girl on my FYP said it cures bloating. My tummy feels like a washing machine 😭 Also I'm livestreaming this.",
        "symptoms": [
            "nausea",
            "abdominal pain",
            "regret",
            "still recording"
        ],
        "disease": "poisoning",
        "extra_quotes": [
            "Doctor, can you say 'slay' on camera?",
            "This is gonna go viral...",
            "Do you accept Venmo for the bill?"
        ]
    },
    {
        "name": "Vlad the Hypochondriac",
        "emoji": "(✖╭╮✖)",
        "age": 35,
        "story": "Doctor, I'm allergic to garlic AND sunlight. I think I'm turning into a vampire. Also I have a sore throat.",
        "symptoms": [
            "sore throat",
            "fever",
            "vampire delusions",
            "fear of mirrors"
        ],
        "disease": "strep_throat",
        "extra_quotes": [
            "Should I stock up on blood?",
            "My coffin is on backorder.",
            "Is this covered by my insurance?"
        ]
    },
    {
        "name": "Cowboy Carl",
        "emoji": "(¬‿¬ )🤠",
        "age": 58,
        "story": "Doc, I been chewin' tobacco since I was 4 years old. My tongue's gone blue and I can't feel my lips. Reckon that's normal?",
        "symptoms": [
            "mouth lesions",
            "blue tongue",
            "numbness",
            "chronic yeehaw"
        ],
        "disease": "oral_cancer",
        "extra_quotes": [
            "I rode here on my horse, Steve.",
            "This here hospital ain't got no saloon?",
            "Yeehaw... ow."
        ]
    },
    {
        "name": "Cat Lady Carol",
        "emoji": "(=^･ω･^=)",
        "age": 62,
        "story": "Mr. Whiskers diagnosed me with lupus. Mittens disagrees and says it's the flu. I trust Mittens more, but here I am.",
        "symptoms": [
            "fever",
            "cough",
            "covered in cat hair",
            "meows occasionally"
        ],
        "disease": "flu",
        "extra_quotes": [
            "Do you accept cats as payment?",
            "Mr. Whiskers is judging your stethoscope.",
            "I have 47 cats. They're all named Steve."
        ]
    },
    {
        "name": "Toddler Timmy",
        "emoji": "(°ロ°)☝",
        "age": 4,
        "story": "I ated da pwetty bwue piwws! Dey tasted wike candy! Mommy is cwying. Why is mommy cwying?",
        "symptoms": [
            "drowsiness",
            "low heart rate",
            "blue lips",
            "still adorable"
        ],
        "disease": "accidental_poisoning",
        "extra_quotes": [
            "Can I have a wowwipop?",
            "You wook funny.",
            "I want my mommy!"
        ]
    },
    {
        "name": "Dr. WebMD Wendy",
        "emoji": "(￣ヘ￣)",
        "age": 33,
        "story": "I've already diagnosed myself with 14 diseases including bubonic plague, scurvy, and 'rare tropical foot fungus.' Confirm please.",
        "symptoms": [
            "mild cold",
            "extreme paranoia",
            "8-page symptom list",
            "knows latin medical terms"
        ],
        "disease": "common_cold",
        "extra_quotes": [
            "I read the entire Mayo Clinic website.",
            "Could it be ALS? Be honest.",
            "I require a full body MRI."
        ]
    },
    {
        "name": "Stoner Steve",
        "emoji": "(⌐■_■)~ 💨",
        "age": 22,
        "story": "Whoa duuude, I ate like... a WHOLE pizza... and my heart is going BRRRR. Also why is the ceiling melting? Is that a thing?",
        "symptoms": [
            "anxiety",
            "rapid heartbeat",
            "munchies",
            "philosophical thoughts"
        ],
        "disease": "panic_attack",
        "extra_quotes": [
            "Is time real, doc?",
            "Do plants have feelings?",
            "Can I get fries with my prescription?"
        ]
    },
    {
        "name": "Anti-Vax Brenda",
        "emoji": "(╯°□°)╯",
        "age": 41,
        "story": "I haven't vaccinated my essential oils in YEARS. Now I'm covered in red spots. Must be 5G. Can you confirm it's 5G?",
        "symptoms": [
            "rash",
            "fever",
            "essential oil residue",
            "Facebook addiction"
        ],
        "disease": "measles",
        "extra_quotes": [
            "My homeopath said lavender cures everything.",
            "Is this hospital 5G-free?",
            "I trust my Facebook group more than you."
        ]
    },
    {
        "name": "Influencer Igor",
        "emoji": "( ͡° ͜ʖ ͡°)📸",
        "age": 27,
        "story": "I injected myself with collagen, Botox, AND turmeric for the 'glow up.' Now my face is paralyzed and I can't smize for the camera!",
        "symptoms": [
            "facial paralysis",
            "swelling",
            "duck lips",
            "vanity"
        ],
        "disease": "allergic_reaction",
        "extra_quotes": [
            "Can you make me glow, doctor?",
            "My sponsor will hear about this.",
            "Selfie before the IV?"
        ]
    },
]

def get_random_patient():
    return random.choice(PATIENTS)