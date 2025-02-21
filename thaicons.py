import tkinter as tk
import random

# List of Thai consonants and their names
thai_consonants = [
    ("ก", "gor kai"), ("\u0e02", "khor khai"), ("\u0e03", "khor khuat"),
    ("\u0e04", "khor khwai"), ("\u0e05", "khor khon"), ("\u0e06", "khor ra-khang"),
    ("\u0e07", "ngor ngu"), ("\u0e08", "jor jaan"), ("\u0e09", "chor ching"),
    ("\u0e0a", "chor chang"), ("\u0e0b", "sor so"), ("\u0e0c", "chor choe"),
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        self.root.geometry("300x200")
        
        self.card_frame = tk.Frame(root, width=300, height=200)
        self.card_frame.pack(expand=True, fill=tk.BOTH)
        
        self.card_label = tk.Label(self.card_frame, text="", font=("Arial", 50))
        self.card_label.pack(expand=True)
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
        self.flip_button.pack(side=tk.LEFT, expand=True)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack(side=tk.RIGHT, expand=True)
        
        self.is_flipped = False
        self.current_card = None
        
        self.next_card()
        
    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.card_label.config(text=self.current_card[0])
        self.is_flipped = False
        
    def flip_card(self):
        if not self.is_flipped:
            self.card_label.config(text=self.current_card[1])
            self.is_flipped = True
        else:
            self.card_label.config(text=self.current_card[0])
            self.is_flipped = False

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()

