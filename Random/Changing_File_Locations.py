import os 
import shutil

# Changing all of the files from the webscrape folder to the Sorted "Hot" or "Not" folders for training
# doing this will make our two classes of pictures for training much easier to call 


def copy_images_to_target_folders(directory, target_folder):
    # Subfolders for Hot and Not images
    hot_folder = os.path.join(target_folder, 'Hot')
    not_folder = os.path.join(target_folder, 'Not')

    # List all the folders in the given directory
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

    for folder in folders:
        # Check if the folder name ends with '_0' or '_1'
        folder_path = os.path.join(directory, folder)
        
        if folder.endswith('_0'):
            destination = not_folder
        elif folder.endswith('_1'):
            destination = hot_folder
        else:
            print(f"Skipping folder: {folder}")
            continue
        
        print(f"Processing folder: {folder}")

        # Copy images from the current folder to the appropriate target folder
        for img in os.listdir(folder_path):
            img_path = os.path.join(folder_path, img)
            
            # Ensure the item is a file (and not a sub-directory)
            if os.path.isfile(img_path):
                shutil.copy2(img_path, destination)
                print(f"Copied {img_path} to {destination}")

directory = "/media/parker/4TB HD/Tinder_AI Training/Female_Pics"
target_folder = "/media/parker/4TB HD/Tinder_AI Training/Sorted_Folders"
copy_images_to_target_folders(directory, target_folder)