import joblib
import mysql.connector
mydb = mysql.connector.connect(
        host = "localhost",
        username = "root",
        passwd = "password",
        database = "ir_policy_db"
        )
summary_list = joblib.load("summary_list_final")
app_id = 1
mycur = mydb.cursor()
for entry in summary_list:
    summary = entry[0]
    sql = "UPDATE apps_table SET Summary =%s WHERE app_id = %s"
    val = (summary, app_id)
    mycur.execute(sql, val)
    app_id += 1
mydb.commit()
mydb.close()