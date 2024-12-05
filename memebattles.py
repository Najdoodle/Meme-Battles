import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from random import shuffle
memes = [
    "meme1.jpg", "meme2.jpg", "meme3.jpg",
    "meme4.jpeg", "meme5.jpeg", "meme6.jpeg",
    "meme7.jpg", "meme8.jpg"
]
shuffle(memes)
current_round = memes[:]
next_round = []
round_number = 1
winner_declared = False
bgclour = "#000000"
Tl = "#FFFF00"
BUTTON_COLOR = "#000000"
HIGHLIGHT_COLOR = "#FFFF00"
FONT_TITLE = ("Onyx", 30, "bold")
FONT_TEXT = ("Onyx", 16)
FONT_BUTTON = ("Onyx", 18, "bold")
root = tk.Tk()
root.title("Meme Battles Tournament")
root.geometry("800x720")
root.configure(bg=bgclour)
def start_tournament():
    """Start the meme tournament."""
    home_frame.pack_forget()
    tournament_frame.pack(fill="both", expand=True)
    update_ui()
def go_home():
    """Return to the home screen."""
    if winner_declared:
        reset_tournament()
    tournament_frame.pack_forget()
    home_frame.pack(fill="both", expand=True)
def reset_tournament():
    """Reset the tournament state."""
    global current_round, next_round, round_number, winner_declared
    shuffle(memes)
    current_round = memes[:]
    next_round = []
    round_number = 1
    winner_declared = False
    update_ui()
def update_ui():
    """Update the tournament UI to display the current memes."""
    global current_round, next_round, round_number
    if len(current_round) < 2:
        if len(next_round) == 1:
            declare_winner(next_round[0])
        else:
            round_number += 1
            current_round = next_round[:]
            next_round = []
            update_ui()
        return
    round_label.config(text=f"Round {round_number} — Battles Left: {len(current_round) // 2}")
    meme1_path, meme2_path = current_round[0], current_round[1]
    display_meme(meme1_label, meme1_path)
    display_meme(meme2_label, meme2_path)
    meme1_button.config(command=lambda: vote(meme1_path))
    meme2_button.config(command=lambda: vote(meme2_path))
def display_meme(label, meme_path):
    """Display a resized version of the meme in the given label."""
    img = Image.open(meme_path).resize((350, 350))
    img_tk = ImageTk.PhotoImage(img)
    label.config(image=img_tk)
    label.image = img_tk
def vote(winner):
    """Register a vote for the given meme and update the round."""
    global current_round, next_round
    next_round.append(winner)
    current_round.pop(0)
    current_round.pop(0)
    update_ui()
def declare_winner(winning_meme):
    """Display the winning meme."""
    global winner_declared
    winner_declared = True
    for widget in tournament_frame.winfo_children():
        widget.pack_forget()
    winner_label = tk.Label(tournament_frame, text="🏆 Meme Champion 🏆", font=FONT_TITLE, bg=bgclour, fg=HIGHLIGHT_COLOR)
    winner_label.pack(pady=20)
    winner_img = Image.open(winning_meme).resize((400, 400))
    winner_img_tk = ImageTk.PhotoImage(winner_img)
    winner_meme = tk.Label(tournament_frame, image=winner_img_tk, bg=bgclour)
    winner_meme.image = winner_img_tk
    winner_meme.pack(pady=20)
    home_button = tk.Button(tournament_frame, text="Home", font=FONT_BUTTON, bg=BUTTON_COLOR, fg="white", command=go_home)
    home_button.pack(pady=20)
home_frame = tk.Frame(root, bg=bgclour)
home_title = tk.Label(home_frame, text="Meme Battles", font=FONT_TITLE, fg=Tl, bg=bgclour)
home_title.pack(pady=40)
home_instructions = tk.Label(
    home_frame,
    text="Welcome to Meme Battles! \nA single-elimination tournament to decide the ultimate meme champion.\nClick Start to begin!",
    font=FONT_TEXT,
    fg=Tl,
    bg=bgclour,
    justify="center",
)
home_instructions.pack(pady=20)
start_button = tk.Button(home_frame, text="Start Tournament", font=FONT_BUTTON, bg=BUTTON_COLOR, fg="white", command=start_tournament)
start_button.pack(pady=40)
home_frame.pack(fill="both", expand=True)
tournament_frame = tk.Frame(root, bg=bgclour)
round_label = tk.Label(tournament_frame, text="", font=FONT_TEXT, fg=Tl, bg=bgclour)
round_label.pack(pady=10)
meme_frame = tk.Frame(tournament_frame, bg=bgclour)
meme_frame.pack(expand=True, fill="both", pady=20)
meme1_label = tk.Label(meme_frame, bg=bgclour)
meme1_label.pack(side="left", padx=10)
meme2_label = tk.Label(meme_frame, bg=bgclour)
meme2_label.pack(side="right", padx=10)
button_frame = tk.Frame(tournament_frame, bg=bgclour)
button_frame.pack(pady=20)
meme1_button = tk.Button(button_frame, text="Vote Meme 1", font=FONT_BUTTON, bg=BUTTON_COLOR, fg="white", command=None)
meme1_button.pack(side="left", padx=20)
meme2_button = tk.Button(button_frame, text="Vote Meme 2", font=FONT_BUTTON, bg=BUTTON_COLOR, fg="white", command=None)
meme2_button.pack(side="right", padx=20)
root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())
root.mainloop()
