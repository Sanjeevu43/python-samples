import weaviate
import requests
import json

import newspaper
import uuid
from tqdm import tqdm

# web-scrape
def get_articles_from_newspaper(
         news_url: str, 
         max_articles: int=200
     ) -> None:
     """
     Download and save newspaper articles as weaviate schemas.
     Parameters
     ----------
     newspaper_url : str
         Newspaper title.
     """
     
     objects = []
     
     # Build the actual newspaper    
     news_builder = newspaper.build(news_url, memoize_articles=False)
     print('******************* news_builder size ************** : ', news_builder.size())
     
     if max_articles > news_builder.size():
         max_articles = news_builder.size()
     pbar = tqdm(total=max_articles)
     pbar.set_description(f"{news_url}")
     i = 0
     while len(objects) < max_articles and i < news_builder.size():
         article = news_builder.articles[i]
         try:
             article.download()
             article.parse()
             article.nlp()

             if (article.title != '' and \
                 article.title is not None and \
                 article.summary != '' and \
                 article.summary is not None and\
                 article.authors):
 
                 # create an UUID for the article using its URL
                 article_id = uuid.uuid3(uuid.NAMESPACE_DNS, article.url)
 
                 # create the object
                 objects.append({
                     'id': str(article_id),
                     'title': article.title,
                     'summary': article.summary,
                     'author': str(article.authors[0])
                 })
                 
                 pbar.update(1)
 
         except:
             # something went wrong with getting the article, ignore it
             pass
         i += 1
     pbar.close()
     return objects
data = []
data += get_articles_from_newspaper('https://www.theguardian.com/international')
#data += get_articles_from_newspaper('http://cnn.com')
#data = get_articles_from_newspaper('https://www.thehindu.com/')
#print(data)
# print(type(data))
# new_data = data[slice(2)]

# for d in new_data:
#     #print('i=',i)
#     print(d['title'])
#     print(d['summary'])
#     print(d['author'])

# create client
client = weaviate.Client(url="https://my-test-cluster-ag9b51je.weaviate.network")
print(client.is_ready())

# create schema
article_class_schema = {
    "class": "Article",
    "description": "An Article class to store the article summary and its authors",
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

client.schema.create_class(article_class_schema)
res = client.schema.get()
print(json.dumps(res, indent=2))

# Configure a batch process
with client.batch(
    batch_size=100
) as batch:
    # Batch import all Questions
    i = 0
    for d in data:
        print(f'importing article : {i+1}')
        properties = {
            "title": d['title'],
            "summary": d['summary'],
            "author": d['author'],
        }
        client.batch.add_data_object(properties, "Article")