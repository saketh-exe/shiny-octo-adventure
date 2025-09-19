import mysql.connector as mysql

# Connect to MySQL
mydb = mysql.connect(
    host="localhost",   # server (use IP if remote)
    user="root",        # your MySQL username
    password="1234",    # your MySQL password
    database="test"     # connects directly to 'test' DB
)

# Create a cursor
mycursor = mydb.cursor()
        
# Run a query
mycursor.execute("Show Tables")

# Print results
for table in mycursor: # type: ignore
    print(table)
