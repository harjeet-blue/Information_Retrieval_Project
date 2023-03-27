import re
import string 
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
from nltk.stem import WordNetLemmatizer
import math 
import pickle
import numpy as np
nltk.download('punkt')
# nltk.download('wordnet')
import query as pt

AppID = {}           # AppName: ID
posDict = {}         #  'thrid party' : {  "Whatsapp": [3,4 ,5], }
total_words = {}     # AppID : total Words


def Preprocessing( data ):

    # define stopwords set
    stop_word_set = set(stopwords.words('english') + list(string.punctuation))

    #lowering the string
    data = data.lower()
    
    # tokenization
    sent_tokens = word_tokenize(data)

    # Removing stopwords & punctuations 
    sent_tokens = [ i for i in sent_tokens if i not in stop_word_set]
    
    # joining the tokens
    final_str = ' '.join(sent_tokens)
    
    #removal of non-char and non-numeric char
    final_str = re.sub(r'[^\w\s]', ' ', final_str)

    return final_str


# posDict = pickle.load( open('postionalIndex', 'rb'))
# AppID = pickle.load( open('appID', 'rb'))
# total_words = pickle.load ( open('totalWords', 'rb'))


def score(l,n):
    # l = [['a':occurence, 'b': occurence],[],[]...]---> a,b are apps, first list is list of occurences of a SPECIAL WORD in apps.
    score_list = np.zeros(n)
    s  = len(l)
    iml=[]
    weights = np.zeros(n*s).reshape(n,s)
    factor = np.zeros(n)
    for i in l:
        iml.append(list(i.values()))

    for k in range(len(iml)):
        for j in range(n):
            factor[j] += iml[k][j]  

    for j1 in range(n):
        for k in range(len(iml)):
            weights[j1][k] = iml[k][j1]/factor[j1] 

    iml = np.array(iml)
    iml = iml.T
    for j in range(n):
        score_list[j] = sum(list(map(lambda x, y: x * y, weights[j], iml[j])))

    final_score = {}
    for app in total_words.keys():
        final_score[app] = np.sum(score_list)/total_words[app]

    return final_score      # sorted by AppID


def score_calculation():
    query = ['data sharing', 'third party', 'advertisement']
    ans = []
    for word in query:
        temp = pt.query_processing(posDict, word, AppID)
        ans.append(temp)

    return score(ans, len(ans))


def update(text):

    df = pd.read_csv("Apps.csv")
    df.loc[len(df.index)] = [ len(df) + 1, 5, 'input', text, 'na', 0, 0, 0] 

    # new_row = pd.DataFrame( { 'App ID': len(df) + 1 , 'Type ID' : 5, 'App Name' : 'input', 'Privacy Policy' : text, 'Summary' : '', 'Score': 0, 'Rating' : 0, 'Paid': 0})
    df['App Name'] = df['App Name'].astype(str)
    df['Privacy Policy'] = df['Privacy Policy'].astype(str)
    df['App ID'] = df['App ID'].astype(int)
    df['clean policy'] = df['Privacy Policy'].apply(Preprocessing)

    for i in range(len(df)):

        AppID[df['App Name'][i]] = df['App ID'][i]

        data = df['clean policy'][i]
        single_tokens = data.split()
        app = df['App Name'][i]
        total_words[app] = len(single_tokens)

        # ************************ CODE TO CREATE POSITIONAL INVERTED LISTS *********************************

        for itr in range(0, len(single_tokens)):
            word = single_tokens[itr]

            if word not in posDict:                 # add only if that index is not present in the posDict
                
                posDict[word] = {}
                posDict[word][app] = [itr]

            else:
                if app in posDict[word]:
                    posDict[word][app].append(itr)
                else:
                    posDict[word][app] = [itr]

    
    # pickle.dump( posDict , open('postionalIndex', 'wb'))
    # pickle.dump( AppID, open('appID', 'wb'))
    # pickle.dump( total_words, open('totalWords', 'wb'))

    temp = score_calculation()

    for i in range(len(df)):
        df.loc[i, 'Score'] = temp[ str(df['App Name'][i]) ]

    df.to_excel('Apps.xlsx', index= False)
    return temp['input']


# print(update("thrid party"))

# print(score_calculation())