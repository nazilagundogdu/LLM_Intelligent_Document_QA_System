# import libraries
import re
import urllib 
import feedparser
import json
import pandas as pd
import requests


# Base api query url
base_url = 'http://export.arxiv.org/api/query?';

# Search parameters -> TODO: generalize this
search_query = 'all:electron' # search for electron in all fields
start = 0                     # retreive the first 5 results
max_results = 5

query = 'search_query=%s&start=%i&max_results=%i' % (search_query,
                                                     start,
                                                     max_results)

d = feedparser.parse(base_url+query)

# create a dictionary to dump the data in
dict_format = {}

# define a list with the keys you want to exclude
entities_to_remove = ['id', 'guidislink', 'updated', 'updated_parsed', 'published_parsed', 'title_detail', 'summary_detail', 'author_detail',
                    'arxiv_doi', 'links', 'arxiv_comment', 'arxiv_journal_ref', 'arxiv_primary_category', 'tags']

# loop to add the relevant item from the query to the dictionary and delete the keys we don't want to keep
for i in range(len(d.entries)):
    dict_format[i] = dict(d.entries[i]) 
    for item in entities_to_remove:
        if item in dict_format[i]:
            del dict_format[i][item]
            
# write the data in a json file
with open('entry.json', 'w') as f:
    json.dump(dict_format, f, indent = 4)
    print(f'The data was written in {f}.')

# read the data in a dataframe
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
