import pandas as pd
reader = pd.read_csv("/Users/varunparashar/Desktop/Information_Retrieval_Project/data_filtering/Apps - features_with_apps.csv", chunksize=1)
output = pd.DataFrame()

for row in reader:
    id = int(row['AppID'])
    perm = list(row['Feature ID'])
    if(isinstance(perm[0], str)):
        perm = perm[0].split(',')
    for i in perm:
        new_row = {'AppID': id, 'Feature ID': i}
        output = output.append(new_row, ignore_index=True)
        
output.to_csv('/Users/varunparashar/Desktop/Information_Retrieval_Project/data_filtering/apps_features.csv', index=False)


reader = pd.read_csv("/Users/varunparashar/Desktop/Information_Retrieval_Project/data_filtering/Apps - permission.csv", chunksize=1)
output = pd.DataFrame()

for row in reader:
    id = int(row['AppID'])
    perm = list(row['Permissions required'])
    if(isinstance(perm[0], str)):
        perm = perm[0].split(',')
    for i in perm:
        new_row = {'AppID': id, 'Permissions required': i}
        output = output.append(new_row, ignore_index=True)
        
output.to_csv('/Users/varunparashar/Desktop/Information_Retrieval_Project/data_filtering/apps_permission.csv', index=False)