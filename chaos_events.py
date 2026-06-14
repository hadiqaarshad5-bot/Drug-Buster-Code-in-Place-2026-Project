"""
chaos_events.py - Random hilarious chaos
"""

import random
from ui import *
from animations import chaos_flash

CHAOS_EVENTS = [
    {
        "name": "POWER OUTAGE!",
        "description": "The hospital lost power! Diagnose by intuition only!",
        "effect": "hide_symptoms"
    },
    {
        "name": "ZOMBIE OUTBREAK!",
        "description": "Patient Zero just bit the janitor! +2x points if you save the next patient!",
        "effect": "double_points"
    },
    {
        "name": "INSURANCE AUDIT!",
        "description": "You must explain your prescription. No pressure!",
        "effect": "explanation_required"
    },
    {
        "name": "CELEBRITY PATIENT!",
        "description": "A famous celebrity arrives. Mess up = front-page tabloid!",
        "effect": "double_penalty"
    },
    {
        "name": "DR. HOUSE VISITS!",
        "description": "Dr. House is judging you. He says: 'It's never lupus.'",
        "effect": "encouragement"
    },
]


def trigger_chaos():
    event = random.choice(CHAOS_EVENTS)

    chaos_flash(event["name"])
    typewriter(f"  📢 {event['description']}", YELLOW, 0.03)
    pause(2)

    return event