import re
import string 
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')

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
    return final_str.split()


def OR(l1, l2):

    i = 0
    j = 0
    
    ans = []

    while i < len(l1) and j < len(l2):

        if l1[i] == l2[j]:
            ans.append(l1[i])
            i = i + 1
            j = j + 1

        elif l1[i] < l2[j]:
            ans.append(l1[i])
            i = i+1
        else:
            ans.append(l2[j])
            j = j+1


    while i < len(l1):
        ans.append(l1[i])
        i = i + 1
    
    while j < len(l2):
        ans.append(l2[j])
        j = j + 1

    return ans
    


def AND( l1, l2):
    i = 0
    j = 0
    
    ans = []

    while i < len(l1) and j < len(l2):

        if l1[i] == l2[j]:
            ans.append(l1[i])
            i = i+1
            j = j+1

        elif l1[i] < l2[j]:
            i = i+1
        else:
            j = j+1

    return ans


def NOT(l):   
    ans = []
    
    for i in range(1, 1401):
        if i not in l:
            ans.append(i)

    return ans


def ANDNOT(l1 , l2):            # l1 and not l2
    i = 0
    j = 0

    ans = []

    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            i = i + 1
            j = j + 1

        elif l1[i] < l2[j]:
            ans.append(l1[i])
            i = i + 1
        else:
            j = j + 1


    while i < len(l1):
        ans.append(l1[i])
        i = i + 1

    return ans

def ORNOT(l1, l2):

    l3 = ANDNOT(l2, l1)
    return NOT(l3)


def helper( l1, l2):
    i = 0
    j = 0
    
    ans = []

    while i < len(l1) and j < len(l2):

        if l1[i]+1 == l2[j]:
            ans.append(l1[i]+1)
            i = i+1
            j = j+1

        elif l1[i] < l2[j]:
            i = i+1
        else:
            j = j+1

    return ans

#*********************************************** QUERY PROCESSING *******************************************************


def positional_query(query, posDict):

    potential = list(posDict[query[0]].keys())

    for i in range(1, len(query)):
        potential = AND(potential, list( posDict[query[i]].keys()) )

    ans = []
    
    for file in potential:
        temp = posDict[query[0]][file]
        for word in range(1, len(query)):
            temp = helper(temp, posDict[query[word]][file] )
        if( len(temp) != 0 ):
            ans.append(file)
    
    return ans


def organize_ans( posDict, query, AppID, app_list):
    temp = {}
    for app, ID in AppID.items():

        if app not in app_list:
            temp[ID] = 0
            continue

        freq = 1e9
        for word in query:
            freq = min( len(posDict[word][app]), freq )

        temp[ID] = freq

    return temp

def query_processing(posDict, query, AppID):

    query = Preprocessing(query)

    try: 
        ans =  positional_query(query, posDict)

    except KeyError:
        print("\n No such token exists in any files :\n ")

    return organize_ans(posDict, query, AppID, ans)


