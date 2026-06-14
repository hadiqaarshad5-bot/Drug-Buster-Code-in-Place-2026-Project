"""
drugs.py - Drug database with real pharmacology + comedy
"""

import random

# Disease → correct drug + 3 wrong (but plausible) options
DRUG_DATABASE = {
    "hypertension": {
        "correct": "Lisinopril (ACE inhibitor)",
        "wrong": ["Insulin", "Albuterol inhaler", "Morphine"],
        "explanation": "Lisinopril lowers blood pressure by blocking the angiotensin-converting enzyme."
    },
    "caffeine_overdose": {
        "correct": "Beta-blocker (Propranolol) + IV fluids",
        "wrong": ["MORE caffeine", "Antibiotics", "Statins"],
        "explanation": "Beta-blockers calm the racing heart caused by caffeine's adrenaline rush."
    },
    "drug_alcohol_interaction": {
        "correct": "IV fluids + observation",
        "wrong": ["More whiskey (hair of the dog)", "Antidepressants", "Anticoagulants"],
        "explanation": "Alcohol potentiates many BP meds. Hydration and monitoring are key!"
    },
    "poisoning": {
        "correct": "Activated Charcoal",
        "wrong": ["More borax (homeopathy!)", "Aspirin", "Ibuprofen"],
        "explanation": "Activated charcoal absorbs toxins in the GI tract before they reach the bloodstream."
    },
    "strep_throat": {
        "correct": "Penicillin (antibiotic)",
        "wrong": ["Garlic capsules", "Holy water", "Antiviral acyclovir"],
        "explanation": "Strep is bacterial, so penicillin works. Vampires are NOT real, Vlad."
    },
    "oral_cancer": {
        "correct": "Refer to Oncology + Chemotherapy",
        "wrong": ["More chewing tobacco", "Aspirin", "Cough syrup"],
        "explanation": "Oral cancers need surgical/oncology evaluation. Step away from the chaw, Carl."
    },
    "flu": {
        "correct": "Oseltamivir (Tamiflu) + rest",
        "wrong": ["Antibiotics", "Cat therapy", "Steroids"],
        "explanation": "Flu is viral. Antivirals like Tamiflu help if started early."
    },
    "accidental_poisoning": {
        "correct": "Naloxone (if opioid) + Activated Charcoal",
        "wrong": ["Make him eat MORE", "Aspirin", "Tylenol"],
        "explanation": "Naloxone reverses opioid overdose. Always identify the substance first!"
    },
    "common_cold": {
        "correct": "Rest, fluids, and reassurance",
        "wrong": ["Antibiotics", "Chemotherapy", "Open-heart surgery"],
        "explanation": "It's a virus, Wendy. You don't have plague. You have a cold."
    },
    "panic_attack": {
        "correct": "Benzodiazepine (Lorazepam) + reassurance",
        "wrong": ["More edibles", "Adrenaline shot", "Caffeine"],
        "explanation": "Benzos calm the nervous system. The pizza is fine, Steve. The pizza is fine."
    },
    "measles": {
        "correct": "Supportive care + Vitamin A",
        "wrong": ["Essential oils", "5G blocker (not real)", "Antibiotics"],
        "explanation": "Vaccines prevent this. Vitamin A reduces complications. Lavender does NOT cure measles."
    },
    "allergic_reaction": {
        "correct": "Epinephrine (EpiPen) + Antihistamine",
        "wrong": ["More Botox", "Aspirin", "Antibiotics"],
        "explanation": "Epinephrine reverses anaphylaxis. Igor, please stop injecting random things."
    },
}


def get_drug_options(disease):
    """Returns shuffled list of 4 options + index of correct answer."""

    data = DRUG_DATABASE[disease]

    options = [data["correct"]] + data["wrong"]
    random.shuffle(options)

    correct_index = options.index(data["correct"]) + 1

    return options, correct_index, data["explanation"]