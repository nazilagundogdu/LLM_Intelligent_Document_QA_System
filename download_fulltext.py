import pandas as pd
import json
import io
import pickle
import requests
import fitz  # PyMuPDF
from tqdm import tqdm
import os

# Paths
DATA_JSON = "data/alzheimer.json"
OUTPUT_PKL = "data/documents_doc.pkl"

df = pd.read_json(DATA_JSON).T

links = df['link']
titles = df['title']


# create a list to add the article texts to
documents = []

# get the corresponding link for a given title
for link, title in zip(links, titles):

    # replace 'abs' with 'pdf' in the link to access the content of the articles
    link = link.replace('abs', 'pdf')
    response = requests.get(link)
    try:
        # convert the content to bytes for PDF processing
        pdf_bytes= io.BytesIO(response.content)

        # open the PDF file using PyMuPDF (fitz) from the byte stream
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        print(f"Successfully opened PDF with {doc.page_count} page(s).")

        # initialize a variable to store the PDF contents in
        text = ""
        # loop extract text from the pdf file pages
        for index in range(len(doc)):
            page = doc[index]
            text = text + page.get_text()
        documents.append(text)
        doc.close()
    except fitz.FileDataError:
        print("The provided bytes do not represent a valid PDF file.")
