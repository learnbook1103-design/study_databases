-- 문제 5 쇼핑몰 상품 테이블
CREATE TABLE shop_products (
    name VARCHAR(255),
    price int,
    stock int,
    category VARCHAR(255)
);

-- 데이터로 INSERT문 작성
INSERT INTO shop_products (name, price, stock, category)
VALUES ('USB 메모리', 12000, 50, '전자제품'),
       ('블루투스 스피커', 45000, 20, '전자제품'),
       ('물병', 5000, 100, '생활용품');

-- price가 10000 이상인 상품 조회
SELECT * 
FROM shop_products
WHERE price >= 10000;   

-- "물병"의 stock을 80으로 수정
UPDATE shop_products
SET stock = 80
WHERE name = '물병';    

-- "블루투스 스피커" 삭제
DELETE FROM shop_products
WHERE name = '블루투스 스피커'; 