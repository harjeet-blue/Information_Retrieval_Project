import pandas as pd
reader = pd.read_csv("/Users/varunparashar/Desktop/Information_Retrieval_Project/data_filtering/new_apps.csv")
query = "INSERT INTO `ir_policy_db`.`Apps_table` (`App_Id`, `type_id`, `App_Name`, `Privacy_policy`, `Summary`, `Score`, `Rating`, `Paid`) VALUES "
file1 = open("/Users/varunparashar/Desktop/Information_Retrieval_Project/data_filtering/query.txt","w")

for row in range(0, len(reader)):
    qtemp = query
    values = "("
    for col in range(0, len(reader.columns)):
        values += "\'" + str(reader.iat[row, col])+"\', "
    values = values[:len(values)-2]
    values += ");"
    qtemp += values + "\n"
    file1.write(qtemp)
file1.close()

