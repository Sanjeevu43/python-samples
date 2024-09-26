import spacy

load_model = spacy.load("en_core_web_sm")
#load_model = spacy.load("en")

my_text = "This is just a sample text for the purpose of testing"

doc = load_model(my_text)

res = " ".join([token.lemma_ for token in doc])

print(res)