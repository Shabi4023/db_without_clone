import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    username = 'root',
    password = 'Rp20ee406',
    database = 'student'
)

print(db)

query = 'INSERT INTO mydb (name, age) VALUES (%s, %s)'
data = [
    ('Sam', 'Developer'),
    ('Bushra', 'Designer'),
    ('Rayan', 'Engineer')
]

cursor = db.cursor()

cursor.executemany(query, data)

db.commit()

print(cursor.rowcount, 'records inserted')

queryCount = 'SELECT COUNT(*) FROM mydb'

cursor.execute(queryCount)
result = cursor.fetchone()
print(result)