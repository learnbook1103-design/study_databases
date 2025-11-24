# prompts/integrated_book_manager.py
import psycopg2
import psycopg2.extras
from contextlib import contextmanager

# --- 1. 데이터베이스 연결 정보 (기존 db_connector.py) ---
DB_PARAMS = {
    "host": "your_host",
    "database": "your_db",
    "user": "your_user",
    "password": "your_password"
}

@contextmanager
def get_db_connection():
    """
    데이터베이스 연결을 위한 컨텍스트 관리자.
    연결, 트랜잭션, 에러 처리, 연결 종료를 자동으로 관리합니다.
    """
    conn = None
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        yield conn
    except psycopg2.Error as e:
        print(f"데이터베이스 연결 중 에러가 발생했습니다: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

# --- 2. 모든 기능을 통합한 단일 클래스 ---
class IntegratedBookManager:
    """
    하나의 클래스에서 도서 데이터베이스의 모든 작업을 관리합니다.
    (테이블 생성, 데이터 삽입/수정/삭제, 다양한 조회 기능 포함)
    """

    # --- CUD (생성, 삽입, 수정, 삭제) 메서드 ---

    def create_books_table(self):
        """
        books 테이블을 생성합니다. (기존 BookManager 클래스의 기능)
        - `uuid-ossp` 확장을 활성화하고, 테이블이 이미 존재하면 삭제 후 다시 생성합니다.
        """
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")
                    cur.execute("DROP TABLE IF EXISTS books;")
                    cur.execute("""
                        CREATE TABLE books (
                            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                            title VARCHAR(100) NOT NULL UNIQUE,
                            price INT NOT NULL
                        );
                    """)
                    conn.commit()
                    print("`books` 테이블이 성공적으로 생성되었습니다.")
        except Exception as e:
            print(f"테이블 생성 중 에러 발생: {e}")

    def insert_books(self):
        """
        books 테이블에 초기 데이터를 삽입합니다. (기존 BookManager 클래스의 기능)
        """
        books_to_insert = [
            ('파이썬 입문', 19000),
            ('알고리즘 기초', 25000),
            ('네트워크 이해', 30000)
        ]
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    psycopg2.extras.execute_values(
                        cur,
                        "INSERT INTO books (title, price) VALUES %s",
                        books_to_insert
                    )
                    conn.commit()
                    print(f"{len(books_to_insert)}개의 도서가 성공적으로 삽입되었습니다.")
        except Exception as e:
            print(f"데이터 삽입 중 에러 발생: {e}")

    def _get_book_id_by_title(self, cur, title):
        """(내부용) 책 제목으로 UUID를 조회하여 반환합니다."""
        cur.execute("SELECT id FROM books WHERE title = %s;", (title,))
        result = cur.fetchone()
        return result[0] if result else None

    def update_book_price(self, title, new_price):
        """
        특정 제목의 도서 가격을 수정합니다. (기존 BookManager 클래스의 기능)
        """
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    book_id = self._get_book_id_by_title(cur, title)
                    if book_id:
                        cur.execute("UPDATE books SET price = %s WHERE id = %s;", (new_price, book_id))
                        conn.commit()
                        print(f"도서 '{title}'의 가격이 {new_price:,}원으로 수정되었습니다.")
                    else:
                        print(f"'{title}' 제목의 도서를 찾을 수 없어 가격을 수정할 수 없습니다.")
        except Exception as e:
            print(f"가격 수정 중 에러 발생: {e}")

    def delete_book(self, title):
        """
        특정 제목의 도서를 삭제합니다. (기존 BookManager 클래스의 기능)
        """
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    book_id = self._get_book_id_by_title(cur, title)
                    if book_id:
                        cur.execute("DELETE FROM books WHERE id = %s;", (book_id,))
                        conn.commit()
                        print(f"도서 '{title}'이(가) 성공적으로 삭제되었습니다.")
                    else:
                        print(f"'{title}' 제목의 도서를 찾을 수 없어 삭제할 수 없습니다.")
        except Exception as e:
            print(f"데이터 삭제 중 에러 발생: {e}")

    # --- R (조회) 메서드 ---

    def get_all_books(self):
        """
        전체 도서 목록을 조회합니다. (기존 GetAllBooks 클래스의 기능)
        """
        print("\n--- [전체 도서 목록 조회] ---")
        try:
            with get_db_connection() as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    cur.execute("SELECT id, title, price FROM books ORDER BY title;")
                    books = cur.fetchall()
                    if not books:
                        print("  (조회된 데이터가 없습니다)")
                        return
                    for book in books:
                        print(f"  - 제목: {book['title']}, 가격: {book['price']:,}원 (ID: {book['id']})")
        except Exception as e:
            print(f"전체 도서 목록 조회 중 에러 발생: {e}")

    def get_expensive_books(self, min_price=25000):
        """
        특정 가격 이상인 도서 목록을 조회합니다. (기존 GetExpensiveBooks 클래스의 기능)
        """
        print(f"\n--- [가격이 {min_price:,}원 이상인 도서 목록 조회] ---")
        try:
            with get_db_connection() as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    cur.execute("SELECT title, price FROM books WHERE price >= %s ORDER BY price DESC;", (min_price,))
                    books = cur.fetchall()
                    if not books:
                        print(f"  (가격이 {min_price:,}원 이상인 도서가 없습니다)")
                        return
                    for book in books:
                        print(f"  - 제목: {book['title']}, 가격: {book['price']:,}원")
        except Exception as e:
            print(f"고가 도서 목록 조회 중 에러 발생: {e}")

    def get_book_by_title(self, title):
        """
        제목으로 특정 도서를 조회합니다. (기존 GetBookByTitle 클래스의 기능)
        """
        print(f"\n--- [제목으로 도서 검색: '{title}'] ---")
        if not title or not title.strip():
            print("  (검색할 제목을 입력해야 합니다)")
            return
        try:
            with get_db_connection() as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    cur.execute("SELECT id, title, price FROM books WHERE title = %s;", (title,))
                    book = cur.fetchone()
                    if book:
                        print(f"  - 발견: {book['title']}, 가격: {book['price']:,}원 (ID: {book['id']})")
                    else:
                        print(f"  '{title}' 제목의 도서를 찾을 수 없습니다.")
        except Exception as e:
            print(f"제목으로 도서 조회 중 에러 발생: {e}")


# --- 3. 메인 실행 블록 ---
if __name__ == '__main__':
    """
    이 스크립트가 직접 실행될 때 전체 시나리오를 수행합니다.
    """
    print("="*50)
    print("통합 도서 관리 시스템 시나리오를 시작합니다.")
    print("="*50)

    # 통합 관리 클래스의 인스턴스 생성
    manager = IntegratedBookManager()

    # --- 단계 1: 초기 설정 (테이블 생성 및 데이터 삽입) ---
    print("\n[단계 1] 데이터베이스 초기 설정")
    manager.create_books_table()
    manager.insert_books()

    # --- 단계 2: 초기 데이터 상태 확인 ---
    print("\n[단계 2] 초기 데이터 상태 확인")
    manager.get_all_books()

    # --- 단계 3: 데이터 조작 (수정 및 삭제) ---
    print("\n[단계 3] 데이터 조작 (수정 및 삭제)")
    manager.update_book_price('알고리즘 기초', 27000)
    manager.delete_book('네트워크 이해')

    # --- 단계 4: 최종 데이터 상태 확인 ---
    print("\n[단계 4] 최종 데이터 상태 확인")
    print("\n--- 4-1. 조작 후 전체 도서 목록 ---")
    manager.get_all_books()
    
    print("\n--- 4-2. 조작 후 고가 도서 목록 (25,000원 이상) ---")
    manager.get_expensive_books()
    
    print("\n--- 4-3. 조작 후 특정 도서 상세 조회 ---")
    manager.get_book_by_title('알고리즘 기초') # 수정된 책
    manager.get_book_by_title('네트워크 이해') # 삭제된 책

    print("\n" + "="*50)
    print("통합 도서 관리 시스템 시나리오가 모두 종료되었습니다.")
    print("="*50)
