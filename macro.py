import tkinter as tk
from datetime import datetime
import csv

def save_text(text_entry):
    text = text_entry.get("1.0", tk.END).strip()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open("daily_notes.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([timestamp, text])
    except Exception as e:
        print(f"Error saving data: {e}")

    text_entry.delete("1.0", tk.END)
    window.destroy()

window = tk.Tk()
window.title("Text Entry and Save")
window.geometry("500x100")

label = tk.Label(window, text="Enter your text:")
label.pack()

text_entry = tk.Text(window, width=500, height=3, undo=False)
text_entry.bind("<Return>", lambda event: save_text(text_entry))
text_entry.focus_set()
text_entry.pack()

button = tk.Button(window, text="Save", command=lambda: save_text(text_entry))
button.pack()

window.mainloop()