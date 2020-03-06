import sqlite3

con = sqlite3.connect("test.db")
print("Database opened successfully")

con.execute('''UPDATE Login set password = 12333444444 where  is ''')
con.commit()
cursor = con.execute('''SELECT Name, password FROM Login''')
for row in cursor:
  print(f"updated password is : {row[1]}")
cursor = con.execute('''select Name, password from Login''')
for row in cursor:
  print(f" name : {row[0]}")
  print(f" password : {row[1]}")

print("closing database")
con.close() #closing database connection
