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

# import pandas as pd
# reader = pd.read_csv("/Users/varunparashar/Desktop/Information_Retrieval_Project/data_filtering/new_apps.csv")
# query = "INSERT INTO `ir_policy_db`.`Apps_table` (`App_Id`, `type_id`, `App_Name`, `Privacy_policy`, `Summary`, `Score`, `Rating`, `Paid`) VALUES "
# file1 = open("query.txt","w")

# for row in range(0, len(reader)):
#     qtemp = query
#     values = "("
#     for col in range(0, len(reader.columns)):
#         values += "\'" + str(reader.iat[row, col])+"\', "
#     values = values[:len(values)-2]
#     values += ");"
#     qtemp += values + "\n"
#     file1.write(qtemp)
# file1.close()

# for row in range(0, len(reader)):
#         pp = ""
#         summary = ""
#         currpp = reader.iloc[row]['Privacy Policy']
#         currsum = reader.iloc[row]['Summary']
#         for ch in currpp:
#              temp = ""
#              if(ch == '\'' or ch == '\"'):
#                   temp = '\\'+ch
#              else:
#                   temp = ch
#              pp += temp

#         for ch in currsum:
#              temp = ""
#              if(ch == '\'' or ch == '\"'):
#                   temp = '\\'+ch
#              else:
#                   temp = ch
#              summary += temp
#         new_row = {'App ID': reader.iloc[row]['App ID'], 'TypeID': reader.iloc[row]['TypeID'], 'App Name': reader.iloc[row]['App Name'], 'Privacy Policy': pp, 'Summary': summary, 'Score': reader.iloc[row]['Score'], 'Rating': reader.iloc[row]['Rating'], 'Paid':reader.iloc[row]['Paid']}
#         output = output.append(new_row, ignore_index=True)