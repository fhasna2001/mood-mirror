def get_mood():
    return input("How are you feeling today? (one word): ").strip().lower()

def mood_face(mood):
    faces = {
        "happy": ":-D",
        "sad": ":-(",
        "angry": ">:-(",
        "calm": ":-)",
        "tired": "-_-",
        "excited": ":-O",
    }
    return faces.get(mood, ":-|")

def main():
    mood = get_mood()
    print(f"Got it. You're feeling {mood} {mood_face(mood)}")

if __name__ == "__main__":
    main()