import re
import string 
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
from nltk.stem import WordNetLemmatizer
import math 
import numpy as np
nltk.download('punkt')
# nltk.download('wordnet')
import query as pt
import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        username = "root",
        passwd = "7061",
        database = "ir_policy_db"
        )
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

    score_list = (score_list/max(score_list))*10

    return score_list      # sorted by AppID


def helper_function():
    query = ['data sharing', 'third party', 'advertisement']
    ans = []
    for word in query:
        temp = pt.query_processing(posDict, word, AppID)
        ans.append(temp)

    return score(ans, len(ans[0]))


def calculate_score():

    df = pd.read_sql("select * from apps_table", con = mydb)
    df['clean_policy'] = df['Privacy_policy'].apply(Preprocessing)

    for i in range(len(df)):

        AppID[df['App_Name'][i]] = df['App_Id'][i]

        data = df['clean_policy'][i]
        single_tokens = data.split()
        app = df['App_Name'][i]
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

    temp = helper_function()
    print("df lenght::", len(df))

    for i in range(len(df)):
        df.loc[i, 'Score'] = temp[ i ]

    df.drop('clean_policy', axis= 1)
    mycur = mydb.cursor()
    for i in range(1, len(df) + 1):
        sql = "UPDATE apps_table SET score =%s WHERE app_id = %s"
        if(math.isnan(temp[i-1])):
            temp[i-1]=0
        val = ( temp[i-1], i)
        mycur.execute(sql, val)
    mydb.commit()

    mydb.close()
    # overwrite MySQL table with updated DataFrame
    # df.to_sql('apps_table', mydb, if_exists='replace',index=False)