import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class PhotoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikacja Zdjęć")

        self.image_label = tk.Label(root)
        self.image_label.pack(padx=10, pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.buttons = []
        for i in range(1, 6):
            button = tk.Button(
                self.button_frame, text=f"Zdjęcie {i}", command=lambda i=i: self.load_image(i))
            button.grid(row=0, column=i-1, padx=5, pady=5)
            self.buttons.append(button)

    def load_image(self, image_number):
        file_path = filedialog.askopenfilename(
            filetypes=[("Pliki obrazów", "*.jpg *.jpeg *.png *.gif")])
        if file_path:
            image = Image.open(file_path)
            image.thumbnail((300, 300))  # Dopasowanie rozmiaru do wyświetlenia
            photo = ImageTk.PhotoImage(image)

            self.image_label.config(image=photo)
            self.image_label.image = photo


if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoApp(root)
    root.mainloop()
