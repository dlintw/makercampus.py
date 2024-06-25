import requests
from bs4 import BeautifulSoup

urls = [
    'https://www.example.com',
    'https://www.example.org',
    'https://www.example.net'
]

def fetch_and_parse(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        title = soup.find('title').text
        description = soup.find('meta', attrs={'name': 'description'})
        if description:
            description = description.get('content')
        else:
            description = "No description available"
        return title, description
    else:
        return None, None

for url in urls:
    title, description = fetch_and_parse(url)
    print(f"URL: {url}")
    print(f"Title: {title}")
    print(f"Description: {description}")
    print('-' * 40)
