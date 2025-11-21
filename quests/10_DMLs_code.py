import psycopg2


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





# # 문제 2 CREATE (INSERT) 기초
# # students 테이블에 다음 데이터를 INSERT 하시오.
# # id name age
# # 1 홍길동 23
# # 2 이영희 21
# # 3 박철수 26
with conn.cursor() as cursor  :
    cursor.execute("INSERT INTO students (name, age) VALUES ('홍길동', 23);")
    cursor.execute("INSERT INTO students (name, age) VALUES ('이영희', 21);")
    cursor.execute("INSERT INTO students (name, age) VALUES ('박철수', 26);")
conn.commit()

# #문제 3 READ (SELECT) 기본 조회
# # 다음 조건들을 만족하는 SELECT 쿼리를 작성하시오.
# # students 테이블의 전체 데이터를 조회
# # 나이가 22세 이상인 학생만 조회
# # name 이 “홍길동”인 학생만 조회
# with conn.cursor() as cursor  :
#     print("students 테이블의 전체 데이터 조회:")
#     cursor.execute("SELECT * FROM students;")
#     records = cursor.fetchall()
#     for record in records:
#         print(record)

#     print("\n나이가 22세 이상인 학생 조회:")
#     cursor.execute("SELECT * FROM students WHERE age >= 22;")
#     records = cursor.fetchall()
#     for record in records:
#         print(record)

#     print("\nname이 '홍길동'인 학생 조회:")
#     cursor.execute("SELECT * FROM students WHERE name = '홍길동';")
#     records = cursor.fetchall()
#     for record in records:
#         print(record)

# 문제 4 UPDATE 연습
# id = '912d995f-9bdc-423c-9df4-a715c29b46c9' 인 학생의 나이를 25로 수정하시오.
# Option : select 통한 UUID id 가져와서 update
with conn.cursor() as cursor  :
    cursor.execute("UPDATE students SET age = 25 WHERE id = '912d995f-9bdc-423c-9df4-a715c29b46c9';")
conn.commit()

with conn.cursor() as cursor :
    cursor.execute("select * From students")
    record = cursor.fetchall()
    second_student = record[1]
    second_student_id = second_student[0]
    cursor.execute(f"UPDATE students SET age = 30 WHERE id = '{second_student_id}';")    
conn.commit()

# 문제 5 DELETE 연습
# 저장된 순번에  세번째 학생 데이터를 삭제하는 DELETE 문을 작성하시오.
# Option : select 통한 UUID id 가져와서 delete

with conn.cursor() as cursor :
    cursor.execute("select * From students")
    record = cursor.fetchall()
    second_student = record[2]
    second_student_id = second_student[0]
    cursor.execute(f"DELETE FROM students  WHERE id = '{second_student_id}';")    
conn.commit()