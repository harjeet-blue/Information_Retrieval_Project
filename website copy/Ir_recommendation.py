import numpy as np
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
        host = "localhost",
        username = "root",
        passwd = "7061",
        database = "ir_policy_db"
        )

def jac_sim(text1,text2):
  set1 = set(text1)
  set2 = set(text2)
  intersection = set1.intersection(set2)
  union = set1.union(set2)
  jaccard_sim = len(intersection) / len(union)
  return jaccard_sim

#df: df with apps name and score
#df2: df with appid and feature ids

df = pd.read_sql("select * from apps_table", con = mydb)
df2 = pd.read_sql("select * from app_features", con = mydb)

def get_recommendations(app_name):
  app_name=app_name.capitalize()
  perms = df2['featureID']
  appID = df2['appID']
  fapp = {}
  recommended=""
  for row in range(len(appID)):
      if(appID[row] not in fapp.keys()):
        fapp[appID[row]] = [perms[row]]
      else:
        fapp[appID[row]].append(perms[row])
  
  
  appID=list(fapp.keys())
  perms=[]
  for k in fapp.keys():
    perms.append(fapp[k])
  app = df['App_Name']
  key_feat=np.zeros(len(perms)*len(perms)).reshape(len(perms),len(perms))
  for i in range(len(perms)-2):
    for j in range(i+1,len(perms)-1):
      dist_features = jac_sim(perms[i], perms[j])
      key_feat[i][j]=dist_features
  print(key_feat, "PRINTING KEY FEAT")
  for i in range(len(key_feat)):
    f1=False
    if(df['App_Name'][i]==app_name):
      f1=False
      sorted = np.argsort(key_feat[i])[::-1]
      top_5 = sorted[:5]
      for j in top_5:
       
        if(df['Score'][df['App_Id']==appID[j]].item() <df['Score'][df['App_Name']==app_name ].item()):
          f1=True
        # print(app[j])
          recommended+=app[j]+" "
      # print(recommended)
      if(len(recommended)==0):
        print("No better app to recommend")
        return 'No better app to recommend'
  return "For",app_name,recommended