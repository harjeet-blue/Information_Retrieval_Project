import pandas as pd
reader = pd.read_csv("/Users/varunparashar/Desktop/IR_project/Apps - features_with_apps.csv", chunksize=1)
output = pd.DataFrame()
for row in reader:
    id = int(row['AppID'])
    perm = list(row['Feature ID'])
    if(isinstance(perm[0], str)):
        perm = perm[0].split(',')
    for i in perm:
        new_row = {'AppID': id, 'Permissions required': i}
        output = output.append(new_row, ignore_index=True)
        
output.to_csv('app_features.csv', index=False)