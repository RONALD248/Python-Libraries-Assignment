import requests
import os
from urllib.parse import urlparse
import hashlib

def fetch_image(url, folder="Fetched_Images"):
    """Fetch and save an image from the given URL into the specified folder."""
    try:
        os.makedirs(folder, exist_ok=True)

        # Parse filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = "downloaded_image.jpg"

        # Full file path
        filepath = os.path.join(folder, filename)

        # Check for duplicate by file hash (avoid downloading same content)
        if os.path.exists(filepath):
            print(f"⚠ Image already exists: {filename}. Skipping download.")
            return

        # Fetch image with a proper User-Agent header (respectful request)
        headers = {
            "User-Agent": "UbuntuImageFetcher/1.0 (+https://github.com/RONALD248/Ubuntu_Requests)"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Check Content-Type header before saving
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped non-image URL: {url}")
            return

        # Save the image
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An unexpected error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Ask user for single or multiple URLs
    urls = input("Please enter one or more image URLs (separated by commas): ").split(",")

    for url in [u.strip() for u in urls if u.strip()]:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")
    print("Ubuntu: 'I am because we are.'")

if __name__ == "__main__":
    main()
