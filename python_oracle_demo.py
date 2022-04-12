from datetime import datetime
import cx_Oracle

# Connect to oracle database instance
connection = cx_Oracle.connect(
    user = "test",
    password = "test",
    dsn = "localhost/orcl"
)


print("Oracle database conencted successfully")

cursor = connection.cursor()
# Read query
workers = cursor.execute('select * from worker')

for row in workers:
    print(row)


rowToBeInserted = [(9, "Anil", "Kumar", 3000000, datetime.now(), "Developer")]
# insert this row
cursor.executemany("Insert into worker (worker_id, first_name, last_name, salary, joining_date, department) values(:1, :2, :3, :4, :5, :6)", rowToBeInserted)

print("Rows inserted: ", cursor.rowcount)

connection.commit()