import tkinter as tk
from tkinter import ttk

# Create Window
window = tk.Tk()
window.geometry("280x320")
window.minsize(250, 320)
window.title("Cupos")

# Create a style object
style = ttk.Style()

# Configure the style
style.configure("TLabel", font=("Google Sans", 12))
style.configure("TButton", font=("Google Sans", 9))
style.configure("TCheckbutton", font=("Google Sans", 9))

#
head_label = ttk.Label(window, text="CuPos")
head_label.pack(pady=(10, 10))

coord_label = ttk.Label(window, text="x: 120 | y: 120", font=(20))
coord_label.pack(pady=(10, 10))

button_frame = ttk.Frame(window)
color_var = tk.BooleanVar()

color_check = ttk.Checkbutton(button_frame, text="Color Picker", variable=color_var)
color_check.grid(row=0, column=0)

copy_button = ttk.Button(button_frame, text="Copy All")
copy_button.grid(row=0, column=1)

button_frame.pack(pady=(10, 10))

log_box = tk.Text(window, height=10, width=30, state="disabled")
log_box.pack(fill=tk.BOTH, expand=True, pady=(10, 10))

window.mainloop()
