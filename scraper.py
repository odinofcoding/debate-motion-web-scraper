import requests
from bs4 import BeautifulSoup

url = "https://hellomotions.com/motions2020"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', class_='table table-striped')

if table:
    motions = []

    for row in table.find_all('tr'):
        columns = row.find_all('td')

        if len(columns) >= 3:
            motion_text = columns[3].get_text(strip=True)
            motions.append(motion_text)

    for motion in motions:
        print(motion)
else:
    print("Table with class 'table table-striped' not found.")
