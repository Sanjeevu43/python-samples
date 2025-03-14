from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import LlamaCpp
import os

# 1. Load and Prepare the Document (replace with your own text file)
# Create a dummy text file for demonstration:
# with open("./RAG/my_document.txt", "w") as f:
#     f.write("""
#     The capital of France is Paris.  Paris is known for its Eiffel Tower.
#     The capital of Germany is Berlin.  Berlin has many historical landmarks.
#     London is the capital of the United Kingdom.  London is famous for Big Ben.
#     Rome is the capital of Italy.  Rome has the Colosseum.
#     """)

loader = TextLoader("./RAG/my_document.txt")
documents = loader.load()
print('********************************* Doc Loaded **************************************')
# Split the document into chunks
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# 2. Embed the Text Chunks and Store in a Vector Database

# Using HuggingFaceEmbeddings (no API key required)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  #A good general-purpose embedding model

# Store the embeddings in ChromaDB (local, open-source)
persist_directory = "db"  # Directory to store the database
vectordb = Chroma.from_documents(documents=texts, embedding=embeddings, persist_directory=persist_directory)
vectordb.persist()  #Save the database to disk
vectordb = None #remove the object from memory after persisting it
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings) #Load the database when needed

# 3.  Load the Language Model (LlamaCpp - requires a model file)
# Download a quantized Llama 2 model from HuggingFace (e.g., "TheBloke/Llama-2-7B-Chat-GGML")
# and place it in the "models" directory.  Adjust the path accordingly.
# You'll need to install llamacpp: `pip install llama-cpp-python`
model_path = "models/llama-2-7b-chat.ggmlv3.q4_0.bin" # Replace with your model path
if not os.path.exists("models"):
    os.makedirs("models")

# Check if the model exists before proceeding
if not os.path.exists(model_path):
    print("Error: LlamaCpp model not found. Please download a quantized Llama 2 model and place it in the 'models' directory.")
    exit()

n_gpu_layers = 1  # Change this value based on your GPU's capabilities.
n_batch = 512  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.

# Make sure the model path is correct for your system!
llm = LlamaCpp(
    model_path=model_path,
    n_gpu_layers=n_gpu_layers,
    n_batch=n_batch,
    n_ctx=2048,
    verbose=False,
)

# 4. Create the RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # Other options: "map_reduce", "refine", "map_rerank"
    retriever=vectordb.as_retriever(search_kwargs={"k": 3}), # Number of documents to retrieve
    return_source_documents=True # Include the source documents in the output
)

# 5. Ask a Question
query = "What is the capital of France?"
result = qa_chain({"query": query})

# Print the result
print("Question:", query)
print("Answer:", result["result"])
print("Source Documents:")
for doc in result["source_documents"]:
    print(doc.page_content)