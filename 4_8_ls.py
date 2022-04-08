'''
SQLite => DBMS
DBMS : MySQL, Oracle. MS-SQL
DB 

응용프로그램 => DBMS => DB

'''


'''
<sqlite3>
import sqlite3
sqlite3.version
# 버전 확인

connect => 데이터 베이스 생성하는 함수
con.cursor() // 호출하는 법 // 데이터 베이스는 엑셀과 굉장히 유사함

CREATE TABLE 만들 테이블 이름(컬럼이름 데이테타입, 컬럼이름 데이터타입)
CREATE VIEW
CREATE INDEX

파이썬            sqlite 
none      =       null
int       =        int(integer)
str       =        text
float     =       real

DDL(데이터 정의어) => CREATE, ALTER, DROP(흔적도 없이 전부 삭제)
DML(데이터 조작어) => SELECT, INSERT, UPDATE, DELETE(틀은 남아 있고 지움(내용물만 지움))
DCL(데이터 제어어) => COMMIT, ROLLBACK, GRANT, REVOKE

# 추가할 거
INSERT INTO 테이블 이름 VALUES () // 순서가 맞아야함
INSERT INTO 테이블 이름 SET 이름 = '우진', 나이 = 18, 성적 = 'A'

# 삭제 DELETE
DELETE FROM 테이블이름 WHERE 조건

# 수정 UPDATE
UPDATE 테이블이름 SET 컬럼명 = 변경할 값 WHERE 조건

'''