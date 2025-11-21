-- UUID primary key 사용
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE users_uuid_name (
  id_name UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(100)
);

insert INTO users_uuid_name (name)VALUES ('Ailce');

-- SELECT * FROM users_uuid_name; 
SELECT * FROM students;

insert INTO users_uuid_name (name) 
VALUES 
('Alice'), 
('Bob'), 
('Charlie');

UPDATE users_uuid_name 
SET name = 'UpdatedName' 
WHERE id_name = '3b06cc78-f87d-4656-a8c1-69464de42df6';

DELETE FROM users_uuid_name 
WHERE id_name = '3b06cc78-f87d-4656-a8c1-69464de42df6';


