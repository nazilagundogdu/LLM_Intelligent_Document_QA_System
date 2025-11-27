# LLM_Intelligent_Document_QA_System 

## 1. Overview

This project implements an Intelligent Question-Answering (QA) System for long scientific documents using a Retrieval-Augmented Generation (RAG) architecture. The system retrieves semantically relevant text chunks from research papers and uses a lightweight large language model (LLM) to generate grounded, context-aware answers.

The prototype focuses on Alzheimer’s disease papers from [arXiv.org](arXiv.org). Due to compute limits, metadata was collected for 1,000 papers, and evaluation was tested both on abstracts only and full-text parsed PDFs.

The study evaluates the performance of `TinyLlama-1.1B-Chat-v1.0` under four prompt templates across:

- Embedding Models

  - `all-MiniLM-L6-v2`
  - `all-MiniLM-L12-v2`
  - `multi-qa-MiniLM-L6-cos-v1`

- Data Context

  - Abstracts only
  - Full paper text

**Key Result**

Model performance (Semantic Recall@5, threshold 0.5) shows the best configuration to be:

`multi-qa-MiniLM-L6-cos-v1` + full-text documents

*Improvement:* 0.597 → 0.690 in semantic similarity.

## 2. System Architecture
              
                ┌───────────────────────────┐
                │     User Query (Question) │
                └───────────────┬───────────┘
                                │
                                ▼      
                   ┌────────────────────────┐
                   │      Text Chunking     │
                   │  (SentenceSplitter)    │
                   └─────────────┬──────────┘
                                 │
                                 ▼
                   ┌────────────────────────┐
                   │  Embedding Generation  │
                   │ (MiniLM-based encoders)│
                   └─────────────┬──────────┘
                                 │
                                 ▼
                 ┌────────────────────────────────-┐
                 │   Semantic Similarity Search    │
                 │ (SentenceSplitter chunks +      │
                 │  cosine similarity retrieval)   │
                 └──────────────────┬──────────────┘
                                    │ Top-k segments
                                    ▼
                        ┌──────────────────────┐
                        │      LLM (RAG)       │
                        │ TinyLlama 1.1B Chat  │
                        └─────────────┬────────┘
                                      │
                                      ▼
                        ┌────────────────────────┐
                        │      Final Answer      │
                        │ (Concise, grounded)    │
                        └────────────────────────┘



## 3. Repository Structure
```
LLM_Intelligent_Document_QA_System/
│
├── data/
│   ├── alzheimer.json          # Metadata + abstracts
│   └── documents_doc.pkl       # Parsed full-text corpus
│
├── parse.py                    # Metadata + abstract retrieval
├── download_fulltext.py        # PDF downloading + parsing
│
├── EDA.ipynb                   # Dataset analysis
├── Modeling.ipynb              # RAG pipeline + evaluation
│
├── img/                        # Figures and diagrams
├── documentation/              # Additional documentation
└── README.md                   # Project documentation


```


## 4. How to Run

### 4.1. Clone the Repo
```
git clone https://github.com/nazilagundogdu/LLM_Intelligent_Document_QA_System.git
cd LLM_Intelligent_Document_QA_System
```

### 4.2. Retrieve Data

`python parse.py` to download metadata for 1000 entries on Alzheimer and stores in `data/alzheimer.json` __ The relevant parts can be modified to query a different keyword and change the limit

`python download_fulltext.py` to download full text using the metadata stored in `data/alzheimer.json`. If the previous script is modified for a new keyword, this script should be modified to reflect that. 

### 4.3. Run RAG Pipeline
`jupyter notebook Modeling.ipynb` 


## 5. Examples

Input question: *"What is the latest development in treating AD?"*

LLM Answer: 
*The latest development in treating AD is the use of chelation therapy to reduce
the levels of Aβ and Ca++ in the brain. This approach has shown promise in
reducing the symptoms of AD and may lead to new research possibilities for AD
therapy.*

## 6. Limitations
- `TinyLlama (1.1B)` provides compact inference but lacks the reasoning strength of larger LLMs.

- Some arXiv PDFs have complex layouts that reduce parsing accuracy.

- Evaluation is limited to a small set of prompt templates.

- Only `Recall@5` was assessed — precision, answer quality, and hallucination rates could be added in future work.
