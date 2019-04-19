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
    sql = "SELECT P.Product_ID,P.Company,P.Product_Name,P.Types,P.Price,I.Inventory_ID  FROM rig R JOIN Orders O ON O.Rig_ID = R.Rig_ID JOIN Inventory I ON O.Inventory_ID = I.Inventory_ID JOIN Products P ON I.Product_ID = P.Product_ID WHERE R.Customer = %s "
    r_set = select(sql,(user_id,))
    total = 0
    for q in r_set:
        dic[q[3]] = {'P_ID':q[0],'P_Company':q[1],'P_Name':q[2],'P_Price':q[4],'Inven_ID':q[5]}
        total += q[4]
    rig_id = select("SELECT Rig_ID FROM Rig JOIN Customer ON Customer.Customer_ID = Rig.Customer WHERE Customer.Name = %s",(str(request.user),))
    dic.update({'total':total,'Rig_ID':rig_id[0][0]})
    
    return dic

def change(user,type,inven_id):
    user_id = select("SELECT Customer_ID FROM Customer WHERE Name = %s",(user,))[0][0]
    pass


def remove(rig,inven):
    sql = "DELETE FROM Orders WHERE Rig_ID = %s AND Inventory_ID = %s"
    val = (rig,inven)
    insert_one(sql,val)
    print(val)


def show(request,Type):
    sql = "SELECT P.Product_ID,P.Product_Name,P.Company,S.Name,S.City,S.State,I.Inventory_ID FROM Products P NATURAL JOIN Inventory I NATURAL JOIN Seller S WHERE P.Types = %s "
    val = (Type,)
    q_tup = select(sql,val)
    print(q_tup)
    dic = {}
    for i in q_tup:
        dic[i[0]] = {'Product_Name':i[1],'Product_Company':i[2],'Sellers':[]}
    for i in q_tup:
        dic[i[0]]['Sellers'].append({'Seller_Name':i[3],'Seller_City':i[4],'Seller_State':i[5],'Inven_ID':i[6]})
    result = []
    for i in dic:
        temp = {'Product_ID':i}
        temp.update(dic[i])
        result.append(temp)
        
    return result


def check(request,Type):
    sql = "SELECT count(*) FROM Customer C JOIN Rig R ON R.Customer = C.Customer_ID JOIN Orders O ON O.Rig_ID = R.Rig_ID JOIN Inventory I ON I.Inventory_ID = O.Inventory_ID JOIN Products P ON P.Product_ID=I.Product_ID WHERE C.Name = %s AND P.Types = %s"
    val = (str(request.user),Type)
    return select(sql,val)[0][0] == 0
        

def add(request):
    sql = "INSERT INTO Orders (Inventory_ID,Rig_ID) VALUE (%s , (SELECT Rig_ID FROM Rig R JOIN Customer C ON C.Customer_ID = R.Customer WHERE C.Name = %s) )"
    val = (request.POST['inven'],str(request.user))
    insert_one(sql,val)




    