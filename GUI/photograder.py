import os
import shutil
import tkinter as tk
from PIL import Image, ImageTk


class ImageBrowser(tk.Tk):
    def __init__(self, directory):
        super().__init__()
        self.title('Image Browser')
        
        # List all subdirectories in the provided directory
        self.folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
        self.folder_index = 0
        self.directory = directory
        
        self.image_label = tk.Label(self)
        self.image_label.pack()

        # Bind keys to functions
        self.bind('<Left>', lambda e: self.navigate_image(-1))  # Arrow key left
        self.bind('<Right>', lambda e: self.navigate_image(1))  # Arrow key right
        self.bind('<space>', lambda e: self.delete_image()) # to Delete the image in the folder
        self.bind('<f>', lambda e: self.rate_folder(1))  # '1' key for yes for the image in the folder 
        self.bind('<l>', lambda e: self.rate_folder(0))  # '0' key for no

        self.load_folder()
        
    def load_folder(self):
        folder_path = os.path.join(self.directory, self.folders[self.folder_index])
        self.image_files = [
            file for file in os.listdir(folder_path) if file.lower().endswith(('png', 'jpg', 'jpeg'))
        ]
        self.index = 0
    
        # Set the title of the window to the current folder name
        self.title(f"Image Browser - {self.folders[self.folder_index]}")
    
        if self.image_files:
            self.update_image()
        else:  # If no images are in the folder, go to the next folder
            self.rate_folder(0)

    def update_image(self):
        folder_path = os.path.join(self.directory, self.folders[self.folder_index])
        image_path = os.path.join(folder_path, self.image_files[self.index])
        pil_image = Image.open(image_path).convert('RGB')
    
        base_width = 500  # You can adjust this
        # Calculate the aspect ratio and resize while maintaining it
        w_percent = base_width / float(pil_image.width)
        h_size = int(float(pil_image.height) * float(w_percent))
        resized_image = pil_image.resize((base_width, h_size), Image.ANTIALIAS)

        tk_image = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image
    
    def navigate_image(self, step):
        self.index = (self.index + step) % len(self.image_files)
        self.update_image()
    
    def delete_image(self):
        folder_path = os.path.join(self.directory, self.folders[self.folder_index])
        image_path = os.path.join(folder_path, self.image_files[self.index])
        os.remove(image_path)
        self.image_files.pop(self.index)
        if self.image_files:  # if there are still images left in the folder, update the displayed image
            self.index = min(self.index, len(self.image_files) - 1)
            self.update_image()
        else:  # if no images are left in the folder, go to the next folder
            self.rate_folder(0)

    def rate_folder(self, rating):
        try:
            folder_path = os.path.join(self.directory, self.folders[self.folder_index])
            new_folder_name = f"{self.folders[self.folder_index]}_{rating}"
            new_folder_path = os.path.join(self.directory, new_folder_name)
        
            os.rename(folder_path, new_folder_path)
        
            # Debugging information
            print(f"Renamed {folder_path} to {new_folder_path}")
        
            self.folder_index += 1
            if self.folder_index < len(self.folders):
                self.load_folder()
            else:
                print("All folders rated")
                self.destroy()
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    root_directory = r"D:\Tinder_AI Training\Female_Pics" ### you will have to rename this spot for the directory of the images you want to rate
    app = ImageBrowser(root_directory)
    app.mainloop()
