from urllib import request
from flask import Flask, render_template, request, redirect,url_for
from flask_mysqldb import MySQL
import mysql.connector
import indexing as idxx
import torch 
from flask_caching import Cache

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
app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='7061'
app.config['MYSQL_DB']='ir_policy_db'

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='7061',
        database='ir_policy_db'
    )
    return conn
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
        userDetails=request.form
        result1=userDetails["App_Name"]
    # Pass the result to the next page
        return redirect(url_for('result', result=result1))

    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    App_Name = request.form['input_text1']
    Privacy_policy = chatBot.generate_ans_chatbot("write privacy policy of "+ App_Name)
    type_id = int(request.form['input_text3'])
    with mysql.connector.connect(
        host='localhost',
        user='root',
        password='7061',
        database='ir_policy_db'
    )as conn:
        cursor = conn.cursor()
        cursor.execute("select count(*) from apps_table")
        result = cursor.fetchall()
        App_id=result[0][0]+1
        
        summary1= summarize_text(Privacy_policy) 
        Rating=4
        Paid=0
        sql = "INSERT INTO apps_table (App_id, type_id, App_Name, Privacy_policy, Summary, Score, Rating, Paid) VALUES (%s,%s, %s,%s,%s, %s,%s,%s)"
        val = (App_id, type_id, App_Name, Privacy_policy, summary1, 0, Rating, Paid)
    
        
        cursor.execute(sql, val)
        conn.commit()   
        idxx.calculate_score()
        str2="SELECT score FROM apps_table WHERE app_name = ";
        str3=str2+"\'"+App_Name+"\';"
        val=(App_Name)
        cursor.execute(str3)
        result = cursor.fetchall()[0][0]
        cursor.close()
    res=[(App_Name,summary1,result)]
    return render_template('newpolicy.html', result=res)
@app.route('/newpolicy')
def newpolicy():
    summary1 = request.args.get('summary1')
    result=[]
    result.append((summary1,score))
    return render_template('newpolicy.html', result=result)


@app.route('/input')
def input():
    return render_template('NotFound.html')

@app.route('/recomendationInput', methods=['POST'])
def recomendationInput():
    App_Name = request.form['input_text1']
    recomendApp=rec.get_recommendations(App_Name)
    return render_template('recScreen.html', input=recomendApp)




@app.route('/recomendation')
def recomendation():
    return render_template('recomendation.html')
    
@app.route('/result')
def result():
    result1 = request.args.get('result')
    print("app name: ",result1)
    conn =get_db_connection()
    with mysql.connector.connect(
        host='localhost',
        user='root',
        password='7061',
        database='ir_policy_db'
    )as conn:
        mycursor = conn.cursor()
        str2="select ir_policy_db.Apps_table.App_Name, ir_policy_db.Apps_table.Summary, ir_policy_db.Apps_table.Score, ir_policy_db.Apps_table.Rating from ir_policy_db.Apps_table where ir_policy_db.Apps_table.App_Name = "
        str3=str2+"\'"+result1+"\';"
            # val=(app_name)
        mycursor.execute(str3)
        result = mycursor.fetchall()
        mycursor.close()
        print("app is:", result);
    if(len(result)==0):
       return redirect(url_for('input'))
    
    return render_template('result.html', result=result)





@app.route('/homepage')

def Homepage():
   
    return render_template('homepage.html')

@app.route('/AskPandSellPdiff1000')   
def AskPandSellPdiff1000():
    with mysql.connector.connect(
        host='localhost',
        user='root',
        password='7061',
        database='ir_policy_db'
    )as conn:

        cur=conn.cursor()
        resultVAlue=cur.execute("select ir_policy_db.Apps_table.App_Id, ir_policy_db.Apps_table.App_Name, ir_policy_db.Apps_table.Rating from ir_policy_db.Apps_table")
        userDetails=cur.fetchall()
        conn.close()
        return render_template('rating.html', userDetails=userDetails)

@app.route('/AvgPriOBikeIneveryCities')
def AvgPriOBikeIneveryCities():
    with mysql.connector.connect(
        host='localhost',
        user='root',
        password='7061',
        database='ir_policy_db'
    )as conn:
        cur=conn.cursor()
        resultVAlue=cur.execute("select ir_policy_db.Apps_table.App_Id, ir_policy_db.Apps_table.App_Name, ir_policy_db.Apps_table.Score from ir_policy_db.Apps_table")
        userDetails=cur.fetchall()
        conn.close()
        return render_template('privacyscore.html', userDetails=userDetails)
    
@app.route('/Dangerous')
def Dangerous():
    conn = get_db_connection()
    with mysql.connector.connect(
        host='localhost',
        user='root',
        password='7061',
        database='ir_policy_db'
    )as conn:
        cur=conn.cursor()
        resultVAlue=cur.execute("select ir_policy_db.Apps_table.App_Id, ir_policy_db.Apps_table.App_Name, ir_policy_db.Apps_table.Score from ir_policy_db.Apps_table where ir_policy_db.Apps_table.Score>4")
        userDetails=cur.fetchall()
        conn.close()
        return render_template('dangerous.html', userDetails=userDetails)
        

@app.route('/safe')
def safe():
    with mysql.connector.connect(
        host='localhost',
        user='root',
        password='7061',
        database='ir_policy_db'
    )as conn:
        cur=conn.cursor()
        resultVAlue=cur.execute("select ir_policy_db.Apps_table.App_Id, ir_policy_db.Apps_table.App_Name, ir_policy_db.Apps_table.Score from ir_policy_db.Apps_table where ir_policy_db.Apps_table.Score<4")
        userDetails=cur.fetchall()
        conn.close()
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
    
