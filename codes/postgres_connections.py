import psycopg2
import os

"""PostgreSQL 데이터베이스에 연결합니다."""
db_host = "db_postgresql"
db_port = "5432"
db_name = "main_db"
db_user = "admin"
db_password = "admin123"

conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)
print("PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.")

with conn.cursor() as cursor  :
    # cursor.execute("insert INTO users_uuid_name (name)VALUES ('from code');")
    # cursor.execute("""UPDATE users_uuid_name set \
    #                 name = 'apdateName' \
    #                 Where id_name = '3b06cc78-f87d-4656-a8c1-69464de42df6';""")
    # cursor.execute("""DELETE FROM users_uuid_name \ WHERE id_name = '3b06cc78-f87d-4656-a8c1-69464de42df6';""")
    cursor.execute("SELECT name, id_name FROM users_uuid_name;")
    records = cursor.fetchall()
    for record in records:
        print(record)
        print(f'{record[0]} : {record[1]}')
conn.commit()