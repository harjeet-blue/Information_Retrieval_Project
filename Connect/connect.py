import mysql.connector

conn = mysql.connector.connect(host='localhost', password='7061', user='root', database = 'ir_policy_db')

if(conn.is_connected()):
    print('Connection Successful')
else:
    print('Connection Failed')




mycursor = conn.cursor()
str2="select ir_policy_db.Apps_table.App_Name, ir_policy_db.Apps_table.Summary, ir_policy_db.Apps_table.Score, ir_policy_db.Apps_table.Rating from ir_policy_db.Apps_table where ir_policy_db.Apps_table.App_Name = "
str3=str2+"\'"+"whatsapp"+"\';"
mycursor.execute(str3)
resultVAlue=mycursor.fetchall()

print(type(resultVAlue))

mycursor.execute("select * from ir_policy_db.Apps_table join ir_policy_db.app_permission join ir_policy_db.Permission where ir_policy_db.Apps_table.App_Id = ir_policy_db.app_permission.appID and ir_policy_db.app_permission.permissionID = ir_policy_db.Permission.PermissionID;")

result = mycursor.fetchall()
mycrsr=conn.cursor()
mycrsr.execute("select ir_policy_db.Apps_table.App_Id, ir_policy_db.Apps_table.App_Name, ir_policy_db.Apps_table.Privacy_policy, ir_policy_db.Apps_table.Summary, ir_policy_db.Permission.Name as Access, ir_policy_db.Permission.Description from ir_policy_db.Apps_table join ir_policy_db.app_permission join ir_policy_db.Permission where ir_policy_db.Apps_table.App_Id = ir_policy_db.app_permission.appID and ir_policy_db.app_permission.permissionID = ir_policy_db.Permission.PermissionID")
res=mycrsr.fetchall()


crsr=conn.cursor()
crsr.execute("select ir_policy_db.Apps_table.App_Id, ir_policy_db.Apps_table.App_Name, ir_policy_db.Apps_table.Privacy_policy, ir_policy_db.Apps_table.Summary, ir_policy_db.feature.description as Feature from ir_policy_db.Apps_table join ir_policy_db.app_features join ir_policy_db.feature where ir_policy_db.Apps_table.App_Id = ir_policy_db.app_features.appID and ir_policy_db.app_features.featureID = ir_policy_db.feature.featureID;")
res3=crsr.fetchall()

print(res3[0])
print(result[0])
print(res[0])


