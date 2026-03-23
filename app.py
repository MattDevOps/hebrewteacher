
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from ttkbootstrap import Style
import random

from ai import ask_ai, correct_hebrew
from progress import load_progress, add_xp
from curriculum import get_lessons
from spaced_repetition import get_due_words, mark_correct, mark_wrong

progress = load_progress()

def send():

    question = input_box.get()

    chat.insert(tk.END, f"\nYou: {question}\n")

    answer = ask_ai(question)

    chat.insert(tk.END, f"Teacher: {answer}\n")

    input_box.delete(0, tk.END)


def lesson():

    lessons = get_lessons(progress["level"])

    if not lessons:
        chat.insert(tk.END, "\nNo lessons for this level yet.\n")
        return

    l = random.choice(lessons)

    chat.insert(tk.END, "\n--- LESSON ---\n")

    chat.insert(tk.END, l["title"] + "\n")

    chat.insert(tk.END, l["content"] + "\n")

    progress["lessons_completed"].append(l["id"])

    add_xp(progress, 50)


def vocab_review():

    due = get_due_words()

    if not due:

        chat.insert(tk.END, "\nNo vocab due for review today.\n")

        return

    w = random.choice(due)

    current_word.set(w["hebrew"])

    chat.insert(tk.END, "\n--- WORD REVIEW ---\n")

    chat.insert(tk.END, f"What does this mean?\n{w['hebrew']}\n")


def mark_right():

    word = current_word.get()

    if word:

        mark_correct(word)

        chat.insert(tk.END, "Correct! Next review scheduled.\n")

        current_word.set("")


def mark_wrong_answer():

    word = current_word.get()

    if word:

        mark_wrong(word)

        chat.insert(tk.END, "Marked wrong. Will review again soon.\n")

        current_word.set("")


def grammar():

    sentence = input_box.get()

    chat.insert(tk.END, f"\nYou: {sentence}\n")

    result = correct_hebrew(sentence)

    chat.insert(tk.END, f"Correction:\n{result}\n")

    input_box.delete(0, tk.END)


def conversation():

    resp = ask_ai("Start a casual conversation in Hebrew like two Israelis talking.")

    chat.insert(tk.END, "\n--- CONVERSATION ---\n")

    chat.insert(tk.END, resp + "\n")


style = Style(theme="darkly")

root = style.master

root.title("Hebrew AI Teacher Pro")

current_word = tk.StringVar()

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Ask", command=send).pack(side=tk.LEFT,padx=5)
tk.Button(btn_frame, text="Lesson", command=lesson).pack(side=tk.LEFT,padx=5)
tk.Button(btn_frame, text="Word Review", command=vocab_review).pack(side=tk.LEFT,padx=5)
tk.Button(btn_frame, text="Right", command=mark_right).pack(side=tk.LEFT,padx=5)
tk.Button(btn_frame, text="Wrong", command=mark_wrong_answer).pack(side=tk.LEFT,padx=5)
tk.Button(btn_frame, text="Grammar Check", command=grammar).pack(side=tk.LEFT,padx=5)
tk.Button(btn_frame, text="Conversation", command=conversation).pack(side=tk.LEFT,padx=5)

chat = ScrolledText(root,height=25,width=90,wrap=tk.WORD)
chat.pack(padx=10,pady=10)

input_box = tk.Entry(root,width=70)
input_box.pack(side=tk.LEFT,padx=10,pady=10)

input_box.bind("<Return>", lambda e: send())

root.mainloop()
