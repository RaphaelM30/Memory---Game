# Import
import tkinter as tk
import os
from PIL import Image, ImageTk
import random

image_folder = "./Images"
button_size = 10

# Main window
window = tk.Tk()
window.title("Memory Game")
window.geometry("1920x1080")
window.resizable(False, False)
window.configure(bg="#185580")
window.iconbitmap("./Assets/logo.ico")

# Main frame
game_frame = tk.Frame(window, bg="#185580")
game_frame.place(relx=0.5, rely=0.5, anchor="center")

clicked_buttons = []  # List of the clicked buttons by the player
clicked_images = []  # List of matching images to verify pairs

# Image loading
image_files = []
for f in os.listdir(image_folder):
    if f.endswith(".png"):
        path = os.path.join(image_folder, f).replace("\\", "/")
        image_files.append(path)

# Creation of Tkinter Object
images = []
for f in os.listdir(image_folder):
    if f.endswith(".png"):
        path = os.path.join(image_folder, f).replace("\\", "/")
        try:
            img = Image.open(path)
            img = img.resize((button_size, button_size), Image.Resampling.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)
            images.append(tk_img)
        except Exception as e:
            print("Erreur lors du chargement :", path, e)


buttons = []
game_images = images * 2
random.shuffle(game_images)

# Creation of the buttons
for i, img in enumerate(game_images):
    button = tk.Button(
        game_frame,
        text="?",
        font=("Arial", 28, "bold"),
        bg="white",
        width=button_size,  # Important : contrôle via pixel (voir dessous)
        height=button_size,
        compound="center",  # Image centrée
        relief="raised",
        bd=2,
    )
    button.grid(row=i // 5, column=i % 5, padx=10, pady=10)

    button.image = img

    # Function to execute when a button got clicked
    def click(btn=button, image=img):
        def on_click():
            btn.config(image=img, text="")
            clicked_buttons.append(btn)
            clicked_images.append(image)

            if len(clicked_buttons) == 2:
                window.after(1000, reset_buttons)

        return on_click

    button.config(command=click())
    buttons.append(button)


def reset_buttons():
    """Reset the clicked buttons to initial state"""
    for btn in clicked_buttons:
        btn.config(image="", text="?")
    clicked_buttons.clear()
    clicked_images.clear()


window.mainloop()
