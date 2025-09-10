import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="attendance_db")
cursor = conn.cursor()

sql = "INSERT INTO attendance (name, timestamp) VALUES (%s, NOW())"
cursor.execute(sql, (recognized_person,))
conn.commit()
conn.close()
