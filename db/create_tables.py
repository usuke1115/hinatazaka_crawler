import sqlite3

conn = sqlite3.connect("db/url.db")

with open("db/scripts/init.sql", encoding="utf-8") as f:
    sql = f.read()

try:
    conn.executescript(sql)
    conn.commit()
    print("✅ blogs and images table have been created.")
except sqlite3.OperationalError as e:
    print("Tables already exists.")
finally:
    conn.close()
