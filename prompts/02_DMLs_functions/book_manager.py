# prompts/book_manager.py
import psycopg2.extras
from db_connector import get_db_connection

class BookManager:
    """books 테이블의 생성, 삽입, 수정, 삭제를 관리하는 클래스"""

    def create_books_table(self):
        """
        books 테이블을 생성합니다.
        - `uuid-ossp` 확장을 활성화합니다.
        - 테이블이 이미 존재하면 삭제하고 다시 생성합니다.
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
                    print("\`books\` 테이블이 성공적으로 생성되었습니다.")
        except Exception as e:
            print(f"테이블 생성 중 에러 발생: {e}")

    def insert_books(self):
        """
        books 테이블에 초기 데이터를 삽입합니다.
        - `executemany` 대신 `execute_values`를 사용하여 효율성을 높입니다.
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
        """책 제목으로 UUID를 조회하여 반환하는 내부 메서드"""
        cur.execute("SELECT id FROM books WHERE title = %s;", (title,))
        result = cur.fetchone()
        return result[0] if result else None

    def update_second_book_price(self):
        """'알고리즘 기초' 도서의 가격을 27,000원으로 수정합니다."""
        target_title = '알고리즘 기초'
        new_price = 27000
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    book_id = self._get_book_id_by_title(cur, target_title)
                    if book_id:
                        cur.execute(
                            "UPDATE books SET price = %s WHERE id = %s;",
                            (new_price, book_id)
                        )
                        conn.commit()
                        print(f"도서 '{target_title}'의 가격이 {new_price:,}원으로 수정되었습니다.")
                    else:
                        print(f"'{target_title}' 제목의 도서를 찾을 수 없습니다.")
        except Exception as e:
            print(f"가격 수정 중 에러 발생: {e}")

    def delete_third_book(self):
        """'네트워크 이해' 도서를 삭제합니다."""
        target_title = '네트워크 이해'
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    book_id = self._get_book_id_by_title(cur, target_title)
                    if book_id:
                        cur.execute("DELETE FROM books WHERE id = %s;", (book_id,))
                        conn.commit()
                        print(f"도서 '{target_title}'이(가) 성공적으로 삭제되었습니다.")
                    else:
                        print(f"'{target_title}' 제목의 도서를 찾을 수 없습니다.")
        except Exception as e:
            print(f"데이터 삭제 중 에러 발생: {e}")

if __name__ == '__main__':
    # 이 파일이 직접 실행될 때 각 메서드를 테스트하는 코드
    manager = BookManager()
    
    print("1. 테이블 생성 작업을 시작합니다.")
    manager.create_books_table()
    
    print("\n2. 데이터 삽입 작업을 시작합니다.")
    manager.insert_books()

    # 데이터가 잘 들어갔는지 확인하기 위해 임시 조회 코드 추가
    try:
        with get_db_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                print("\n--- 삽입 후 데이터 확인 ---")
                cur.execute("SELECT title, price FROM books ORDER BY title;")
                for book in cur.fetchall():
                    print(f"  제목: {book['title']}, 가격: {book['price']:,}원")
    except Exception as e:
        print(f"데이터 확인 중 에러: {e}")

    print("\n3. 가격 수정 작업을 시작합니다.")
    manager.update_second_book_price()

    print("\n4. 데이터 삭제 작업을 시작합니다.")
    manager.delete_third_book()

    # 최종 상태 확인
    try:
        with get_db_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                print("\n--- 최종 데이터 확인 ---")
                cur.execute("SELECT title, price FROM books ORDER BY title;")
                books = cur.fetchall()
                if not books:
                    print("  (테이블에 데이터가 없습니다)")
                for book in books:
                    print(f"  제목: {book['title']}, 가격: {book['price']:,}원")
    except Exception as e:
        print(f"최종 데이터 확인 중 에러: {e}")
