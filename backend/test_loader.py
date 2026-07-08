from ingestion.loader import DocumentLoader

loader = DocumentLoader()

docs = loader.load_documents("../seed_data")

print(f"Loaded {len(docs)} documents\n")

for doc in docs:

    print("=" * 60)
    print(doc.file_name)
    print(doc.content[:150])