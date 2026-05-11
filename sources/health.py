import random


TASKS = [    
        "💧 Drink a full glass of water before you start coding.",
        "🧘 5 deep breaths. Inhale 4 counts, hold 4, exhale 4.",
        "👀 20-20-20 rule: every 20 mins, look 20 feet away for 20 seconds.",
        "🚶 Take a 10 minute walk before you sit down.",
        "🙆 Roll your shoulders back 10 times. You're hunched right now.",
        "📵 First 30 mins of your day — no phone, just code.",
        "🌅 Step outside for 5 minutes. Sunlight resets your focus.",
        "✍️  Write one thing you want to accomplish today before opening VS Code.",
        "🍎 Eat something real before coding. Not just chai.",
        "😴 Did you sleep 7+ hours? No? Close one tab today as punishment.",
        "🖐️  Shake out your hands and wrists. RSI is real.",
        "📖 Read one page of any book. Not Twitter. A book.",
        ]

class HealthSource:
    def fetch(self):
        return {"task": random.choice(TASKS)}
