# prompts/get_all_books.py
import psycopg2.extras
from db_connector import get_db_connection

class GetAllBooks:
    """전체 도서 목록을 조회하는 클래스"""

    def get_books(self):
        """
        books 테이블의 모든 데이터를 조회하여 출력합니다.
        - DictCursor를 사용하여 결과를 딕셔너리 형태로 받습니다.
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
                        print(f"  - ID: {book['id']}")
                        print(f"    제목: {book['title']}")
                        print(f"    가격: {book['price']:,}원")
        except Exception as e:
            print(f"전체 도서 목록 조회 중 에러 발생: {e}")

if __name__ == '__main__':
    # 이 파일이 직접 실행될 때 get_books 메서드를 테스트합니다.
    # 테스트를 위해서는 'books' 테이블이 존재하고 데이터가 있어야 합니다.
    # (book_manager.py를 먼저 실행하여 데이터를 준비해주세요)
    print("'GetAllBooks' 클래스 단독 실행 테스트입니다.")
    
    retriever = GetAllBooks()
    retriever.get_books()
