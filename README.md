# 🦁 Ubuntu Image Fetcher

> “I am because we are.” — Ubuntu Philosophy

Welcome to the **Ubuntu Image Fetcher**, a mindful Python tool that connects to the global web community, respectfully fetches shared images, and organizes them for later appreciation.

This project is built in the spirit of **Ubuntu**, emphasizing **community**, **respect**, **sharing**, and **practicality**.

---

## 🌍 Project Overview

The **Ubuntu Image Fetcher** allows users to input one or more image URLs, downloads them responsibly, and stores them in a directory called `Fetched_Images`.

It includes thoughtful features such as:
- Graceful error handling for failed connections.
- Content-type validation to ensure only images are downloaded.
- Prevention of duplicate downloads.
- Support for multiple URLs in one run.

---

## ⚙️ Features

✅ Fetch single or multiple images from given URLs.  
✅ Automatically create a storage directory (`Fetched_Images`).  
✅ Avoid duplicate downloads.  
✅ Verify file type using HTTP headers before saving.  
✅ Respectful requests using a custom `User-Agent` header.  
✅ Clean, friendly terminal messages in the spirit of Ubuntu.

---

## 🧠 Requirements

Ensure Python 3.x is installed on your system.

Install dependencies using:

```bash
pip install requests
🚀 Usage
Run the script using:

bash
Copy code
python ubuntu_image_fetcher.py
Then enter one or more image URLs (comma-separated):

bash
Copy code
https://example.com/image1.jpg, https://example.com/image2.png
The program will:

Fetch each image from the web.

Save it inside the Fetched_Images/ folder.

Display success messages for each downloaded image.

🖼️ Example Output
pgsql
Copy code
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter one or more image URLs (separated by commas): https://example.com/ubuntu-wallpaper.jpg
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

Connection strengthened. Community enriched.
Ubuntu: 'I am because we are.'
⚠️ Precautions When Downloading
When fetching content from unknown sources:

Always check content type before saving (image/* only).

Set a timeout to prevent hanging requests.

Avoid very large files (optional size limit can be added).

Validate URLs before downloading.

Handle exceptions to keep the program running smoothly.

🫱🏽‍🫲🏾 Ubuntu Principles in Practice
Ubuntu Value	In This Program
Community	Connects respectfully with web resources.
Respect	Handles all errors gracefully without crashing.
Sharing	Organizes fetched images for easy access and reuse.
Practicality	Serves a useful real-world purpose.

📁 Folder Structure
markdown
Copy code
Ubuntu_Requests/
│
├── ubuntu_image_fetcher.py
├── README.md
└── Fetched_Images/
    └── (downloaded images will appear here)
🧑🏽‍💻 Author
Ronald Omondi Omollo
Full_Stack Developer.
📧 Email: omolloronald5@gmail.com
📞 Phone: 0715920019
🌐 GitHub:RONALD248

💬 Closing Words
“A person is a person through other persons.”
This tool reminds us that through code and connectivity, we thrive together — not alone.

yaml
Copy code

---

Would you like me to make a **shorter README version** (for class submission)
