import tkinter as tk
import keyboard
from tkinter import ttk
from mouse_info import get_mouse_info
from mouse_info import position_log
import pyautogui


# Functions
def update_logbox():
    # Clear the log_box
    for widget in log_box.winfo_children():
        widget.destroy()

    for item in position_log:
        text = tk.Text(log_box, height=1, width=30, state="normal")
        text.insert("1.0", str(item))
        text.configure(state="disabled")
        text.pack()

        # Bind left-click event
        text.bind("<Button-1>", lambda event, text=text: copy_to_clipboard(text))

        # Bind right-click event
        text.bind("<Button-3>", lambda event, text=text: delete_text(text))


def copy_all():
    window.clipboard_clear()
    window.clipboard_append(str(position_log))


def copy_to_clipboard(text_widget):
    text_widget.clipboard_clear()
    text_widget.clipboard_append(text_widget.get("1.0", "end-1c"))


def delete_text(text_widget):
    text = text_widget.get("1.0", "end-1c")
    text_widget.destroy()
    position_log.remove(eval(text))


def get_mouse_info_wrapper():
    get_mouse_info(color_var.get())


def update_label():
    x, y = pyautogui.position()
    coord_label.config(text=f"x: {x} | y: {y}")
    window.after(100, update_label)  # call update_label again after 100 ms


keyboard.add_hotkey("ctrl + shift + z", get_mouse_info_wrapper)
keyboard.add_hotkey("ctrl + shift + z", update_logbox)


# Window
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


head_label = ttk.Label(window, text="CuPos")
head_label.pack(pady=(10, 10))

coord_label = ttk.Label(window, text="x: 120 | y: 120", font=(20))
coord_label.pack(pady=(10, 10))

button_frame = ttk.Frame(window)

color_var = tk.BooleanVar()
color_check = ttk.Checkbutton(button_frame, text="Color Picker", variable=color_var)
color_check.grid(row=0, column=0)

copy_button = ttk.Button(button_frame, text="Copy All", command=copy_all)
copy_button.grid(row=0, column=1)


button_frame.pack(pady=(10, 10))

log_box = tk.Frame(window)
log_box.pack(fill=tk.BOTH, expand=True, pady=(10, 10))

update_label()  # start the label update loop
window.mainloop()
