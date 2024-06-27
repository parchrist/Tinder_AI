import os
import tkinter as tk
from PIL import ImageTk, Image

class PhotoGrader(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Photo Grader")

        self.image_label = tk.Label(self)
        self.image_label.pack()

        self.bind("<Left>", self.prev_image)
        self.bind("<Right>", self.next_image)
        self.bind("<a>", self.grade_yes)
        self.bind("<d>", self.grade_no)
        self.bind("<Delete>", self.delete_image)
        self.bind("<Escape>", lambda e: self.destroy())

        self.folder_path = filepath  # specify the folder path here
        self.image_files = []
        self.current_index = 0

        if os.path.exists(self.folder_path) and os.path.isdir(self.folder_path):
            self.load_folder(self.folder_path)
        else:
            print(f"Error: {self.folder_path} is not a valid directory.")
            self.destroy()

    def load_folder(self, folder_path):
        self.image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
        if self.image_files:
            self.show_image(0)

    def show_image(self, index):
        if 0 <= index < len(self.image_files):
            self.current_index = index
            image_path = os.path.join(self.folder_path, self.image_files[index])
            img = Image.open(image_path)
            img.thumbnail((300, 300))
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img

    def prev_image(self, event):
        if self.current_index > 0:
            self.show_image(self.current_index - 1)

    def next_image(self, event):
        if self.current_index < len(self.image_files) - 1:
            self.show_image(self.current_index + 1)

    def grade_yes(self, event):
        self.grade_image(1)

    def grade_no(self, event):
        self.grade_image(0)

    def grade_image(self, grade):
        if self.image_files:
            file_name = self.image_files[self.current_index]
            base, ext = os.path.splitext(file_name)
            new_name = f"{base}_{grade}{ext}"
            os.rename(os.path.join(self.folder_path, file_name), os.path.join(self.folder_path, new_name))
            self.image_files[self.current_index] = new_name

    def delete_image(self, event):
        if self.image_files:
            file_path = os.path.join(self.folder_path, self.image_files.pop(self.current_index))
            os.remove(file_path)
            if self.image_files:
                self.show_image(min(self.current_index, len(self.image_files) - 1))
            else:
                self.image_label.config(image=None)

if __name__ == "__main__":
    filepath = "/4TB HD/Tinder_AI Training/Female_Pics"  # Specify your file path here
    app = PhotoGrader()
    app.mainloop()
