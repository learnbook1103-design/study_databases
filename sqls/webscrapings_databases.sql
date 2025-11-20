CREATE TABLE study_webscrapings_database (
    contents varchar(500),
    link varchar(500),
    link_html varchar(500),
    link_href varchar(500)
);

SELECT *
FROM study_webscrapings_database;

CREATE TABLE study_webscripings_database (
    id VARCHAR(500) PRIMARY KEY,  -- PRIMARY KEY : 해당 컬럼에 unique한 값만 들어가도록 설정
    contents VARCHAR(500),
    link VARCHAR(500),
    link_html VARCHAR(500),
    link_href VARCHAR(500),
    created_at VARCHAR(500) DEFAULT NOW()   -- DEFAULT NOW() : 현재 시간으로 기본값 설정
);