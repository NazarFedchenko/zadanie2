import tkinter as tk
from tkinter import messagebox
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sys, os




def generate_numbers():
    try:
        n = int(entry_N.get())
        a = int(entry_A.get())
        b = int(entry_B.get())
        c = int(entry_C.get())
    except ValueError:
        messagebox.showerror("Chyba", "Zadajte platné celé čísla!")
        return

    if n <= 0:
        messagebox.showerror("Chyba", "N musí byť kladné celé číslo!")
        return

    if a > b:
        a, b = b, a  # Prehodenie hodnôt, ak používateľ zadal rozsah opačne

    numbers = [random.randint(a, b) + c for _ in range(n)]

      # Aplikovanie filtra pre záporné čísla, ak je zaškrtnuté
    if show_negatives.get():
        numbers = [x for x in numbers if x < 0]

    # Vymazanie výstupného textového poľa
    output_box.delete(1.0, tk.END)

    if numbers:
        output_box.insert(tk.END, "\n".join(map(str, numbers)))
    else:
        output_box.insert(tk.END, "Žiadne záporné čísla")

    # Kreslenie grafu
    ax.clear()
    ax.bar(range(len(numbers)), numbers)
    ax.set_title("Graf upravených čísel")
    ax.set_xlabel("Index")
    ax.set_ylabel("Hodnota")
    canvas.draw()


# ----- GUI -----

# Funkcia na získanie cesty k zdrojom (pre PyInstaller)
def resource_path(relative_path):

    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

root = tk.Tk()
root.title("Generátor čísel ⟨A, B⟩ + C")
root.geometry("600x500")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

ICON_FILE = "icon2.ico"

ICON_FILE = "icon2.ico"

# Funkcia na nastavenie ikony aplikácie
def _set_icon(root: tk.Tk):

    base_dir = os.path.dirname(os.path.abspath(__file__))
    ico_path = os.path.join(base_dir, ICON_FILE)
    if os.path.isfile(ico_path):
        try:
            root.iconbitmap(ico_path)
        except (tk.TclError, OSError) as e:
            print(f"⚠️ Іконку не вдалося завантажити: {e}")


root.title("Generátor čísel ⟨A, B⟩ + C")

# Volanie funkcie na nastavenie ikony
_set_icon(root)

try:
    from PIL import Image, ImageTk
    bg_image = Image.open(resource_path("Background.jpg"))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
except Exception as e:
    print(f"⚠️ Background not loaded: {e}")





# Inputs
# Дозволяємо головному вікну адаптуватися при зміні розміру
for i in range(8):  # бо у тебе рядки 0–7
    root.rowconfigure(i, weight=1)
for j in range(2):  # бо у тебе колонки 0–1
    root.columnconfigure(j, weight=1)
    

tk.Label(root, text="N (počet čísel):").grid(row=0, column=0, sticky="e")
entry_N = tk.Entry(root)
entry_N.insert(0, "10")
entry_N.grid(row=0, column=1)

tk.Label(root, text="A (dolná hranica):").grid(row=1, column=0, sticky="e")
entry_A = tk.Entry(root)
entry_A.insert(0, "-10")
entry_A.grid(row=1, column=1)

tk.Label(root, text="B (horná hranica):").grid(row=2, column=0, sticky="e")
entry_B = tk.Entry(root)
entry_B.insert(0, "10")
entry_B.grid(row=2, column=1)

tk.Label(root, text="C (konštanta):").grid(row=3, column=0, sticky="e")
entry_C = tk.Entry(root)
entry_C.insert(0, "0")
entry_C.grid(row=3, column=1)

show_negatives = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Zobraziť len záporné", variable=show_negatives).grid(row=4, column=0, columnspan=2)

tk.Button(root, text="Generovať", command=generate_numbers, bg="#4CAF50", fg="white").grid(row=5, column=0, columnspan=2, pady=10)

# Output text box
output_box = tk.Text(root, height=8, width=30)
output_box.grid(row=6, column=0, columnspan=2, pady=10)

# Matplotlib figure
fig, ax = plt.subplots(figsize=(5, 2))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
