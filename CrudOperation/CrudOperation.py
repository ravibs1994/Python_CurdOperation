""" 
  * Author :Ravindra
  * Date   :20-11-2020
  * Time   :22:32
  * Package:CrudOperation
  * Statement:Study and perform CURD Operation
"""
import os

import mysql.connector
class CurdOperation:
  def __init__(self):
     """Constructor
      Mysql database connection Created
     """
     global mydb
     try:

        USER_NAME = os.environ.get('USER')
        PASSWORD= os.environ.get('password')
        print(USER_NAME,PASSWORD)
        mydb = mysql.connector.connect(
        host="localhost",
        user=USER_NAME,
        password=PASSWORD,
        database="mydatabase"
        )
        print("Connected Successfully",mydb)
     except Exception as e:
       print(e)
  def createTable(self):
    """Method Definition
       Create Table In Database
       :return
    """
    mycursor = mydb.cursor()
    try:
        mycursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(25), address VARCHAR(25))")
        print("Table Created Successfully")
    except Exception as e:
      print(e)
  def insertIntoTable(self):
    """Method Definition
       Insert records into Table In Database
       :return
    """
    mycursor=mydb.cursor()
    try:
      name = input("Enter Name that you want to insert into database ")
      address = input("Enetr Address of student")
      sql = "INSERT INTO students (name, address) VALUES (%s, %s)"
      val = (name,address )
      mycursor.execute(sql, val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
    except Exception as e:
      print(e)

  def updateRecords(self):
    """Method Definition
       Update Records into Table In Database
       :return
    """
    mycursor = mydb.cursor()
    try:
      idValue = int(input("enter the id for which record you want to update "))
      value1 = input(" Enter new value for name ")
      sql = "UPDATE students SET name  = %s WHERE id = %s"
      val = (value1 , idValue)
      mycursor.execute(sql, val)
      mydb.commit()
      print(mycursor.rowcount, "record(s) affected")
    except Exception as e:
      print(e)

  def deleteRecords(self):
    """Method Definition
       Delete Records from Table In Database
       :return
    """
    mycursor = mydb.cursor()
    try:
      #colName = input("enter where you want to delete from name or address or id")
      value1 = input(" Enter Name value you want to delete")
      sql = "DELETE FROM students WHERE name = %s"
      val = (value1, )
      mycursor.execute(sql, val)
      mydb.commit()
      print(mycursor.rowcount, "record(s) deleted")
    except Exception as e:
      print(e)

  def readRecords(self):
    """Method Definition
       Fetch Records From Table
    """
    mycursor = mydb.cursor()
    try:
      mycursor.execute("SELECT * FROM students")
      myresult = mycursor.fetchall()
      for x in myresult:
        print(x)
    except Exception as e:
        print(e)

if __name__ == '__main__':
  """Main Method 
     Class Object Created and Calling class Methods
  """
  object1=CurdOperation()
  while True:
    while True:
      try:
        choice = int(input(" Enter Your Choice 1=create Table, 2=Insert, 3=update,4=delete, 5=read "))
        break
      except Exception as e:
        print(e)
    if choice == 1:
      object1.createTable()
    elif choice == 2:
      object1.insertIntoTable()
    elif choice == 3:
      object1.readRecords()
      object1.updateRecords()
    elif choice == 4:
      object1.readRecords()
      object1.deleteRecords()
    elif choice == 5:
      object1.readRecords()
    else:
      print(" Envalid Choice")
    option = str(input(" Do you want to Continue... Y/N"))
    if 'Y' or 'y' == option:
      continue
    else:
      break











