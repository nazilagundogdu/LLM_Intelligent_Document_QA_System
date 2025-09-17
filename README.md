# LLM_Intelligent_Document_QA_System (IN PROGRESS)

## 🚧 This project is currently under development. Please check back later!


This project aims to build a Question-Answering (QA) system for long documents (e.g., academic papers, manuals, legal documents) using a Retrieval-Augmented Generation (RAG) architecture. The system retrieves relevant chunks of content and uses a large language model (LLM) to generate accurate, grounded answers in natural language.

For this prototype, the focus is on academic papers about **Alzheimer's disease** published on [arXiv.org](https://arxiv.org/). Due to computational resource constraints, API calls are limited to **1,000 entries**.

---

### Notebooks

**Notebook 1:** [`EDA.ipynb`](https://github.com/nazilagundogdu/LLM_Intelligent_Document_QA_System/blob/main/EDA.ipynb)  
Exploratory Data Analysis — includes insights such as number of authors, abstract lengths, and other metadata distributions.

**Notebook 2:** [`Preprocessing&Modeling_Full_text.ipynb`](Preprocessing&Modeling_Full_text.ipynb)  
Implements the RAG pipeline: online full-text ingestion using [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/index.html), semantic chunking, vector embeddings, and LLM querying using Hugging Face models. This does not require anything to be saved locally on your laptop. To save time and resources, you could download the [documents_doc.pkl](documents_doc.pkl) (on the current repo) before running the notebook. 

---
### Python Script
A minimal, interactive Python script to test the QA system in the terminal via: `python alzheimer_pipeline_a.py`. This would require a local `json` file. It could be the file obtained via API call or a random `json` file on your laptop. The file used in the script is `entry.json`, available on the current repo. 



