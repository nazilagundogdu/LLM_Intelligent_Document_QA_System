# LLM_Intelligent_Document_QA_System (IN PROGRESS)

## This project is not finished and is still in progress. Please come back later! 


This project aims to build a Q&amp;A system that takes long documents (e.g. academic papers, manuals, legal docs) and allows users to ask questions in natural language. The system retrieves relevant content and uses an LLM to generate accurate, grounded answers.


For the purpose of this project, I focus on papers on "Alzheimer" disease published on `arXiv.org`. Due to limitation of computational resources, I limit my API call to only 1000 entries. 

**Step 1:** [`parse.py`](https://github.com/nazilagundogdu/LLM_Intelligent_Document_QA_System/blob/main/parse.py) downloads a `.json` file with metadata for 1000 papers on "Alzheimer".

**Step 2:** ['EDA.ipynb'](https://github.com/nazilagundogdu/LLM_Intelligent_Document_QA_System/blob/main/EDA.ipynb) provides a high level analysis of the data, e.g. number of authors, length of abstracts, etc.

**Step3:** [`Preprocessing&Modeling.ipynb`](Preprocessing&Modeling_clean.ipynb) includes feeding the data as part of a RAG (Retrieval Augmented Generation) architect, using [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/index.html) to handle document data, invoking an LLM from the `Hugging Face` library and an example of a QA.

