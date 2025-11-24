```
{
  "prompt": "PostgreSQL books 테이블의 CRUD 작업을 다음과 같이 6개의 파일로 분리하여 생성해 주세요. 모든 파일은 `psycopg2`와 `db_connector.py`를 사용하여 데이터베이스에 연결해야 합니다. 모든 클래스와 함수에는 `if '__name__' == '__main__':` 안전장치를 추가하여 개별 실행 가능하도록 해주세요.\n\n1.  **`db_connector.py`**: DB 연결 파라미터(`DB_PARAMS`를 placeholder로 설정)와 `get_db_connection` context manager를 정의합니다.\n\n2.  **`book_manager.py`**: 테이블 생성(`create_books_table`), 데이터 삽입(`insert_books`), 가격 수정(`update_second_book_price`), 데이터 삭제(`delete_third_book`) 메서드를 포함하는 `BookManager` 클래스를 구현합니다.\n    * 테이블 생성 시 `uuid-ossp` 확장을 사용하고, `id`를 UUID PRIMARY KEY로 설정해야 합니다.\n    * UPDATE와 DELETE는 대상 도서의 제목('알고리즘 기초', '네트워크 이해')으로 먼저 UUID를 조회한 후 수행해야 합니다.\n\n3.  **`get_all_books.py`**: 전체 도서 목록을 조회하는 `GetAllBooks` 클래스를 구현합니다. 메서드 이름은 `get_books()`입니다.\n\n4.  **`get_expensive_books.py`**: 가격이 25000원 이상인 도서 목록을 조회하는 `GetExpensiveBooks` 클래스를 구현합니다. 메서드 이름은 `get_books()`입니다.\n\n5.  **`get_book_by_title.py`**: 제목을 인자(`title`)로 받아 특정 도서를 조회하는 `GetBookByTitle` 클래스를 구현합니다. 메서드 이름은 `get_book(title)`입니다.\n\n6.  **`02_DMLs_functions.py`**: 이 파일은 메인 실행 스크립트 역할을 합니다.\n    * `BookManager`, `GetAllBooks`, `GetExpensiveBooks`, `GetBookByTitle` 클래스를 모두 import 합니다.\n    * `if '__name__' == '__main__':` 블록 내에서 다음 순서로 모든 작업을 실행합니다:\n        1.  `BookManager`를 사용하여 테이블 생성 및 데이터 삽입.\n        2.  `GetAllBooks`를 사용하여 전체 데이터 조회.\n        3.  `BookManager`를 사용하여 가격 수정 및 데이터 삭제.\n        4.  조회 클래스들을 다시 사용하여 최종 데이터 상태를 검증합니다.\n\n모든 출력 메시지는 한국어로 작성하고, SELECT 결과는 출력하여 검증합니다.",
  "file_names": [
    "db_connector.py",
    "book_manager.py",
    "get_all_books.py",
    "get_expensive_books.py",
    "get_book_by_title.py",
    "02_DMLs_functions.py"
  ],
  "language": "python"
}
```