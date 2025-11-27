# LLM_Intelligent_Document_QA_System 

## 1. Goal and Setup

This project aims to build a Question-Answering (QA) system for long documents (e.g., academic papers, manuals, legal documents) using a Retrieval-Augmented Generation (RAG) architecture. The system retrieves relevant chunks of content and uses a large language model (LLM) to generate accurate, grounded answers in natural language.

For this prototype, the focus is on academic papers about **Alzheimer's disease** published on [arXiv.org](https://arxiv.org/). Due to computational resource constraints, API calls are limited to **1,000 entries** and only the abstracts of the papers.


This study compares the performance of `TinyLlama-1.1B-Chat-v1.0` on 4 pre-defined prompts using:

- 3 different sentence embedding models:
  -  `all-MiniLM-L6-v2`
  -  `all-MiniLM-L12-v2`
  -  `multi-qa-MiniLM-L6-cos-v1`

-  different context:
    - abstracts only
    - full paper text 


The evaluation of model performance using "Semantic Recall @5" with the similarity threshold of 0.5 concludes the best combination to be the use `multi-qa-MiniLM-L6-cos-v1` embedding model on full paper text. This combination improves the semantic similarity score from 0.597 to 0.690.





## 2. The Code

### 2.1. Python Script

**Script 1:** `parse.py` makes an API call to [arXiv.org](arXiv.org) that pulls metadata with abstracts for 1000 papers on "Alzheimer". To save on API invocation costs, the data is made available in this repo under `alzheimer.json` in the data folder. 

The full papers are downloaded using `PyMuPDF` python library, and are available in this repo under `documents_doc.pkl` file. 


### 2.2. Notebooks

**Notebook 1:** [`EDA.ipynb`](https://github.com/nazilagundogdu/LLM_Intelligent_Document_QA_System/blob/main/EDA.ipynb)  
Exploratory Data Analysis — includes insights such as number of authors, abstract lengths, and other metadata distributions.

**Notebook 2:** [`Modeling.ipynb`](Modeling.ipynb)  
Implements the RAG pipeline: Loading the pre-downloaded data, semantic chunking, vector embeddings, and LLM querying using Hugging Face models. 

---





