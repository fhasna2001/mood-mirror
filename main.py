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
        bar_len = max(entry["score"] + 5, 0)
        bar = "#" * bar_len
        print(f"{entry['date']} | {bar} ({entry['mood']})")

def mood_weather(data, days=5):
    recent = data[-days:]
    if not recent:
        print("Not enough data yet for a forecast.")
        return
    avg = sum(e["score"] for e in recent) / len(recent)
    if avg >= 3:
        print("Forecast: Sunny skies ahead — you've been in great spirits!")
    elif avg >= 0:
        print("Forecast: Partly cloudy — a mix of ups and downs.")
    elif avg >= -2:
        print("Forecast: Rainy patch — take it easy on yourself.")
    else:
        print("Forecast: Stormy stretch — maybe talk it through with someone you trust.")

def main():
    while True:
        print("\n=== MoodMirror ===")
        print("1) Log today's mood")
        print("2) View mood chart")
        print("3) Get mood weather forecast")
        print("4) Quit")
        choice = input("Choose an option: ").strip()

        data = load_data()
        if choice == "1":
            log_mood()
        elif choice == "2":
            print_mood_chart(data)
        elif choice == "3":
            mood_weather(data)
        elif choice == "4":
            print("See you tomorrow!")
            break
        else:
            print("Please choose 1-4.")

if __name__ == "__main__":
    main()