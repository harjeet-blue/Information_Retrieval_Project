import pandas as pd
reader = pd.read_csv("/Users/varunparashar/Desktop/Information_Retrieval_Project/data_filtering/Apps - Apps.csv")
output = pd.DataFrame()
for row in range(0, len(reader)):
        pp = ""
        summary = ""
        currpp = reader.iloc[row]['Privacy Policy']
        currsum = reader.iloc[row]['Summary']

        for ch in currpp:
             temp = ""
             if(ch == '\"' or ch == '\'' ):
                  temp = '\\'+ch
             else:
                  temp = ch
             
             pp += temp

        for ch in currsum:
             temp = ""
             if(ch == '\"' or ch == '\''):
                  temp = '\\'+ch
             else:
                  temp = ch
             summary += temp
        new_row = {'App ID': reader.iloc[row]['App ID'], 'TypeID': reader.iloc[row]['TypeID'], 'App Name': reader.iloc[row]['App Name'], 'Privacy Policy': pp, 'Summary': summary, 'Score': reader.iloc[row]['Score'], 'Rating': reader.iloc[row]['Rating'], 'Paid':reader.iloc[row]['Paid']}
        output = output.append(new_row, ignore_index=True)
output.to_csv('/Users/varunparashar/Desktop/Information_Retrieval_Project/data_filtering/new_apps.csv', index=False)