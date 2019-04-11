from mysql import connector

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

def intro(type):
    sql = "SELECT Product_ID,Product_Name,MRP,Company FROM products WHERE Type=%s"
    val=(type,)
    A = select(sql,val)
    desc = []
    for i in A:
        desc.append({'id':i[0],'name':i[1],'MRP':i[2],'company':i[3]})
    return desc



def distinct_companies(type):
    sql = "SELECT DISTINCT Company FROM products WHERE Type=%s"
    val=(type,)
    A = select(sql,val)
    comp = []
    for i in A:
        comp.append(i[0])
    return comp


    