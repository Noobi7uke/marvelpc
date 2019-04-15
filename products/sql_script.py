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
        sql = "SELECT Product_ID,Product_Name,Price,Company FROM products WHERE Types=%s"
    else:
        sql = "SELECT Product_ID,Product_Name,Price,Company FROM products WHERE Types=%s AND Company in {}".format(companies)
        sql = sql.replace("[",'(')
        sql = sql.replace("]",')')
        print(sql)
    val=(type,)
    A = select(sql,val)
    desc = []
    for i in A:
        desc.append({'id':i[0],'name':i[1],'Price':i[2],'company':i[3]})
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
        dic = {'id':A[0][0],'name':A[0][2],'Price':A[0][6],'company':A[0][1],'specs':spec,'desc':A[0][5],'type':A[0][3]}
    return dic

def add_to_cart(user,inven_id):
    sql = "SELECT Cart_ID FROM Customer JOIN Cart ON Customer.Customer_ID=Cart.Customer WHERE Customer.Name = %s"
    val=(user,)
    cart = select(sql,val)
    if len(cart)==0:
        user_id = select("SELECT Customer_ID FROM Customer WHERE Name = %s",(user,))[0][0]
        sql = "INSERT INTO Cart (Customer) VALUE (%s ) "
        val=(user_id)
        insert_one(sql,val)
        print("Entered....")
        add_to_cart(user,inven_id)
    else:
        cart_id = cart[0][0]
        check = select("SELECT * FROM Orders WHERE Inventory_ID= %s AND Cart_ID= %s",(inven_id,cart_id))
        if len(check)==0:
            sql = "INSERT INTO orders (Inventory_ID,Cart_ID) VALUE (%s, %s)"
            val = (inven_id,cart_id)
        # test = select("SELECT ")
            try:
                insert_one(sql,val)   
                # print("inserted to cart")
                msg = "Inserted to cart"
            except:               
                # print("ERROR")
                msg = "Error in Inserting to Cart"
        else:
            msg = "Already in Cart"
        
    return msg




def add_to_rig(user,inven_id):
    sql = "SELECT R.Rig_ID FROM Rig R JOIN Customer C ON R.Customer=C.Customer_ID WHERE C.Name = %s "
    val = (user,)        
    temp = select(sql,val)
    if  len(temp)==0:
        sql = "INSERT INTO Rig (Customer) VALUE ((SELECT Customer_ID FROM Customer WHERE Name =%s ))"
        val = (user,)
        insert_one(sql,val)
        add_to_rig(user,inven_id)
    else:
        rig_id = temp[0][0]
        sql = "INSERT INTO orders (Inventory_ID,Rig_ID) VALUE (%s,%s)"
        val = (inven_id,rig_id)
        try:
            insert_one(sql,val)
            print("inserted to rig")
        except:
            print("ERROR")
    


def get_seller(pro_id):
    sql = "SELECT S.Seller_ID,S.Name,S.City,S.State,S.Star,I.Inventory_ID FROM Seller S NATURAL JOIN Inventory I WHERE I.Product_ID = %s AND I.Pieces > 0"
    val = (pro_id,)
    temp = select(sql,val)
    sellers = []
    for i in temp:
        dic = {}
        dic['Seller_ID'] = i[0]
        dic['Seller_Name'] = i[1]
        dic['Seller_City'] = i[2]
        dic['Seller_State'] = i[3]
        dic['Seller_Star'] = i[4]
        dic['Inventory_ID'] = i[5]
        sellers.append(dic)
    return sellers





def distinct_companies(type):
    sql = "SELECT DISTINCT Company FROM products WHERE Types=%s"
    val=(type,)
    A = select(sql,val)
    comp = []
    for i in A:
        comp.append(i[0])
    return comp


    