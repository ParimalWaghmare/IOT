import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

emp_id = int(input("Enter the Employee Id:"))
name = (input("Enter the Employee name"))
department = (input("Enter the Department"))
email = (input("Enter your email:"))
salary = int (input("Enter the salary:"))
doj = (input("Enter the Date of Joining"))

query = f"insert into employee values ({emp_id}, '{name}', '{department}','{email}' , {salary}, {doj} )"

cursor = connection.cursor()

cursor.execute(query)

connection.commit();

cursor.close()

connection.close()