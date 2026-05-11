import random


TASKS = [
        "Drink 1 glass of water right now.",
        "Walk for 10 mins."
    ]

class HealthSource:
    def fetch(self):
        return {"task": random.choice(TASKS)}
