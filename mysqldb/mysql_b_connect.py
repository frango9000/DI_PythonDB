import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="narf",
    passwd="narf",
    database="narf"

)

print(mydb)
