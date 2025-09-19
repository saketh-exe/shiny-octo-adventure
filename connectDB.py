def connectDB():
    import mysql.connector as mysql
    DB = mysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="test"
    )
    cursor = DB.cursor()
    print("Database connected successfully!")
    return DB,cursor


