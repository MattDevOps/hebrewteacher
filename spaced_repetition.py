
import json
from datetime import date, timedelta

VOCAB_FILE = "vocab.json"

def load_vocab():
    with open(VOCAB_FILE) as f:
        return json.load(f)

def save_vocab(data):
    with open(VOCAB_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_due_words():

    data = load_vocab()

    today = date.today()

    due = []

    for w in data["words"]:
        if date.fromisoformat(w["next_review"]) <= today:
            due.append(w)

    return due

def mark_correct(word):

    data = load_vocab()

    for w in data["words"]:

        if w["hebrew"] == word:

            w["interval"] *= 2

            next_review = date.today() + timedelta(days=w["interval"])

            w["next_review"] = str(next_review)

    save_vocab(data)


def mark_wrong(word):

    data = load_vocab()

    for w in data["words"]:

        if w["hebrew"] == word:

            w["interval"] = 1

            w["next_review"] = str(date.today())

    save_vocab(data)
