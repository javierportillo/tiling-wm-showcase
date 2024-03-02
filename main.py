import tkinter as tk
import sys


def create_window(background_color):
    window = tk.Toplevel(root)
    window.geometry("200x200")
    window.title("Tiling WM Showcase")
    window.configure(bg=background_color)


colors = [
    "#f2cdcd",
    "#f5c2e7",
    "#cba6f7",
    "#f38ba8",
    "#eba0ac",
    "#fab387",
    "#f9e2af",
    "#a6e3a1",
    "#94e2d5",
    "#89dceb",
    "#74c7ec",
    "#89b4fa",
    "#b4befe",
    "#cdd6f4",
    "#bac2de",
    "#a6adc8",
    "#9399b2",
    "#7f849c",
    "#6c7086",
    "#585b70",
    "#45475a",
    "#313244",
    "#1e1e2e",
    "#181825",
    "#11111b",
]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: tiling_wm_showcase.exe <num_windows>")
        sys.exit(1)

    try:
        num_windows = int(sys.argv[1])
    except ValueError:
        print("Invalid number of windows. Please provide an integer")
        sys.exit(1)

    root = tk.Tk()
    root.geometry("200x200")
    root.title("Tiling WM Showcase - Main")
    root.configure(bg="#f2cdcd")

    for i in range(num_windows - 1):
        color_index = (i + 1) % len(colors)
        create_window(colors[color_index])

    root.mainloop()
