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
    sql = "SELECT Name,Email,Phone FROM customer WHERE Name = %s OR Email = %s OR Phone = %s;"
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

def insert_to_customer(name,email,address,city,state,pincode,phone,id):
    sql = "INSERT INTO customer (Customer_ID,Name,Email,Address,City,State,Pincode,Phone) VALUE (%s,%s,%s,%s,%s,%s,%s,%s) ;"
    val = (id,name,email,address,city,state,pincode,phone)
    insert_one(sql,val)
    print("Success")
    

 