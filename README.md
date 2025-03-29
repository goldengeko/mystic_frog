# Mystic Frog

Welcome to **Mystic Frog**, the web scraper that does all the dirty work for you. It downloads images from websites, throws them into folders like a lazy teenager cleaning their room, and scans them for QR codes, because a mystic frog asked me to, so why not? It’s like the Swiss Army knife of web scraping, but without the corkscrew. 

## Features

Here’s what Mystic Frog can do, because it’s awesome and you’re not (you never will be):

- Crawls the internet like your ex stalking your Instagram, grabbing image URLs from web pages.
- Downloads those images and organizes them into subfolders named after the website’s domain. Yes, it’s that organized. No, it won’t clean your mom's basement. You've still gotta do it after abusing kids on Call Of Duty.
- Checks if the images are valid because nobody likes broken files. That’s like getting socks for Christmas.
- Detects QR codes in images using OpenCV and Pyzbar. Unlike your drunk uncle's idea of “high tech,” this thing actually works.
- Deletes images without QR codes because they’re useless. Like the charger your mom gave you that doesn’t fit your phone.

## Requirements

Before you unleash the Frog, make sure you’ve got these Python libraries installed. If not, you’re going to have a bad time:

- `requests` (for grabbing stuff off the internet, like a digital kleptomaniac stealing your mom’s boyfriend's Wi-Fi)
- `beautifulsoup4` (for parsing HTML, not for making soup, Karen)
- `Pillow` (for image validation, not for napping, unlike your mom when she says she’s “working”)
- `opencv-python` (for seeing things, like Terminator vision, but you’re not nearly as cool as Arnold, sorry)
- `pyzbar` (for decoding QR codes, because QR codes are the future—way ahead of your mom’s understanding of modern technology)
- `numpy` (because math is hard, and Mystic Frog is smarter than you, or your mom, depending on the day)

Install them all with this magical command:

```bash
pip install -r requirements.txt

```
You know, the command you’ll ignore, and then wonder why it doesn’t work.

## Usage

So, you wanna use Mystic Frog? Here’s how you do it, Jesse James:

```bash
python3 mystic_frog.py <website_1_url>, <website_2_url>, ... <website_n_url>
```

### Example

```bash
python3 mystic_frog.py https://example.com
```

This will send Mystic Frog hopping over to `https://example.com`, download all the images it can find, and dump them into a folder named `example.com`. Then it’ll scan those images for QR codes like it’s looking for buried treasure. If it finds one, great! If not, the image gets yeeted into the void- just like your mom “yeets” your excuses when you forget to take the trash out.

## Disclaimer

Mystic Frog is not responsible for:

- Your internet bill after scraping 10,000 images because you didn’t read the documentation. But hey, it’s not like you actually read your mom’s texts, right?

- Any weird looks you get for downloading random images off the web. Maybe don’t explain what you’re doing to anyone. Just… don’t.

- The existential crisis you’ll have when you realize you just spent hours looking for QR codes, because let’s be real, that’s your life now.

Use responsibly, or don’t. I'm not Jo! Jo who, you ask? (ahahahahahahahahahahahahaha)

## License

This project is licensed under the MIT License, which means you can do whatever you want with it. Just don’t blame us if Mystic Frog becomes self-aware and starts downloading cat memes on its own. Honestly, I wouldn’t be surprised.
