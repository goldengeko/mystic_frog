# Mystic Frog

Mystic Frog is a Python-based web scraper that downloads images from websites, organizes them into subfolders based on the website's URL, and detects QR codes in the downloaded images.

## Features

- Fetches and parses web pages to extract image URLs.
- Downloads images and organizes them into subfolders named after the website's domain.
- Validates downloaded images to ensure they are not corrupted.
- Detects QR codes in images using OpenCV and Pyzbar.
- Deletes images without QR codes to save storage.

## Requirements

The project requires the following Python libraries:

- `requests`
- `beautifulsoup4`
- `Pillow`
- `opencv-python`
- `pyzbar`
- `numpy`

Install the dependencies using:

```bash
pip install -r requirements.txt
```
**Usage:**

```bash
python3 mystic_frog.py <website_1_url>, <wenbsite_2_url>, ... <website_n_url>
```

**Example:**

```bash
python3 mystic_frog.py https://example.com
```
This will download all images from `https://example.com`, organize them into a folder named `example.com`, and detect QR codes in the images.
