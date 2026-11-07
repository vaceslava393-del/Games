
import tkinter as tk
import random
import os

progress = 0
timer = None

root = tk.Tk()
root.title("Geometry Dash Browser")
root.geometry("850x570")
root.configure(bg="#10131c")
root.resizable(False, False)

GREEN = "#35e58b"
BG = "#10131c"
PANEL = "#1c2230"

# Заголовок
tk.Label(
    root,
    text="GEOMETRY DASH BROWSER",
    font=("Arial", 24, "bold"),
    bg=BG,
    fg=GREEN
).pack(pady=30)

tk.Label(
    root,
    text="Downloading Geometry Dash...",
    font=("Arial", 17, "bold"),
    bg=BG,
    fg="white"
).pack(pady=20)

percent_label = tk.Label(
    root,
    text="0%",
    font=("Arial", 35, "bold"),
    bg=BG,
    fg=GREEN
)
percent_label.pack(pady=10)

canvas = tk.Canvas(
    root,
    width=650,
    height=30,
    bg="#30394b",
    highlightthickness=0
)
canvas.pack(pady=15)

bar = canvas.create_rectangle(
    0, 0, 0, 30,
    fill=GREEN,
    outline=""
)

status = tk.Label(
    root,
    text="Ожидание...",
    font=("Arial", 12),
    bg=BG,
    fg="white"
)
status.pack(pady=15)


def launch_fnaf():
    status.config(
        text="ЗАПУСК FNAF 2!",
        fg=GREEN
    )

    try:
        os.startfile("steam://run/332800")
    except Exception as error:
        status.config(text="Ошибка: " + str(error))


def download():
    global progress, timer

    progress += random.randint(2, 5)

    if progress > 100:
        progress = 100

    percent_label.config(text=str(progress) + "%")

    canvas.coords(
        bar,
        0, 0,
        650 * progress / 100, 30
    )

    status.config(
        text="Загрузка... " + str(progress) + "%"
    )

    if progress >= 100:
        status.config(
            text="ЗАГРУЗКА ЗАВЕРШЕНА!",
            fg=GREEN
        )

        root.after(2000, launch_fnaf)
        return

    timer = root.after(100, download)


def start():
    global progress

    progress = 0
    button.config(state="disabled")
    download()


button = tk.Button(
    root,
    text="НАЧАТЬ ЗАГРУЗКУ",
    font=("Arial", 15, "bold"),
    bg=GREEN,
    fg=BG,
    relief="flat",
    padx=35,
    pady=15,
    command=start
)
button.pack(pady=30)

root.mainloop()
