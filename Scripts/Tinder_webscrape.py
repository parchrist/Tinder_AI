import requests
import os
import time

# set the URL of the API endpoint and the auth key
url = "https://api.gotinder.com/v2/recs/core?locale=en"
auth_key = "ur key here"

# set the save folder for the downloaded images

save_folder = "E:\Tinder_AI Training\More_Webscape"

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

def download_images(data):
    for result in data['data']['results']:
        user = result['user']
        name = user['name']
        user_id = user['_id']

        save_dir = f'E:\Tinder_AI Training\More_Webscape\{name}_{user_id}'
        os.makedirs(save_dir, exist_ok=True)

        for i, photo in enumerate(user['photos']):
            photo_url = photo['url']
            save_path = f'{save_dir}/{name}_{user_id}_{i+1}.jpeg'

            response = requests.get(photo_url)
            with open(save_path, "wb") as f:
                f.write(response.content)
            print(f"Downloaded image {i+1} for user {name} ({user_id})")

while True:
    headers = {"X-Auth-Token": auth_key}
    response = requests.get(url, headers=headers)

    data = response.json()
    download_images(data)
    print("Downloaded set 15 second delay has started...")

    time.sleep(15)