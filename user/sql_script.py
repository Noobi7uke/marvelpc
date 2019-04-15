from mysql import connector
from django.db.utils import IntegrityError
from django.contrib.auth.models import User


# def initialize(request=None):
#     db =connector.connect(user="marvel",passwd="marvel123",host="localhost",database = "marvel")
#     return db

def insert_one(sql,val):
    db =connector.connect(user="marvel",passwd="marvel123",host="localhost",database = "marvel")
    cur = db.cursor()
    cur.execute(sql,val)
    db.commit()
    db.close()



def save_profile(id,img_src):
    sql = "UPDATE auth_user SET profile_pic = %s WHERE id = %s"
    val = (img_src,id)
    insert_one(sql,val)

def  select(sql,val):
    db =connector.connect(user="marvel",passwd="marvel123",host="localhost",database = "marvel")
    cur = db.cursor()
    cur.execute(sql,val)
    D = cur.fetchall()
    db.close()
    return D
    
def check_for_user(name,email,errors):
    sql = "SELECT username,email FROM auth_user WHERE username = %s OR email = %s "
    val = (name,email)
    q_result = select(sql,val)
    for i in q_result:
        if i[0] == name:
            errors['username']=True
            errors['err']=True
        if i[1] == email:
            errors['email']=True
            errors['err']=True
    return errors

def check_for_customer(name,email,phone,errors):
    sql = "SELECT Name,Email,Phone FROM Customer WHERE Name = %s OR Email = %s OR Phone = %s;"
    val = (name,email,phone)
    q_result = select(sql,val)
    for i in q_result:
        if i[0] == name:
            errors['username']=True
            errors['err']=True
        if i[1] == email:
            errors['email']=True
            errors['err']=True
        if i[2] == phone:
            errors['phone']=True
            errors['err']=True
    return errors

def insert_to_customer(name,email,address,city,state,pincode,phone,bitrth_date,id):
    sql = "INSERT INTO customer (Customer_ID,Name,Email,Address,City,State,Pincode,Phone,birth_date) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s) ;"
    val = (id,name,email,address,city,state,pincode,phone,bitrth_date)
    insert_one(sql,val)
    print("Success")
    

def get_cart(user):

    cart = select("SELECT Cart_ID FROM Cart Ca JOIN Customer Cu ON Ca.Customer = Cu.Customer_ID WHERE Cu.Name = %s",(user,))
    if len(cart)==0:
        return []
    else:
        cart_id = cart[0][0]
        sql = "SELECT P.Product_ID,P.Product_Name,P.Company,P.Price,S.Name,S.City,S.State,P.Types FROM Orders O JOIN Inventory I ON O.Inventory_ID = I.Inventory_ID JOIN Seller S ON S.Seller_ID = I.Seller_ID JOIN Products P ON P.Product_ID = I.Product_ID WHERE O.Cart_ID = %s"
        val=(cart_id,)
        tup = select(sql,val)
        lis = []
        for temp in tup:
            dic = {}
            dic['ID'] = temp[0]
            dic['Name'] = temp[1]
            dic['Company'] = temp[2]
            dic['Price'] = temp[3]
            dic['Seller_ID'] = temp[4]
            dic['Seller_City'] = temp[5]
            dic['Seller_State'] = temp[6]
            dic['Product_Types'] = temp[7]
            lis.append(dic)
        return lis



def get_rig(user):

    rig = select("SELECT Rig_ID FROM Rig R JOIN Customer C ON C.Customer_ID=R.Customer WHERE C.Name = %s",(user,))
    if len(rig) == 0:
        return []
    else:
        rig_id = rig[0][0]
        sql = "SELECT P.Product_ID,P.Product_Name,P.Company,P.Price,S.Name,S.City,S.State FROM Orders O JOIN Inventory I ON O.Inventory_ID = I.Inventory_ID JOIN Seller S ON S.Seller_ID = I.Seller_ID JOIN Products P ON P.Product_ID = I.Product_ID WHERE O.Rig_ID = %s"
        val=(rig_id,)
        tup = select(sql,val)
        lis = []
        for temp in tup:
            dic = {}
            dic['ID'] = temp[0]
            dic['Name'] = temp[1]
            dic['Company'] = temp[2]
            dic['Price'] = temp[3]
            dic['Seller_ID'] = temp[4]
            dic['Seller_City'] = temp[5]
            dic['Seller_State'] = temp[6]
            lis.append(dic)
        return lis
