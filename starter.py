from llama_index import VectorStoreIndex, SimpleDirectoryReader
import logging
import sys
import os.path
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    # load the documents and create the index
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)


query_engine = index.as_query_engine()
response = query_engine.query("llama index 를 시작하려면?")
print(type(response))
print(response.metadata)
print(response)

response = query_engine.query("임진왜란때 강화도에서는 무슨일이 있었어?")

print(type(response))
print(response.metadata)
print(response)


