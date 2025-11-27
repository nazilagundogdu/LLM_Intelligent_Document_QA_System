# LLM_Intelligent_Document_QA_System 



This project aims to build a Question-Answering (QA) system for long documents (e.g., academic papers, manuals, legal documents) using a Retrieval-Augmented Generation (RAG) architecture. The system retrieves relevant chunks of content and uses a large language model (LLM) to generate accurate, grounded answers in natural language.

For this prototype, the focus is on academic papers about **Alzheimer's disease** published on [arXiv.org](https://arxiv.org/). Due to computational resource constraints, API calls are limited to **1,000 entries** and only the abstracts of the papers.

---

### Python Script

**Script 1:** `parse.py` makes an API call to [arXiv.org](arXiv.org) that pulls metadata for 1000 papers on "Alzheimer". To save on API invocation costs, the data is made available in this repo under `alzheimer.json` in the data folder. 

---
### Notebooks

**Notebook 1:** [`EDA.ipynb`](https://github.com/nazilagundogdu/LLM_Intelligent_Document_QA_System/blob/main/EDA.ipynb)  
Exploratory Data Analysis — includes insights such as number of authors, abstract lengths, and other metadata distributions.

**Notebook 2:** [`Preprocessing&Modeling_Abs_.ipynb`](Preprocessing&Modeling_Abs_.ipynb)  
Implements the RAG pipeline: Loading the pre-downloaded data (via running `parse.py` , semantic chunking, vector embeddings, and LLM querying using Hugging Face models. 

---





