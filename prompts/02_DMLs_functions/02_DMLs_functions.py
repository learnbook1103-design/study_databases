# prompts/02_DMLs_functions.py

# --- 필요한 클래스들을 각 모듈에서 가져오기 ---
# 모든 기능은 각 클래스에 캡슐화되어 있으므로, 여기서는 해당 클래스들만 임포트합니다.
from book_manager import BookManager
from get_all_books import GetAllBooks
from get_expensive_books import GetExpensiveBooks
from get_book_by_title import GetBookByTitle

def main():
    """
    메인 실행 함수:
    - 데이터베이스 테이블 생성, 데이터 삽입, 수정, 삭제, 조회의 모든 과정을 순서대로 실행합니다.
    """
    print("="*50)
    print("도서 관리 시스템 시나리오를 시작합니다.")
    print("="*50)

    # --- 1. 초기 설정: 테이블 생성 및 데이터 삽입 ---
    print("\n[단계 1] 데이터베이스 초기 설정")
    book_manager = BookManager()
    book_manager.create_books_table()  # 테이블 생성 (또는 재생성)
    book_manager.insert_books()      # 초기 데이터 3개 삽입

    # --- 2. 초기 데이터 검증 ---
    print("\n[단계 2] 초기 데이터 상태 확인")
    all_books_retriever = GetAllBooks()
    all_books_retriever.get_books()

    # --- 3. 데이터 조작: 가격 수정 및 특정 데이터 삭제 ---
    print("\n[단계 3] 데이터 조작 (수정 및 삭제)")
    book_manager.update_second_book_price() # '알고리즘 기초' 가격 수정
    book_manager.delete_third_book()      # '네트워크 이해' 삭제

    # --- 4. 최종 데이터 검증 ---
    print("\n[단계 4] 최종 데이터 상태 확인")
    
    # 4-1. 전체 도서 목록 재조회
    print("\n--- 4-1. 조작 후 전체 도서 목록 ---")
    all_books_retriever.get_books()

    # 4-2. 고가 도서 목록 조회
    print("\n--- 4-2. 조작 후 고가 도서 목록 (25,000원 이상) ---")
    expensive_books_retriever = GetExpensiveBooks()
    expensive_books_retriever.get_books()

    # 4-3. 특정 도서 조회 (수정된 도서와 삭제된 도서)
    print("\n--- 4-3. 조작 후 특정 도서 조회 ---")
    book_by_title_retriever = GetBookByTitle()
    
    # 가격이 수정된 도서 조회
    book_by_title_retriever.get_book('알고리즘 기초')
    
    # 삭제되어 더 이상 존재하지 않는 도서 조회
    book_by_title_retriever.get_book('네트워크 이해')

    print("\n" + "="*50)
    print("도서 관리 시스템 시나리오가 모두 종료되었습니다.")
    print("="*50)


if __name__ == '__main__':
    # 이 스크립트가 직접 실행될 때만 main() 함수를 호출합니다.
    main()