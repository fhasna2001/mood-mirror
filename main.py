import json
import os
from datetime import date

DATA_FILE = "mood_data.json"

MOOD_INFO = {
    "happy":   {"face": ":-D",  "score": 5},
    "excited": {"face": ":-O",  "score": 5},
    "calm":    {"face": ":-)",  "score": 3},
    "tired":   {"face": "-_-",  "score": 1},
    "sad":     {"face": ":-(",  "score": -3},
    "angry":   {"face": ">:-(", "score": -4},
}
DEFAULT = {"face": ":-|", "score": 0}

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_mood():
    return input("How are you feeling today? (one word): ").strip().lower()

def log_mood():
    mood = get_mood()
    info = MOOD_INFO.get(mood, DEFAULT)
    entry = {"date": str(date.today()), "mood": mood, "score": info["score"]}
    data = load_data()
    data.append(entry)
    save_data(data)
    print(f"Logged: {mood} {info['face']}")

def print_mood_chart(data, days=7):
    print("\nYour mood over the last days:")
    for entry in data[-days:]:
        bar_len = max(entry["score"] + 5, 0)   # shifts range (-4..5) to (1..10)
        bar = "#" * bar_len
        print(f"{entry['date']} | {bar} ({entry['mood']})")

if __name__ == "__main__":
    log_mood()
    data = load_data()
    print_mood_chart(data)