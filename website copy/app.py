from urllib import request
from flask import Flask, render_template, request, redirect,url_for
from flask_mysqldb import MySQL
import mysql.connector
import indexing as idxx
import torch 
import summary as smr
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config
import Ir_recommendation as rec


import chatBot as chatBot
# import indexing as idxx
input_text=""
score=0
model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')
device = torch.device('cpu')
conn = mysql.connector.connect(host='localhost', password='7061', user='root', database = 'ir_policy_db')
# import yaml

app = Flask(__name__)

# db=yaml.load(open('db.yaml'))
# app.config['MYSQL_HOST']=db['mysql_host']
# app.config['MYSQL_USER']=db['mysql_user']
# app.config['MYSQL_PASSWORD']=db['mysql_password']
# app.config['MYSQL_DB']=`db['mysql_db']
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='7061'
app.config['MYSQL_DB']='ir_policy_db'

mysql=MySQL(app)

def summarize_text(text):
    
  preprocess_text = text.strip().replace("\n","")
  t5_prepared_Text = "summarize: "+preprocess_text

  tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)

  # summmarize 
  summary_ids = model.generate(tokenized_text,
                                      num_beams=4,
                                      no_repeat_ngram_size=2,
                                      min_length=50,
                                      max_length=300,
                                      early_stopping=True)

  output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

  return output
@app.route("/", methods=['GET', 'POST'])
def template():
    if request.method=='POST':
        # print("heu")
        userDetails=request.form
        # cur=mysql.connection.cursor()
        # cur.execute("select count(*) from user_details")
        # result = cur.fetchall()
        # userid=result[0][0]+2
        result1=userDetails["App_Name"]
        print(result1)
    # Pass the result to the next page
        return redirect(url_for('result', result=result1))
        # mycursor.execute(str3)
        # resultVAlue=mycursor.fetchall()
        # print(resultVAlue )
        # mysql.connection.commit()
        # 
        # return redirect('/homepage')
        # Homepage(str3)
    return render_template('index.html')

def privacyScore(summary):
    return 0
def summary(policy):

    return "this is very good policy"
@app.route('/process_input', methods=['POST'])
def process_input():
    App_Name = request.form['input_text1']
    Privacy_policy = chatBot.generate_ans_chatbot("write privacy policy of "+ App_Name)
    type_id = int(request.form['input_text3'])
    
    cursor = mysql.connection.cursor()
    cursor.execute("select count(*) from apps_table")
    result = cursor.fetchall()
    App_id=result[0][0]+1
    # Process the input here
   
    summary1= summarize_text(Privacy_policy) 
    Rating=0
    Paid=0
    

    sql = "INSERT INTO apps_table (App_id, type_id, App_Name, Privacy_policy, Summary, Score, Rating, Paid) VALUES (%s,%s, %s,%s,%s, %s,%s,%s)"
    val = (App_id, type_id, App_Name, Privacy_policy, summary1, 0, Rating, Paid)
   
    
    cursor.execute(sql, val)
    mysql.connection.commit()
    global score
    idxx.calculate_score()
    
    str2="SELECT score FROM apps_table WHERE app_name = ";
    str3=str2+"\'"+App_Name+"\';"
    val=(App_Name)
    cursor.execute(str3)
    result = cursor.fetchall()[0][0]
    res=[(App_Name,summary1,result)]
    
    # summary1 +="It's Privacy Score is:: "+ str(result) 
    # result.append(privacyscore)
    print("score",result)
    return render_template('newpolicy.html', result=res)
@app.route('/newpolicy')
def newpolicy():
    summary1 = request.args.get('summary1')
    privacyscore=privacyScore(summary1)
    result=[]
    result.append((summary1,score))
    # print(type(summary1))
    return render_template('newpolicy.html', result=result)


@app.route('/input')
def input():
    return render_template('NotFound.html')

@app.route('/recomendationInput', methods=['POST'])
def recomendationInput():
    App_Name = request.form['input_text1']
    recomendApp=rec.get_recommendations(App_Name)
    print(recomendApp)
    return render_template('recScreen.html', input=recomendApp)




@app.route('/recomendation')
def recomendation():
    return render_template('recomendation.html')
    
@app.route('/result')
def result():
    result1 = request.args.get('result')
    print(len(result1))
    mycursor = conn.cursor()
    str2="select ir_policy_db.Apps_table.App_Name, ir_policy_db.Apps_table.Summary, ir_policy_db.Apps_table.Score, ir_policy_db.Apps_table.Rating from ir_policy_db.Apps_table where ir_policy_db.Apps_table.App_Name = "
    str3=str2+"\'"+result1+"\';"
        # val=(app_name)
    mycursor.execute(str3)
    result = mycursor.fetchall()
    print(len(result))
    if(len(result)==0):
       return redirect(url_for('input'))
    mycursor.close()
    return render_template('result.html', result=result)





@app.route('/homepage')

def Homepage():
    # cur=mysql.connection.cursor()
    # resultVAlue=cur.execute("select DISTINCT(seller_id) from (select seller_id from product_table) AS temp1 where seller_id NOT IN(SELECT seller_id FROM (select* from(select DISTINCT(seller_id)from product_table) AS temp2 cross join (select type_id from type_table) AS temp3)AS temp4 WHERE (seller_id,type_id) NOT IN( select seller_id,type_id from product_table));")
    # if resultVAlue>0:
    #     userDetails=cur.fetchall()
    return render_template('homepage.html')




@app.route('/AskPandSellPdiff1000')   
def AskPandSellPdiff1000():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select ir_policy_db.Apps_table.App_Id, ir_policy_db.Apps_table.App_Name, ir_policy_db.Apps_table.Rating from ir_policy_db.Apps_table")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('rating.html', userDetails=userDetails)

@app.route('/AvgPriOBikeIneveryCities')
def AvgPriOBikeIneveryCities():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select ir_policy_db.Apps_table.App_Id, ir_policy_db.Apps_table.App_Name, ir_policy_db.Apps_table.Score from ir_policy_db.Apps_table")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('privacyscore.html', userDetails=userDetails)
    
@app.route('/Dangerous')
def Dangerous():
    print("hhhh")
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select ir_policy_db.Apps_table.App_Id, ir_policy_db.Apps_table.App_Name, ir_policy_db.Apps_table.Score from ir_policy_db.Apps_table where ir_policy_db.Apps_table.Score>4")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('dangerous.html', userDetails=userDetails)

@app.route('/safe')
def safe():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select ir_policy_db.Apps_table.App_Id, ir_policy_db.Apps_table.App_Name, ir_policy_db.Apps_table.Score from ir_policy_db.Apps_table where ir_policy_db.Apps_table.Score<4")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('safe.html', userDetails=userDetails)

@app.route("/bottt")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get("msg")
    response = chatBot.generate_ans_chatbot(user_text)
    return str(response)
if __name__=='__main__':
    app.run(debug=True)
    
