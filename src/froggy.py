import requests
from bs4 import BeautifulSoup
import os
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from urllib.parse import urljoin
from PIL import Image

def fetch_page(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        if response.status_code == 200: # Check for successful response
            return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}") 
    return None

def extract_images(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    images = []
    for img in soup.find_all("img"):
        src = img.get("src")
        if src:
            src = urljoin(base_url, src)  # Properly handle relative URLs
            images.append(src)
    return images

def download_image(url, base_url, folder="images"):
    # Create a subfolder based on the base URL
    subfolder_name = base_url.replace("http://", "").replace("https://", "").split("/")[0]
    subfolder_path = os.path.join(folder, subfolder_name)
    os.makedirs(subfolder_path, exist_ok=True)
    
    # Generate the filename
    filename = os.path.join(subfolder_path, url.split("/")[-1])
    
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200:
            with open(filename, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            
            # Validate image
            try:
                Image.open(filename).verify()
            except Exception:
                print(f"Invalid image, deleting: {filename}")
                os.remove(filename)
                return None
            
            return filename
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
    return None

def contains_qr(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return False
    qr_codes = decode(img)
    return len(qr_codes) > 0

def process_websites(urls):
    for url in urls:
        if not url.startswith("http"):
            print(f"Skipping invalid URL: {url}")
            continue
        print(f"Scraping {url}...")
        html = fetch_page(url)
        if html:
            image_urls = extract_images(html, url)
            for img_url in image_urls:
                img_path = download_image(img_url, url)  # Pass the base URL here
                if img_path and contains_qr(img_path):
                    print(f"QR Code found in {img_path}")
                elif img_path is not None:
                    os.remove(img_path)  # Delete if no QR code
                else:
                    print("Warning: img_path is None, skipping deletion.")

def main():
    urls = input("Enter the URL(s) to scrape (comma-separated): ")
    urls = [url.strip() for url in urls.split(",") if url.strip()]
    
    if not urls:
        print("No valid URLs provided.")
        return
    
    print("Processing the following URLs:")
    for url in urls:
        print(url)
    print("Starting the scraping process...")
    process_websites(urls)

if __name__ == "__main__":
    main()
