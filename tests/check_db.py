from database import Database

db = Database()

db.cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
""")

for table in db.cursor.fetchall():
    print(table["name"])

db.close()
