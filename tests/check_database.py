import sqlite3

conn = sqlite3.connect("database/resume_analyzer.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM candidates")
print("Total Candidates:", cursor.fetchone()[0])

cursor.execute("SELECT * FROM candidates")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
