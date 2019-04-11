from mysql import connector
from json import loads
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

def intro(type,companies=[]):
    if companies==[]:
        sql = "SELECT Product_ID,Product_Name,MRP,Company FROM products WHERE Type=%s"
    else:
        sql = "SELECT Product_ID,Product_Name,MRP,Company FROM products WHERE Type=%s AND Company in {}".format(companies)
        sql = sql.replace("[",'(')
        sql = sql.replace("]",')')
        print(sql)
    val=(type,)
    A = select(sql,val)
    desc = []
    for i in A:
        desc.append({'id':i[0],'name':i[1],'MRP':i[2],'company':i[3]})
    return desc

def sel_item(name):
    sql = "SELECT * FROM products WHERE Product_Name = %s"
    val=(name,)
    A=select(sql,val)
    print(A)
    dic={}
    spec = A[0][4]
    spec=spec.split(',')
    
    

    if len(A)==1:
        dic = {'id':A[0][0],'name':A[0][1],'MRP':A[0][2],'company':A[0][3],'specs':spec,'desc':A[0][5],'type':A[0][6]}
    return dic

def distinct_companies(type):
    sql = "SELECT DISTINCT Company FROM products WHERE Type=%s"
    val=(type,)
    A = select(sql,val)
    comp = []
    for i in A:
        comp.append(i[0])
    return comp


    