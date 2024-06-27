import requests
import os
import time
import csv
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set the URL of the API endpoint and the auth key
url = "https://api.gotinder.com/v2/recs/core?locale=en"
auth_key = "9516f6ee-b9b4-440a-96d1-462991d48ed1"

# Set the save folders for the downloaded images and bios
image_save_folder = "E:/Tinder_AI Training/More_Webscape"
bio_save_folder = "E:/Tinder_AI Training/Bios"
csv_file = "E:/Tinder_AI Training/Bios/bios.csv"

# Create folders if they don't exist
os.makedirs(image_save_folder, exist_ok=True)
os.makedirs(bio_save_folder, exist_ok=True)

# Initialize the CSV file
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['user_id', 'name', 'bio'])

def download_images_and_save_bio(data):
    for result in data['data']['results']:
        user = result['user']
        name = user['name']
        user_id = user['_id']
        bio = user.get('bio', 'blank')

        # Save bio to CSV
        with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([user_id, name, bio])

        # Save bio to text file with unique ID
        bio_file_path = os.path.join(bio_save_folder, f"{user_id}_bio.txt")
        with open(bio_file_path, "w", encoding='utf-8') as bio_file:
            bio_file.write(bio)

        # Create directory for user's images
        user_image_folder = os.path.join(image_save_folder, f"{name}_{user_id}")
        os.makedirs(user_image_folder, exist_ok=True)

        # Download and save images
        for i, photo in enumerate(user['photos']):
            photo_url = photo['url']
            save_path = os.path.join(user_image_folder, f"{name}_{user_id}_{i+1}.jpeg")
            
            try:
                response = requests.get(photo_url)
                response.raise_for_status()  # Check for HTTP errors
                with open(save_path, "wb") as f:
                    f.write(response.content)
                logging.info(f"Downloaded image {i+1} for user {name} ({user_id})")
            except requests.exceptions.RequestException as e:
                logging.error(f"Error downloading image {i+1} for user {name} ({user_id}): {e}")

while True:
    headers = {"X-Auth-Token": auth_key}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        download_images_and_save_bio(data)
        logging.info("Downloaded set, 15-second delay has started...")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from API: {e}")
    
    time.sleep(15)

