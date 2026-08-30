import os
import glob
from app.services.vector_store import collection

kb_dir = "data/knowledge_base"
md_files = glob.glob(f"{kb_dir}/*.md")

documents = []
metadatas = []
ids = []

for file_path in md_files:
    filename = os.path.basename(file_path)
    doc_id = filename.replace('.md', '')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    documents.append(content)
    category = doc_id.split('_')[0]
    metadatas.append({"source": filename, "category": category})
    ids.append(doc_id)

print(f"Embedding and ingesting {len(documents)} documents into ChromaDB. This may take a moment...")
collection.upsert(documents=documents, metadatas=metadatas, ids=ids)
print(f"Success! Total documents in vector database: {collection.count()}")
