import mysql.connector
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
         print("Selected search a consumer")
    elif(ch==3):
        print("Selected delete a consumer")
    elif(ch==4):
        print("Selected update a consumer")
    elif(ch==5):
        print("Selected viewall consumer")
    elif(ch==6):
        print("Selected generate bill")
    elif(ch==7):
        print("Selected view all")
    elif(ch==8):
        break