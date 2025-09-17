import pandas as pd
from llama_index.core import SimpleDirectoryReader, Document, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.core.indices.list import ListIndex
from llama_index.llms.huggingface import HuggingFaceLLM
from huggingface_hub import notebook_login  # optional if using gated models


def preprocess(filename: str = "entry.json"):
    """
    Loads and preprocesses the data from a JSON file,
    creates vector embeddings, and returns a query engine.
    Using a smaller file (with metadata for only 5 papers to save on resources.
    """
    # Load data
    df = pd.read_json(filename).T

    # Convert summaries to Document objects
    documents = [Document(text=s) for s in df["summary"].tolist()]

    # Split into smaller chunks (nodes)
    splitter = SentenceSplitter(chunk_size=200, chunk_overlap=20)
    nodes = splitter.get_nodes_from_documents(documents)

    # Set embedding model
    Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Build vector index
    index = VectorStoreIndex.from_documents(documents, embed_model=Settings.embed_model)

    # Create query engine
    query_engine = index.as_query_engine()
    return query_engine


def initialize_llm():
    """
    Initializes and sets the Hugging Face LLM (TinyLlama) in global Settings.
    """
    llm = HuggingFaceLLM(
        model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        tokenizer_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        device_map="auto",
        context_window=2048,
        max_new_tokens=256,
    )
    Settings.llm = llm


def main():
    # Optional: Authenticate with Hugging Face if needed
    # notebook_login()

    # Step 1: Load LLM
    initialize_llm()

    # Step 2: Preprocess and build index
    query_engine = preprocess("entry.json")

    # Step 3: Ask a question
    question = input("Ask a question about Alzheimer's research: ")
    response = query_engine.query(question)

    print("\nAnswer:")
    print(response)



if __name__ == "__main__":
    main()
