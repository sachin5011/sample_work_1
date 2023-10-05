import pyodbc

# DRIVER_NAME = "SQL SERVER"
# SERVER_NAME = "localhost"
# DATABASE_NAME = "workdb"

def createTable(connection):
    print('Creating table ')
    table_name = input("Enter table name : ")
    cursor = connection.cursor()
    cursor.execute(f"Create table {table_name} (id Integer, name text, phone text)")
    print(f"Table {table_name} created")
    connection.commit()
    connection.close()


def read(connection):
    print("read")
    table_name=input("Enter table name : ")
    cursor = connection.cursor()
    cursor.execute(f"select * from {table_name}")
    for row in cursor:
        print(row)
    connection.commit()
    connection.close()


def create(connection):
    print("create")
    id = int(input("Enter id : "))
    fname = input("Enter first name : ")
    lname = input("Enter last name : ")
    email = input("Enter Email : ")
    cursor = connection.cursor()
    cursor.execute(
        "insert into students(id,first_name,last_name,email) values(?,?,?,?);",
        (id, fname, lname, email)
    )
    print("data inserted....")
    connection.commit()
    connection.close()

def drop(connection):
     table_name = input("Enter table name : ")
     cursor = connection.cursor()
     cursor.execute(f"drop table {table_name}")
     connection.commit()
     connection.close()



# Connection_string = f"""
#         DRIVER={{{DRIVER_NAME}}};
#         SERVER={SERVER_NAME};
#         DATABASE={DATABASE_NAME};
#         Trust_connection=True;
#         uid="sa";
#         pwd="s";
# """

# connection = pyodbc.connect(Connection_string)
# print(connection)

connection = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=MLBSRL-110080;"
    "Database=demodb;"
    "Trusted_connection=yes;"
)
print(connection)
# create(connection)
# createTable(connection)
read(connection)
# drop(connection)



