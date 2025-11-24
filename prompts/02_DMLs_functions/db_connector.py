# prompts/db_connector.py
import psycopg2
from contextlib import contextmanager

# --- 데이터베이스 연결 정보 (실제 환경에 맞게 수정) ---
# 이 부분은 실제 데이터베이스의 호스트, 이름, 사용자, 비밀번호로 채워야 합니다.
# 예: DB_PARAMS = {
#     "host": "localhost",
#     "database": "mydatabase",
#     "user": "myuser",
#     "password": "mypassword"
# }
DB_PARAMS = {
    "host": "your_host",
    "database": "your_db",
    "user": "your_user",
    "password": "your_password"
}

@contextmanager
def get_db_connection():
    """
    데이터베이스 연결을 위한 컨텍스트 관리자를 제공합니다.
    연결, 트랜잭션, 에러 처리, 연결 종료를 자동으로 관리합니다.
    """
    conn = None
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        yield conn
    except psycopg2.Error as e:
        print(f"데이터베이스 연결 중 에러가 발생했습니다: {e}")
        # 컨텍스트 관리자 내에서 예외가 발생하면 트랜잭션을 롤백합니다.
        if conn:
            conn.rollback()
    finally:
        # 컨텍스트를 빠져나갈 때 연결을 항상 닫습니다.
        if conn:
            conn.close()

if __name__ == '__main__':
    # 이 파일이 직접 실행될 때 연결을 테스트하는 예제 코드
    print("데이터베이스 연결 테스트를 시작합니다...")
    try:
        with get_db_connection() as conn:
            if conn:
                # 연결 객체로부터 커서를 얻어 간단한 쿼리를 실행
                with conn.cursor() as cur:
                    cur.execute("SELECT version();")
                    db_version = cur.fetchone()
                    print(f"데이터베이스에 성공적으로 연결되었습니다.")
                    print(f"PostgreSQL 버전: {db_version[0]}")
    except Exception as e:
        # get_db_connection 내부에서 이미 에러 메시지를 출력하지만,
        # 이 블록은 get_db_connection 자체에서 예외가 발생할 경우를 대비합니다.
        print(f"연결 테스트 중 예상치 못한 에러 발생: {e}")
