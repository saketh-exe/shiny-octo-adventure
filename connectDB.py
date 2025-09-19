
def connectDB():
    from dotenv import load_dotenv
    import mysql.connector as mysql
    import os
    load_dotenv()
    DB = mysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = DB.cursor()
    print("Database connected successfully!")
    return DB,cursor


