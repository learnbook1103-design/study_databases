# prompts/get_book_by_title.py
import psycopg2.extras
from db_connector import get_db_connection

class GetBookByTitle:
    """제목으로 특정 도서를 조회하는 클래스"""

    def get_book(self, title):
        """
        주어진 제목(`title`)으로 특정 도서를 조회하여 출력합니다.
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
                        print(f"  - ID: {book['id']}")
                        print(f"    제목: {book['title']}")
                        print(f"    가격: {book['price']:,}원")
                    else:
                        print(f"  '{title}' 제목의 도서를 찾을 수 없습니다.")
        except Exception as e:
            print(f"제목으로 도서 조회 중 에러 발생: {e}")

if __name__ == '__main__':
    # 이 파일이 직접 실행될 때 get_book 메서드를 테스트합니다.
    # (book_manager.py를 먼저 실행하여 데이터를 준비해주세요)
    print("'GetBookByTitle' 클래스 단독 실행 테스트입니다.")
    
    retriever = GetBookByTitle()

    # 테스트 케이스 1: 존재하는 도서
    retriever.get_book('파이썬 입문')

    # 테스트 케이스 2: 존재하지 않는 도서
    retriever.get_book('존재하지 않는 책')
    
    # 테스트 케이스 3: 빈 제목
    retriever.get_book('')
