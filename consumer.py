import mysql.connector
from datetime import datetime
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
    print("8 exit")
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
        for i in result:
            print(i)
    elif(ch==3):
        print("Selected delete a consumer")
        consumerid = input("Enter the consumer id to delete: ")
        sql = "DELETE FROM `consumer` WHERE `consumerid` = "+consumerid
        mycursor.execute(sql)
        mydb.commit()
        print("deleted")
    elif(ch==4):
        print("Selected update a consumer")
        print("Update Consumer selected")
        consumerid = input("Enter the consumer ie: ")
        consumerName = input("Enter the consumer name to update: ")
        consumerAddress = input("Enter the consumer address to update: ")
        consumerPhone = input("Enter the consumer phone to update: ")
        consumerEmail = input("Enter the consumer email id to update: ")
        
        sql = "UPDATE `consumer` SET `name`='"+consumerName+"',`address`='"+consumerAddress+"',`phone`='"+consumerPhone+"',`email`='"+consumerEmail+"' WHERE `consumerid` = "+consumerid
        mycursor.execute(sql)
        mydb.commit()
        print("Data updated successfully")
    elif(ch==5):
        print("Selected viewall consumer")
        print("View All Consumer selected")
        sql = "SELECT `consumerid`, `name`, `address`, `phone`, `email` FROM `consumer` "
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(ch==6):
        print("Generate Bill selected")
        consumerCode = input("Enter the consumer code: ")
        sql = "SELECT `id` FROM `consumer` WHERE `consumerid` = "+consumerCode
        mycursor.execute(sql)
        result = mycursor.fetchone()
        consumerId = result[0]
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        currentMonth = str(currentMonth)
        currentYear = str(currentYear)
        sql = "select SUM(`unit`) from usages where month(date) = '"+currentMonth+"' AND year(date) = '"+currentYear+"' AND `consumerid` ="+str(consumerId)
        mycursor.execute(sql)
        result = mycursor.fetchone()
        sumOfUnit = result[0]
        print("Total Unit used : ",sumOfUnit)
        totalAmount = int(sumOfUnit)*5
        print("Total amount: ",totalAmount)
        sql = "INSERT INTO `bill`(`consumerid`, `month`, `year`, `bill`, `paidstatus`, `date`, `totalunits`) VALUES (%s,%s,%s,%s,%s,now(),%s)"
        data = (consumerId,currentMonth,currentYear,totalAmount,'0',sumOfUnit)
        mycursor.execute(sql,data)
        mydb.commit()
        print("Bill inserted successfully.")
        
    elif(ch==7): 
        print("Selected view all")
    elif(ch==8):
        break