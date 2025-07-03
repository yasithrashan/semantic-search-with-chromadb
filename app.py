import chromadb

# Initialize ChromaDB client
client = chromadb.Client()

# Create or get a collection
collection = client.create_collection(name="my_documents")

# Read the text file
def read_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# Split text into chunks
def split_into_chunks(text):
    chunks = text.split('\n\n')
    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
    return chunks

# Add documents to ChromaDB
def add_documents_to_collection(collection, chunks):
    ids = [f"doc_{i}" for i in range(len(chunks))]
    collection.add(
        documents=chunks,
        ids=ids
    )
    print(f"Added {len(chunks)} documents to ChromaDB!")

# Search function
def search_documents(collection, query, n_results=2):
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results

# Load and store documents
text_content = read_text_file('sample_data.txt')
chunks = split_into_chunks(text_content)
add_documents_to_collection(collection, chunks)

# Test the search
query = "What came out in 2017?"
search_results = search_documents(collection, query)

print(f"\nSearch Query: '{query}'")
print(f"Found {len(search_results['documents'][0])} relevant documents:")
print("\nRelevant documents:")
for i, doc in enumerate(search_results['documents'][0]):
    print(f"{i+1}: {doc}")

