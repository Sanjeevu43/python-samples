
import chromadb
from chromadb.utils import embedding_functions
import uuid # For generating truly unique IDs

# --- Core Mechanics Explained with Chroma ---

# --- a) Data Ingestion ---
print("--- a) Data Ingestion ---")

# 1) Source Data:
# Let's define some sample text documents.
# In a real application, this could come from files, databases, APIs, etc.
source_data = [
    {
        "id": "article_001", # A user-defined unique ID (could also be generated)
        "content": "The quick brown fox jumps over the lazy dog. This is a classic pangram.",
        "category": "linguistics",
        "author": "unknown",
        "published_year": 2020
    },
    {
        "id": "product_A42",
        "content": "Introducing the new SuperPhone X, with an advanced AI camera and long-lasting battery.",
        "category": "electronics",
        "brand": "SuperTech",
        "release_year": 2023
    },
    {
        "id": "recipe_s003",
        "content": "A delicious recipe for apple pie: Combine apples, cinnamon, sugar, and bake in a preheated oven.",
        "category": "cooking",
        "cuisine": "dessert",
        "prep_time_minutes": 60
    },
    {
        "id": "news_report_7B",
        "content": "Researchers have made a breakthrough in quantum computing, potentially revolutionizing data processing.",
        "category": "science",
        "source_outlet": "Tech Today",
        "published_year": 2023
    }
]

# 2) Embedding Model:
# We'll use a pre-trained sentence transformer model.
# Chroma can use its default, or you can specify one.
# For clarity, let's specify one.
# all-MiniLM-L6-v2 is a good general-purpose model.
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)
print(f"Using embedding model: all-MiniLM-L6-v2")

# Initialize Chroma Client
# You can use an in-memory client or a persistent client.
# client = chromadb.Client() # In-memory, data lost on script exit
client = chromadb.PersistentClient(path="./chroma_db_store") # Persists data to disk

# Create or get a collection. A collection is where your vectors are stored.
# We specify the embedding function here.
# We can also set the distance metric for indexing (see 'Indexing' section below).
collection_name = "my_documents_collection"
try:
    client.delete_collection(name=collection_name) # Clear previous collection for demo
    print(f"Cleared existing collection: {collection_name}")
except:
    pass # Collection didn't exist, which is fine

collection = client.get_or_create_collection(
    name=collection_name,
    embedding_function=sentence_transformer_ef,
    metadata={"hnsw:space": "cosine"}  # Sets the distance function for HNSW index.
                                       # Common options: "l2" (Euclidean), "cosine", "ip" (inner product)
                                       # Default is "l2" if not specified.
)
print(f"Created/accessed collection: {collection_name} with cosine similarity.")


# 3) Storage: Storing vectors, IDs, original data reference, and metadata.
print("\n--- Storing Data ---")

documents_to_add = []
metadatas_to_add = []
ids_to_add = []

for item in source_data:
    # i) A unique ID for the vector:
    # We can use the ID from our source data or generate one.
    # Chroma requires string IDs.
    unique_id = str(item.get("id", uuid.uuid4())) # Use provided ID or generate a UUID
    ids_to_add.append(unique_id)

    # ii) The original data or a reference to it:
    # For text, we store the text itself in the `documents` field for Chroma.
    # If it were an image, 'documents' might be a path/URL, or you might embed the image directly if your model supports it.
    # Here, `item["content"]` is our original data.
    documents_to_add.append(item["content"])

    # iii) Optional metadata:
    # We can store any other relevant information as metadata.
    # This is a dictionary.
    metadata = {
        "category": item.get("category", "unknown"),
        "source_id": item.get("id", "N/A") # Storing the original ID again for easy reference
    }
    # Add any other fields from source_data to metadata
    for key, value in item.items():
        if key not in ["id", "content"]: # id is primary, content is the document
            metadata[key] = value
    metadatas_to_add.append(metadata)

    print(f"  Prepared ID: {unique_id}, Metadata: {metadata}")


# Add data to the collection
# Chroma will automatically use the `sentence_transformer_ef` to convert
# `documents_to_add` into embeddings.
collection.add(
    documents=documents_to_add,
    metadatas=metadatas_to_add,
    ids=ids_to_add
)

print(f"\nSuccessfully added {collection.count()} items to the collection '{collection_name}'.")

# --- b) Indexing (The Secret Sauce for Speed) ---
print("\n--- b) Indexing ---")
# ChromaDB handles indexing automatically.
# By default, for smaller datasets, it might perform exact nearest neighbor search.
# As the dataset grows, or by configuration, it uses ANN algorithms like HNSW (Hierarchical Navigable Small World).
# You typically don't need to manually trigger indexing for HNSW in Chroma after adding data;
# it's built as data is added/updated.
# The `metadata={"hnsw:space": "cosine"}` during collection creation tells Chroma
# to optimize its HNSW index for cosine similarity.

print("Chroma handles indexing automatically (typically HNSW).")
print("The similarity metric for indexing was set to 'cosine' during collection creation.")
# You can inspect collection metadata:
# print(collection.metadata) # Might not directly show HNSW params unless explicitly set beyond hnsw:space

# --- c) Querying ---
print("\n--- c) Querying ---")

# 1) Query Embedding:
# The search query is converted into a vector using the SAME embedding model.
query_text = "Tell me about AI or advanced technology"
print(f"Query: '{query_text}'")
# Chroma's `query` method handles embedding the `query_texts` automatically
# using the collection's configured embedding function.

# 2) ANN Search:
# Find the k vectors closest to the query vector.
num_results = 2
results = collection.query(
    query_texts=[query_text],       # List of query texts
    n_results=num_results,          # Number of top results to return
    # include=['metadatas', 'documents', 'distances'] # Specify what to return
)

# 3) Similarity Metrics:
# We chose 'cosine' similarity when creating the collection.
# Chroma returns 'distances'. For cosine similarity, distance = 1 - similarity.
# So, a smaller distance means higher similarity.

# 5) Results:
print("\n--- Query Results (No Filter) ---")
if results['ids'][0]:
    for i in range(len(results['ids'][0])):
        doc_id = results['ids'][0][i]
        distance = results['distances'][0][i]
        similarity = 1 - distance # For cosine
        document = results['documents'][0][i]
        metadata = results['metadatas'][0][i]

        print(f"  Rank {i+1}:")
        print(f"    ID: {doc_id}")
        print(f"    Similarity (Cosine): {similarity:.4f} (Distance: {distance:.4f})")
        print(f"    Document: {document[:100]}...") # Print first 100 chars
        print(f"    Metadata: {metadata}")
else:
    print("  No results found.")


# 4) Optional Filtering (Metadata Filtering):
print("\n--- Query Results (With Metadata Filter) ---")
query_text_filtered = "information about food"
category_filter = "cooking"
print(f"Query: '{query_text_filtered}' with filter: category = '{category_filter}'")

filtered_results = collection.query(
    query_texts=[query_text_filtered],
    n_results=num_results,
    where={"category": category_filter} # This is the metadata filter
    # include=['metadatas', 'documents', 'distances']
)

if filtered_results['ids'][0]:
    for i in range(len(filtered_results['ids'][0])):
        doc_id = filtered_results['ids'][0][i]
        distance = filtered_results['distances'][0][i]
        similarity = 1 - distance # For cosine
        document = filtered_results['documents'][0][i]
        metadata = filtered_results['metadatas'][0][i]

        print(f"  Rank {i+1}:")
        print(f"    ID: {doc_id}")
        print(f"    Similarity (Cosine): {similarity:.4f} (Distance: {distance:.4f})")
        print(f"    Document: {document[:100]}...")
        print(f"    Metadata: {metadata}")
else:
    print(f"  No results found for category '{category_filter}'.")

# Example of filtering with multiple conditions (e.g., published_year >= 2023)
# Chroma's `where` filter supports operators like $eq, $ne, $gt, $gte, $lt, $lte.
# For more complex queries, there's also $and and $or (check Chroma docs for exact syntax)
print("\n--- Query Results (With Advanced Metadata Filter) ---")
query_text_advanced_filter = "latest tech news"
print(f"Query: '{query_text_advanced_filter}' with filter: category = 'science' AND published_year >= 2023")

advanced_filtered_results = collection.query(
    query_texts=[query_text_advanced_filter],
    n_results=num_results,
    where={
        "$and": [
            {"category": {"$eq": "science"}},
            {"published_year": {"$gte": 2023}}
        ]
    }
    # include=['metadatas', 'documents', 'distances']
)

if advanced_filtered_results['ids'][0]:
    for i in range(len(advanced_filtered_results['ids'][0])):
        doc_id = advanced_filtered_results['ids'][0][i]
        distance = advanced_filtered_results['distances'][0][i]
        similarity = 1 - distance # For cosine
        document = advanced_filtered_results['documents'][0][i]
        metadata = advanced_filtered_results['metadatas'][0][i]

        print(f"  Rank {i+1}:")
        print(f"    ID: {doc_id}")
        print(f"    Similarity (Cosine): {similarity:.4f} (Distance: {distance:.4f})")
        print(f"    Document: {document[:100]}...")
        print(f"    Metadata: {metadata}")
else:
    print("  No results found for the advanced filter.")


# --- Clean up (optional, especially if using PersistentClient and want to remove the DB) ---
# To delete the collection:
# client.delete_collection(name=collection_name)
# print(f"\nCollection '{collection_name}' deleted.")
# To reset the entire database (deletes all collections in the persistent path):
# client.reset()
# print("\nChroma database reset (all collections deleted).")

print("\n--- Script Finished ---")