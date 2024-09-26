import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification,AutoModel
from sentence_transformers import SentenceTransformer, util

#give me python example code with RAG

# Define your dataset (replace with your actual data)
documents = [
    "The quick brown fox jumps over the lazy dog.",
    "A lazy cat sleeps on a sunny window sill.",
    "The dog chased the squirrel up the tree.",
]

# Initialize the embedding model
embedding_model = SentenceTransformer('paraphrase-distilroberta-base-v1')

# Initialize the retrieval system (using cosine similarity)
def retrieve_documents(query, top_k=2):
    query_embedding = embedding_model.encode(query)
    document_embeddings = embedding_model.encode(documents)
    similarities = util.cos_sim(query_embedding, document_embeddings)[0]
    sorted_indices = torch.argsort(similarities, descending=True)
    return [documents[i] for i in sorted_indices[:top_k]]

# Initialize the language model for generation
# tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-mrpc")
# model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-mrpc")

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
#model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-mrpc")



# Example usage
query = "What does the dog do?"
query = "Had your luch?"

# Retrieve relevant documents
retrieved_documents = retrieve_documents(query)
print(f"Retrieved Documents:\n{retrieved_documents}\nn")

# Combine retrieved documents with the query for generation
input_text = "\n".join([query] + retrieved_documents)

# Generate the response
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model(**inputs)
print(f"Output:\n{outputs}")
#predicted_label = torch.argmax(outputs.logits).item()  # Assuming you have labels for classification
#predicted_label = torch.argmax(outputs).item()  # Assuming you have labels for classification

# Print the generated response
#print(f"Retrieved Documents:\n{retrieved_documents}\n\nGenerated Response: {predicted_label}")