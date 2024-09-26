# this file create a schema in Weaviate 

import weaviate
import json

client = weaviate.Client(url="https://my-test-cluster-ag9b51je.weaviate.network")

print(client.is_ready()) # will return true 

class_obj = {
    "class": "Question",
    "vectorizer": "text2vec-huggingface",  # If set to "none" you must always provide vectors yourself. Could be any other "text2vec-*" also.
    "moduleConfig": {
        "text2vec-huggingface": {
            "model": "sentence-transformers/all-MiniLM-L6-v2",  # Can be any public or private Hugging Face model.
            "options": {
                "waitForModel": True
            }
        }
    }
}

client.schema.create_class(class_obj)

res = client.schema.get()
print(json.dumps(res, indent=2))
#print(res)
