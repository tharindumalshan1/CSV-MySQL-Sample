import pandas as pandas
import mysql.connector as mysql
from mysql.connector import Error

# Import CSV
data = pandas.read_csv(r'/home/tharindu/Docs/Python/People.csv')
df = pandas.DataFrame(data, columns=['Name', 'Country', 'Age'])
print(df)

# create database
# try:
#     conn = msql.connect(host='localhost', user='root',
#                         password='sql@123')
#     if conn.is_connected():
#         cursor = conn.cursor()
#         cursor.execute("CREATE DATABASE testDB")
#         print("testDB database is created")
# except Error as e:
#     print("Error while connecting to MySQL", e)

try:
    connection = mysql.connect(host='localhost', database='testDB', user='root',
                               password='root')
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS people;')
        print('Creating table....')
        cursor.execute("CREATE TABLE people (Name nvarchar(50), Country nvarchar(50), Age nvarchar(20))")
        print("people table is created....")
        for i, row in data.iterrows():
            sql = "INSERT INTO testDB.people VALUES (%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
        connection.commit()

except Error as e:
    print("Error while connecting to MySQL", e)
