import mysql.connector
try:
    db=mysql.connector.connect(
        host="localhost",
        username="root",
        database="python_health_care",
        password="Gopi@123"
    )
    print("Successfully Connected Database")
    cursor=db.cursor()
    add_user_admin=""" 
    insert into users(username,password,role) values(%s,%s,%s)
    """
    values=("admin","admin@123","ADMIN")
    cursor.execute(add_user_admin,values)
    db.commit()
except mysql.connector.Error as err:
    print("Error in Connection My Sql",err)