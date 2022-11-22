import mysql.connector
from datetime import datetime
import random
from tabulate import tabulate
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='ksebdb')
except mysql.connector.Error as e:
    print ("db connection error",e)
mycursor=mydb.cursor()
while True:
    print("\nSelect an option")
    print("1 Add a consumer")
    print("2 Search a consumer")
    print("3 Delete a consumer")
    print("4 Update a consumer")
    print("5 view all consumer")
    print("6 Generate bill")
    print("7 View bill")
    print("8 Top two high bill")
    print("9 exit")
    ch=int(input("Select an option  : \n"))
    if (ch==1):
        consumerid=input("Enter the consumer id")
        name=input("Enter the consumer name")
        address=input("Enter the consumer address")
        phno=input("Enter the phone number")
        email=input("Enter the email")
        try:
            sql='INSERT INTO `consumer`(`consumerid`, `name`, `address`, `phone`, `email`) VALUES(%s,%s,%s,%s,%s)'
            data=(consumerid,name,address,phno,email)
            mycursor.execute(sql,data)
            mydb.commit()        
            print("inserted successfully")
        except mysql.connector.Error as e:
            print("db error",e)
        
    elif(ch==2):
        print("Search Consumer selected")
        sdata = input("Enter the Consumer Code/Name/Phone to search: ")
        try:
            sql = "SELECT `consumerid`, `name`, `address`, `phone`, `email` FROM `consumer` WHERE `consumerid` ='"+sdata+"'  OR `name`='"+sdata+"' OR `phone` ='"+sdata+"' "
            mycursor.execute(sql)
            result = mycursor.fetchall()
        except mysql.connector.Error as e:
            print("error",e)
        print(tabulate(result,headers=['consumerid','name','address','phone','email'],tablefmt = "psql"))
    elif(ch==3):
        print("Selected delete a consumer")
        consumerid = input("Enter the consumer id to delete: ")
        try:
            sql = "DELETE FROM `consumer` WHERE `consumerid` = "+consumerid
            mycursor.execute(sql)
            mydb.commit()
            print("deleted")
        except mysql.connector.Error as e:
            print(e)
    elif(ch==4):
        print("Selected update a consumer")
        print("Update Consumer selected")
        consumerid = input("Enter the consumer ie: ")
        consumerName = input("Enter the consumer name to update: ")
        consumerAddress = input("Enter the consumer address to update: ")
        consumerPhone = input("Enter the consumer phone to update: ")
        consumerEmail = input("Enter the consumer email id to update: ")
        try:
            sql = "UPDATE `consumer` SET `name`='"+consumerName+"',`address`='"+consumerAddress+"',`phone`='"+consumerPhone+"',`email`='"+consumerEmail+"' WHERE `consumerid` = "+consumerid
            mycursor.execute(sql)
            mydb.commit()
            print("Data updated successfully")
        except mysql.connector.Error as e:
            print(e)
    elif(ch==5):
        print("Selected viewall consumer")
        try:
            sql = "SELECT `consumerid`, `name`, `address`, `phone`, `email` FROM `consumer` "
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print(tabulate(result,headers=['consumerid','name','address','phone','email'],tablefmt = "psql"))
        except mysql.connector.Error as e:
            print(e)
    elif(ch==6):
        print("Generate Bill selected")
        cMonth = datetime.now().month
        cYear = datetime.now().year
        cMonth = str(cMonth)
        cYear = str(cYear)
        try:
            sql = "DELETE FROM `bill` WHERE `month` ='"+cMonth+"'  AND `year` ='"+cYear+"'"
            mycursor.execute(sql)
            mydb.commit()
            print("Previous data deleted.")
            sql = "SELECT `id` FROM `consumer`"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            for i in result:
                conId = str(i[0])
                print(conId)
                sql = "select SUM(`unit`) from usages where month(date) = '"+cMonth+"' AND year(date) = '"+cYear+"' AND `consumerid` ="+conId
                mycursor.execute(sql)
                result = mycursor.fetchone()
                sumOfUnit = result[0]
                totalAmount = int(sumOfUnit)*5
                invoice = random.randint(10000,100000)
                sql = "INSERT INTO `bill`(`consumerid`, `month`, `year`, `bill`, `paidstatus`, `date`, `totalunits`, `duedate`, `invoice`) VALUES (%s,%s,%s,%s,%s,now(),%s,now()+ interval 14 day,%s)"
                data = (conId,cMonth,cYear,totalAmount,'0',sumOfUnit,invoice)
                mycursor.execute(sql,data)
                mydb.commit()
                print("Data inserted successfully")
        except mysql.connector.Error as e:
            print(e)         
    elif(ch==7): 
        print("Selected view all")
        try:
            sql = "SELECT b.`consumerid`, b.`month`, b.`year`, b.`bill`, b.`paidstatus`, b.`date`, b.`totalunits`, b.`duedate`, b.`invoice`, c.`name`, c.`address` FROM bill b JOIN consumer c ON b.consumerid=c.id"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print(tabulate(result,headers=['consumerid','month','year','bill','paidstatus','date','totalunits','duedate','invoice','name','address'],tablefmt = "psql"))
        except mysql.connector.Error as e:
            print(e)   
    elif(ch==8):
        print("Displaying top two high bill consumer details")
        try:
            sql = "SELECT c.`name`,c.`address`,b.`totalunits`,b.`bill` FROM bill b JOIN consumer c ON b.consumerid = c.id GROUP BY `bill` ORDER BY `bill` DESC LIMIT 0,2"
            #sql="SELECT `bill` FROM bill GROUP BY `bill` ORDER BY `bill` DESC LIMIT 0,2"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print(tabulate(result,headers=['name','address','consumerid','totalunits','bill'],tablefmt = "psql"))
        except mysql.connector.Error as e:
            print(e)
    elif(ch==9):
        break