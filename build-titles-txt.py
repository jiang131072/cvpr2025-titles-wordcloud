import re

import requests
from bs4 import BeautifulSoup

url = "https://cvpr.thecvf.com/Conferences/2025/AcceptedPapers"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table")
titles = table.select("tr > td > strong")
with open("cvpr2025.txt", "w") as f:
    for title in titles:
        f.write(re.sub(r"\s+", " ", title.get_text(strip=True)) + "\n")
