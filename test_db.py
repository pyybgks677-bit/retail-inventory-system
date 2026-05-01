from db_config import get_db_connection

try:
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()

    print("Connected to MySQL successfully!")
    print("Database: inventory_db")
    print("Tables found:")

    for table in tables:
        print("-", table[0])

    cursor.close()
    db.close()

except Exception as e:
    print("Connection failed:", e)