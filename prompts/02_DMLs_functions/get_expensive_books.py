# prompts/get_expensive_books.py
import psycopg2.extras
from db_connector import get_db_connection

class GetExpensiveBooks:
    """가격이 특정 기준 이상인 도서 목록을 조회하는 클래스"""

    def get_books(self, min_price=25000):
        """
        가격이 `min_price` 이상인 도서를 조회하여 출력합니다.
        - 결과를 가격 내림차순으로 정렬합니다.
        """
        print(f"\n--- [가격이 {min_price:,}원 이상인 도서 목록 조회] ---")
        try:
            with get_db_connection() as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    cur.execute(
                        "SELECT title, price FROM books WHERE price >= %s ORDER BY price DESC;",
                        (min_price,)
                    )
                    books = cur.fetchall()

                    if not books:
                        print(f"  (가격이 {min_price:,}원 이상인 도서가 없습니다)")
                        return
                    
                    for book in books:
                        print(f"  - 제목: {book['title']}, 가격: {book['price']:,}원")
        except Exception as e:
            print(f"고가 도서 목록 조회 중 에러 발생: {e}")

if __name__ == '__main__':
    # 이 파일이 직접 실행될 때 get_books 메서드를 테스트합니다.
    # (book_manager.py를 먼저 실행하여 데이터를 준비해주세요)
    print("'GetExpensiveBooks' 클래스 단독 실행 테스트입니다.")
    
    retriever = GetExpensiveBooks()
    retriever.get_books()
