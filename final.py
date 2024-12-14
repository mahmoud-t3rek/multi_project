import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

def play_text():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        try:
            tts = gTTS(text, lang='en')
            tts.save("output.mp3")
            os.system("start output.mp3" if os.name == "nt" else "open output.mp3")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter some text to play.")

def clear_text():
    text_entry.delete("1.0", tk.END)

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Text-to-Speech App")
root.geometry("400x250")

label = tk.Label(root, text="Enter your Text: ", font=("Arial", 15))
label.pack(pady=5)

text_entry = tk.Text(root, wrap=tk.WORD, height=5, width=40, fg="black", font=("Arial", 12))
text_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10, fill=tk.X)

play_button = tk.Button(button_frame, text="Play", command=play_text)
play_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

exit_button = tk.Button(button_frame, text="Exit", command=exit_app)
exit_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

set_button = tk.Button(button_frame, text="Set", command=clear_text)
set_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

root.mainloop()
