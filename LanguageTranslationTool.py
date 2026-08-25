import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def translate_text():
    src_lang = src_lang_cb.get()
    dest_lang = dest_lang_cb.get()
    text = input_text.get("1.0", tk.END).strip()
    
    if not text:
        messagebox.showwarning("Warning", "Please enter text to translate.")
        return
        
    src_code = [k for k, v in LANGUAGES.items() if v.title() == src_lang][0]
    dest_code = [k for k, v in LANGUAGES.items() if v.title() == dest_lang][0]
    
    translator = Translator()
    translated = translator.translate(text, src=src_code, dest=dest_code)
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated.text)

app = tk.Tk()
app.title("Language Translator - CodeAlpha")
app.geometry("500x400")

lang_list = [lang.title() for lang in LANGUAGES.values()]

tk.Label(app, text="Input Text:").pack(pady=5)
input_text = tk.Text(app, height=5, width=50)
input_text.pack()

frame = tk.Frame(app)
frame.pack(pady=10)

src_lang_cb = ttk.Combobox(frame, values=lang_list, state="readonly")
src_lang_cb.set("English")
src_lang_cb.grid(row=0, column=0, padx=5)

dest_lang_cb = ttk.Combobox(frame, values=lang_list, state="readonly")
dest_lang_cb.set("Urdu")
dest_lang_cb.grid(row=0, column=1, padx=5)

tk.Button(app, text="Translate", command=translate_text, bg="#007bff", fg="white").pack(pady=10)

tk.Label(app, text="Translated Text:").pack(pady=5)
output_text = tk.Text(app, height=5, width=50)
output_text.pack()

app.mainloop()
