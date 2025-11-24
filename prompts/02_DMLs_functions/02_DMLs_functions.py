# prompts/02_DMLs_functions.py

# --- 통합 관리 클래스를 가져오기 ---
# 모든 기능이 IntegratedBookManager에 포함되어 있습니다.
from integrated_book_manager import IntegratedBookManager

def main():
    """
    메인 실행 함수:
    - 통합 관리 클래스를 사용하여 데이터베이스 CRUD 시나리오를 실행합니다.
    """
    print("="*50)
    print("통합 도서 관리 시스템 시나리오를 시작합니다.")
    print("="*50)

    # --- 1. 통합 관리 클래스 인스턴스 생성 ---
    manager = IntegratedBookManager()

    # --- 2. 초기 설정: 테이블 생성 및 데이터 삽입 ---
    print("\n[단계 1] 데이터베이스 초기 설정")
    manager.create_books_table()
    manager.insert_books()

    # --- 3. 초기 데이터 검증 ---
    print("\n[단계 2] 초기 데이터 상태 확인")
    manager.get_all_books()

    # --- 4. 데이터 조작: 가격 수정 및 특정 데이터 삭제 ---
    print("\n[단계 3] 데이터 조작 (수정 및 삭제)")
    manager.update_book_price('알고리즘 기초', 27000)
    manager.delete_book('네트워크 이해')

    # --- 5. 최종 데이터 검증 ---
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


if __name__ == '__main__':
    # 이 스크립트가 직접 실행될 때만 main() 함수를 호출합니다.
    main()
