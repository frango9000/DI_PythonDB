import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="narf",
    passwd="narf",
    database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE customers CASCADE")
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
