import os
import requests

# Define the GitHub URL and the local directory where images will be saved
github_url = "https://github.com/OTA-Tech-AI/OTA-Tarot"
branch = "main"
image_folder_path = "src/images"
local_dir = "images"

# Create the local directory if it does not exist
if not os.path.exists(local_dir):
    os.makedirs(local_dir)

# Function to download and save images
def download_image(image_url, save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {save_path}")
    else:
        print(f"Failed to download: {image_url}")

# Function to scrape the GitHub page and download images
def download_images_from_github():
    api_url = f"https://api.github.com/repos/OTA-Tech-AI/OTA-Tarot/contents/{image_folder_path}?ref={branch}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        files = response.json()
        for file in files:
            if file['type'] == 'file' and file['name'].lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
                download_image(file['download_url'], os.path.join(local_dir, file['name']))
    else:
        print(f"Failed to retrieve the GitHub directory: {api_url}")

# Run the downloading process

