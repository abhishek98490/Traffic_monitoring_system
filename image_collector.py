import requests
from bs4 import BeautifulSoup
import os
import schedule
import time 

base_url = 'https://onemotoring.lta.gov.sg/content/onemotoring/home/driving/traffic_information/traffic-cameras/'
camera_locations = [
    'woodlands', 'bke', 'sle', 'kje', 'aye', 'stg', 'mce', 'ecp', 'pie', 'kpe', 'cte', 'tpe', 'ltm']

previous_images = {}

def fetch_traffic_images(base_url, location):
    url = base_url + location + '.html#trafficCameras'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        img_urls = []
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if img_url and img_url.startswith('//datamall.lta.gov.sg'):
                img_url = 'https:' + img_url
                img_urls.append(img_url)
        
        return img_urls
    else:
        print(f"Failed to fetch data for {location}")
        return []

def download_images(img_urls):
    for idx, img_url in enumerate(img_urls):
        try:
            img_data = requests.get(img_url).content
            file_path = f"data/traffic_image_{time.time()}.jpg"
            with open(file_path, 'wb') as f:
                f.write(img_data)
            print(f"Image {idx + 1} downloaded: {img_url}")
        except Exception as e:
            print(f"Error downloading image {idx + 1}: {e}")

def fetch_and_download_traffic_images():
    global previous_images
    for location in camera_locations:
        current_images = fetch_traffic_images(base_url, location)
        
        # Compare with previous images for this location
        if location not in previous_images or set(current_images) != set(previous_images[location]):
            print(f"Images have changed for {location}. Downloading new images...")
            download_images(current_images)
            previous_images[location] = current_images
        else:
            print(f"No change in images for {location}")


schedule.every(1).minutes.do(fetch_and_download_traffic_images)


while True:
    i = 1
    print(f"itter{i}")
    schedule.run_pending()
    time.sleep(60)
    i+=1
