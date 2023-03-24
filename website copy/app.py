from urllib import request
from flask import Flask, render_template, request, redirect,url_for
from flask_mysqldb import MySQL
import mysql.connector

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
def summary(policy):

    return "this is very good policy"
@app.route('/process_input', methods=['POST'])
def process_input():
    input_text = request.form['input_text']
    # Process the input here
    print(input_text)
    summary1=summary(input_text)
    return redirect(url_for('newpolicy', summary1=summary1))
@app.route('/newpolicy')
def newpolicy():
    summary1 = request.args.get('summary1')
    print(summary1)
    return render_template('newpolicy.html', string_var=summary1)


@app.route('/input')
def input():
    return render_template('NotFound.html')

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


@app.route('/search')
def search():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("SELECT * FROM product_table")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('search.html', userDetails=userDetails)

@app.route('/users')
def users():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select DISTINCT(seller_id) from (select seller_id from product_table) AS temp1 where seller_id NOT IN(SELECT seller_id FROM (select* from(select DISTINCT(seller_id)from product_table) AS temp2 cross join (select type_id from type_table) AS temp3)AS temp4 WHERE (seller_id,type_id) NOT IN( select seller_id,type_id from product_table));")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('users.html', userDetails=userDetails)

@app.route('/homepage')

def Homepage():
    # cur=mysql.connection.cursor()
    # resultVAlue=cur.execute("select DISTINCT(seller_id) from (select seller_id from product_table) AS temp1 where seller_id NOT IN(SELECT seller_id FROM (select* from(select DISTINCT(seller_id)from product_table) AS temp2 cross join (select type_id from type_table) AS temp3)AS temp4 WHERE (seller_id,type_id) NOT IN( select seller_id,type_id from product_table));")
    # if resultVAlue>0:
    #     userDetails=cur.fetchall()
    return render_template('homepage.html')

@app.route('/EmbeddedCodes')
def EmbeddedCodes():

    return render_template('EmbeddedCodes.html')  

@app.route('/sellerSALLTypeProducts')
def sellerSALLTypeProducts():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select DISTINCT(seller_id) from (select seller_id from product_table) AS temp1 where seller_id NOT IN(SELECT seller_id FROM (select* from(select DISTINCT(seller_id)from product_table) AS temp2 cross join (select type_id from type_table) AS temp3)AS temp4 WHERE (seller_id,type_id) NOT IN( select seller_id,type_id from product_table));")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('sellerSALLTypeProducts.html', userDetails=userDetails)

@app.route('/AskPandSellPdiff1000')   
def AskPandSellPdiff1000():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select temp1.product_id as ID, temp1.Askprice, temp1.SoldPrice from(select P.product_id,P.price as AskPrice,S.price as SoldPrice from product_table P join sold_product S  on P.product_id = S.product_id where  P.price-S.price<=1000)AS temp1; ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('AskPandSellPdiff1000.html', userDetails=userDetails)

@app.route('/AvgPriOBikeIneveryCities')
def AvgPriOBikeIneveryCities():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select A.city_name,AVG(Price) as AvgPrice, Count(*) as Number from (select product_id,price,city_code from  product_table  where type_id=( select type_id from type_table where name='bike') ) as P join area_table A  on P.city_code=A.area_id Group By A.city_name having  AVG(Price)>1000 Order by A.city_name ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('AvgPriOBikeIneveryCities.html', userDetails=userDetails)

@app.route('/ThoseWhoMEssegedMoreThan1')
def ThoseWhoMEssegedMoreThan1():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select U.user_id, Count(*) as NumberofMsgs from user_details U join chat_table C on U.user_id=C.sender_id Group by  C.sender_id having  Count(distinct receiver_id)>1 order by C.sender_id ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('ThoseWhoMEssegedMoreThan1.html', userDetails=userDetails)

@app.route('/bajajBikeInkarnataka')
def bajajBikeInkarnataka():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select P.product_id,A.city_name as City, P.price as Price, P.seller_id as Seller_id, D.short_description as Description from product_table P join (select area_table.area_id,area_table.city_name from area_table  where area_table.state_name='Karnataka') as A on P.city_code=A.area_id join (select type_table.type_id from type_table where name='bike') as T on T.type_id=P.type_id join (select product_id,short_description from description_table where short_description LIKE 'bajaj%' )as D on D.product_id=P.product_id where NOT EXISTS( 	select product_id     from sold_product     where P.product_id=sold_product.product_id limit 1 ) ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('bajajBikeInkarnataka.html', userDetails=userDetails)

@app.route('/soldAmountAndBoughtAmount')
def soldAmountAndBoughtAmount():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select temp.user_id,temp.Selling_amount,IFNULL(Bought_amount, 0 ) as Bought_amount FROM ( select P.seller_id as user_id, SUM(P.price) as Selling_Amount, SUM(S.price) as Bought_amount from product_table P left join sold_product S on P.product_id=S.product_id Group by  P.seller_id Order by P.seller_id ) as temp ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('soldAmountAndBoughtAmount.html', userDetails=userDetails)


@app.route('/ChatOfUSer9And1ondate')
def ChatOfUSer9And1ondate():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select sender,receiver,chat,time from( select U.customer_name as sender, U1.customer_name as receiver, C.chat, C.time from user_details U join (select sender_id,chat,time,receiver_id,date from chat_table where sender_id=1 and receiver_id=9 and date='2020-05-03') as C on U.user_id = C.sender_id join user_details U1 on U1.user_id = C.receiver_id union all select U.customer_name as sender, U1.customer_name as receiver, C.chat, C.time from user_details U join (select sender_id,chat,time,receiver_id,date from chat_table where sender_id=9 and receiver_id=1 and date='2020-05-03') as C on U.user_id = C.sender_id join user_details U1 on U1.user_id = C.receiver_id ) as Temp Order by Temp.time ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('ChatOfUSer9And1ondate.html', userDetails=userDetails)  

@app.route('/groupingUSerByage')
def groupingUSerByage():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select U.age,count(*) as Number from user_details U group by U.age order by U.age ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('groupingUSerByage.html', userDetails=userDetails)

@app.route('/groupbyMessageSize')
def groupbyMessageSize():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select length(chat),count(*) as length  from chat_table group by length(chat) order by length(chat) ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('groupbyMessageSize.html', userDetails=userDetails)

@app.route('/ThoseWhoAreSellerAndBuyer')
def ThoseWhoAreSellerAndBuyer():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select U.user_id, U.customer_name, U.age from user_details U  where EXISTS( 	select P.seller_id     from product_table P     where U.user_id=P.seller_id limit 1)  and EXISTS(  select S.bought_id  from sold_product S  where S.bought_id=U.user_id limit 1 	) order by user_id ")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('ThoseWhoAreSellerAndBuyer.html', userDetails=userDetails)

@app.route('/bike')
def bike():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("SELECT * FROM product_table where type_id=1")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('bike.html', userDetails=userDetails)

@app.route('/car')
def car():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("SELECT * FROM product_table where type_id=2")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('bike.html', userDetails=userDetails)

@app.route('/electronics')
def electronics():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("SELECT * FROM product_table where type_id=4")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('bike.html', userDetails=userDetails)

@app.route('/books')
def books():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("SELECT * FROM product_table where type_id=5")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('bike.html', userDetails=userDetails)

@app.route('/others')
def others():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("SELECT * FROM product_table where type_id=3")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('bike.html', userDetails=userDetails)
@app.route('/avgPriceOfDTypeOfPRoduct')
def avgPriceOfDTypeOfPRoduct():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select T.type_id,T.name,AVG(P.price),Count(*) from type_table T join product_table P on P.type_id=T.type_id group by T.type_id order by T.type_id")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('avgPriceOfDTypeOfPRoduct.html', userDetails=userDetails)
@app.route('/NoofMessagesEachCustomerSent')
def NoofMessagesEachCustomerSent():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("select U.user_id, U.customer_name, Count(*) from user_details U join chat_table C on C.sender_id = U.user_id Group by  U.user_id order by U.user_id")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('NoofMessagesEachCustomerSent.html', userDetails=userDetails)


@app.route('/kolkata')
def kolkata():
    cur=mysql.connection.cursor()
    resultVAlue=cur.execute("SELECT * FROM product_table where type_id=3")
    if resultVAlue>0:
        userDetails=cur.fetchall()
        return render_template('kolkata.html', userDetails=userDetails)


if __name__=='__main__':
    app.run(debug=True)
    
