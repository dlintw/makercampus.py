import threading
import requests
from bs4 import BeautifulSoup

urls = [
    "https://www.example.com",
    "https://www.example.org",
    "https://www.example.net"
]

def fetch_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find("title").text
        print(f"URL: {url}, Title: {title}")

threads = [threading.Thread(target=fetch_content, args=(url,)) for url in urls]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
