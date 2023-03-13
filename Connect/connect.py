import mysql.connector
conn = mysql.connector.connect(host='localhost', password='password', user='root', database = 'ir_policy_db')

if(conn.is_connected()):
    print('Connection Successful')
else:
    print('Connection Failed')

mycursor = conn.cursor()

mycursor.execute("select * from ir_policy_db.Apps_table join ir_policy_db.app_permission join ir_policy_db.Permission where ir_policy_db.Apps_table.App_Id = ir_policy_db.app_permission.appID and ir_policy_db.app_permission.permissionID = ir_policy_db.Permission.PermissionID;")
result = mycursor.fetchall()
print(result[0])


