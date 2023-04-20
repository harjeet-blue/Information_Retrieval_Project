from transformers import T5Tokenizer, T5ForConditionalGeneration
import spacy
from collections import Counter
from string import punctuation
import pandas as pd
import torch
import re
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import string
import numpy as np
import joblib

# nlp = spacy.load("en_core_web_sm")
model_name = 't5-small'
tokenizer = T5Tokenizer.from_pretrained(model_name, model_max_length = 11000)
model = T5ForConditionalGeneration.from_pretrained(model_name)
device = torch.device('cpu')

# def get_hotwords(text):
#     result = []
#     pos_tag = ['PROPN', 'ADJ', 'NOUN'] 
#     doc = nlp(text.lower()) 
#     for token in doc:
#         if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
#             continue
#         if(token.pos_ in pos_tag):
#             result.append(token.text)
#     return resul

# def get_terms(text):
#     words=[]
#     output = set(get_hotwords(text))
#     most_common_list = Counter(output).most_common(10)
#     for item in most_common_list:
#         words.append(item[0])
#     return words
'''
def preprocess(pol):
  import nltk
  from nltk.corpus import stopwords 
  from nltk.tokenize import word_tokenize 
  import string
  nltk.download('stopwords')
  nltk.download('punkt')
  for i in range(len(pol)):
    pol[i] = pol[i].lower()
    for j in pol[i]:
      if(j in string.punctuation):
        # print(j)
        pol[i]=pol[i].replace(j," ")
        # print(pol[i])
    stop_words = set(stopwords.words('english')) 
    # print(pol[i])
    word_tokens = re.findall(r"[a-z]+|[A-Z]+", pol[i])
    # word_tokens = word_tokenize(pol[i])
  
  filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  pol[i] = filtered_sentence
  pol_pre = ""
  for i in range(len(pol)):
    for j in pol[i]:
      pol_pre+=" " +str(j)
  for i in range(len(pol)):
    temp = pol[i]
    pol[i]=""
    for j in temp:
      pol[i]+=j+" "
  l=[]
  l.append(pol_pre)
  l = np.array(l)
  return l

def get_keywords(l,pol):
  from sklearn.feature_extraction.text import CountVectorizer
  n_gram_range = (1, 1)
  stop_words = "english"
  from sentence_transformers import SentenceTransformer
  model = SentenceTransformer('all-mpnet-base-v2')

  # Extract candidate words/phrases
  count = CountVectorizer(ngram_range=n_gram_range, stop_words=stop_words).fit(l)
  candidates = count.get_feature_names_out()
  candidate_embeddings = model.encode(candidates)
  from sklearn.metrics.pairwise import cosine_similarity

  demd=[]
  for i in range(len(pol)):
    doc_embedding = model.encode([pol[i]])
    demd.append(doc_embedding)
  candidate_embeddings = model.encode(candidates)
  keyword_list=[]

  top_n = 10
  for i in range(len(demd)-1):
    distKey = cosine_similarity(demd[i], candidate_embeddings)
    keywords = [candidates[index] for index in distKey.argsort()[0][-top_n:]]
    keyword_list.append(keywords)
  return keyword_list
'''
def summarize_text(text, keywords=["key", "party", "reaching", "indicate", "recognition", "key", "spell", "written"]):
    privacy_terms = keywords
    text = text.strip().replace("\n","")
    prefix = "summarize: "
    for term in privacy_terms:
        prefix += f"{term};"
    t5_prepared_Text = prefix + text

    tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)
    summary_ids = model.generate(tokenized_text,
                                        num_beams=4,
                                        no_repeat_ngram_size=2,
                                        min_length=50,
                                        max_length=300,
                                        early_stopping=True)

    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return output

df = pd.read_csv("Apps - Apps.csv")
policy = df["Privacy Policy"]
# prepro = preprocess(policy)
# keywords = get_keywords(prepro, policy)
keywords = joblib.load("keywords_for_each_app_IR_Project")
count = 0
print(summarize_text(policy[0], keywords[0]))


