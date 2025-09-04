import pandas as pd
import requests

df = pd.read_json('entry.json', orient = 'index')

links = df['link']
titles = df['title']

for link, title in zip(links, titles):
    link = link.replace('abs', 'pdf')
    response = requests.get(link)
    if response.status_code == 200:
        filename = f'{title}.pdf'
        with open(filename, 'wb') as f: 
            f.write(response.content)
            print(f"PDF downloaded and saved as '{title}'")
    else: 
        print(f"Failed to fetch data for {title}, Status Code: {response.status_code}")

        