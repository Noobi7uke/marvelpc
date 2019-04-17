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

def get_rig(request):
    user = str(request.user)
    dic = {'Processor':None,'Motherboard':None,'RAM':None,'Storage':None,'Graphics':None,'Cabinet':None}
    user_id = select("SELECT Customer_ID FROM Customer WHERE Name = %s",(user,))[0][0]
    sql = "SELECT P.Product_ID,P.Company,P.Product_Name,P.Types,P.Price  FROM rig R JOIN Orders O ON O.Rig_ID = R.Rig_ID JOIN Inventory I ON O.Inventory_ID = I.Inventory_ID JOIN Products P ON I.Product_ID = P.Product_ID WHERE R.Customer = %s "
    r_set = select(sql,(user_id,))
    total = 0
    for q in r_set:
        dic[q[3]] = {'P_ID':q[0],'P_Company':q[1],'P_Name':q[2],'P_Price':q[4]}
        total += q[4]
    dic.update({'total':total})
    
    return dic

def change(user,type,inven_id):
    user_id = select("SELECT Customer_ID FROM Customer WHERE Name = %s",(user,))[0][0]


    