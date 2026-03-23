
import json
from datetime import date

FILE = "progress.json"

def load_progress():
    with open(FILE) as f:
        return json.load(f)

def save_progress(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_xp(progress, amount):

    progress["xp"] += amount

    if progress["xp"] > progress["level"] * 200:
        progress["level"] += 1

    save_progress(progress)

def update_streak(progress):

    today = str(date.today())

    if progress["last_study_date"] != today:
        progress["streak_days"] += 1
        progress["last_study_date"] = today

    save_progress(progress)
