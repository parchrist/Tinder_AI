import os

# This Script allows for you to be able to change the end of the file name, makes easier for Training


def rename_images_based_on_folder(directory):
    # List all the folders in the given directory
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

    for folder in folders:
        # Check if the folder name ends with '_0' or '_1'
        if folder.endswith('_0') or folder.endswith('_1'):
            print(f"Processing folder: {folder}")
            
            folder_path = os.path.join(directory, folder)
            
            # Extract the suffix from the folder name
            suffix = folder[-2:]

            # Rename the images inside the folder
            for img in os.listdir(folder_path):
                img_path = os.path.join(folder_path, img)
                
                # Make sure the item is a file (and not a sub-directory)
                if os.path.isfile(img_path):
                    base, ext = os.path.splitext(img)
                    new_name = f"{base}{suffix}{ext}"
                    new_path = os.path.join(folder_path, new_name)
                    
                    os.rename(img_path, new_path)
                    print(f"Renamed {img_path} to {new_path}")
        else:
            print(f"Skipping folder: {folder}")

directory = "/media/parker/4TB HD/Tinder_AI Training/Female_Pics"
rename_images_based_on_folder(directory)


