# DB

- 행 : 튜플
- 열 : 어트리뷰트
- 테이블이름 : 릴레이션?
- degree(차수) : 튜플의 수
- 카티널리티 : 어트리뷰트의 수

---

#### SQL 문법

- **DDL**

  - 데이터 정의 언어 (테이블을 수정하거나 삭제)
  - 데이터를 정의하기 위한 언어이다.
  - 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령이다

  

  - **CREATE** : create table (테이블 명) (컬럼, 컬럼, );

    - ```sqlite
      CREATE TABLE 테이블_이름 (
          속성_이름 데이터_타입 [NOT NULL] [DEFAULT 기본값]               // 1
      
          [PRIMARY KEY (속성_리스트)]                                 // 2
          [UNIQUE (속성_리스트)]                                      // 3
          [FOREIGN KEY (속성_리스트) PREFERENCES 테이블_이름(속성_리스트)]  // 4
          [ON DELETE 옵션] [ON UPDATE 옵션]
          [CONSTRAINT 이름] [CHECK(조건)]                             // 5
      );
      1. 테이블을 구성하는 각 속성의 이름, 데이터 타입, 기본적인 제약 사항을 정의한다.
      
      2. 기본키 : 테이블에 하나만 존재할 수 있다. (유일성, 최소성(꼭 필요한 속성으로 구성, 슈퍼키는(2개이상 구성) 최소성을 만족 못함.), 개체 무결성(Null 이 들어가면 안됨.))
      
      3. 대체키 : 테이블에 여러 개 존재할 수 있다. (유일한 속성이나 기본키가 아닌 키들, 기본키가 아니기에 NULL 값을 가질 수 있다.)
      
      4. 외래키 : 테이블에 여러 개 존재할 수 있다. (다른 테이블을 참조하는 키 (pk를 설정), 부모 테이블이 먼저 삭제 될 수 없다. 자식 삭제 후 부모 삭제해야함.)
      
      5. 데이터 무결성을 위한 제약 조건 : 테이블에 여러 개의 제약조건이 존재할 수 있다.
      
         > 데이터 무결성 이란?저장된 데이터 값의 정확성을 의미관객수가 음수로 저장되면 무결성 위반유효성 검사를 하여 데이터 무결성을 유지CONSTRAINT CHK_ATD CHECK(attendance >= 0)
      
      `ON DELETE` / `ON UPDATE` 옵션
      
      - NO ACTION : 참조하는 테이블의 데이터 삭제 불가
      - CASECADE : 참조하는 테이블 데이터 삭제시 참조하는 데이터도 같이 삭제
      - SET NULL : 참조하는 테이블 데이터 삭제시 NULL 로 속성값 변경 (NULL 허용 필요)
      - SET DEFAULT : 참조하는 테이블 데이터 삭제시 DEFAULT 값으로 변경 (DEFAULT 값 설정 필요.)
      
      CREATE TABLE table(
        column1 datatype PRIMARY KEY,
        column2 datatype
      );
      
      ex)
      CREATE TABLE classmates(
        # 프라이머리키는 INTEGER만 사용가능 INT X, 자동으로 id값 증가
        # 특정한 요구사항이 없아면 AUTOINCREMENT 속성을 사용하지 않는다.하지만 django에서는 사용
        id INTEGER PRIMARY KEY AUTOINCREMENT, 	
        name TEXT,
        age INT,
        address TEXT,
      );
      
      # NOT NULL 조건 추가
      CREATE TABLE classmates(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INT NOT NULL,
        address TEXT NOT NULL
      );
      
      # PRIMARY KEY 값을 안 넣어주는 경우 rowid로 PRIMARY KEY 확인 가능
      SELECT rowid, * FROM classmates;
      ```

  - DROP(테이블 삭제)

    - `DROP TABLE table;`

    - ```sql
      salite> DROP TABLE classmates;
      ```

  - **ALTER**: 테이블 변경 ( 속성 추가 / 삭제, 제약조건 추가 / 삭제)

    - `ALTER TABLE table;`

    - ```sqlite
      CREATE TABLE articles(
        title TEXT NOT NULL,
        content TEXT NOT NULL
      );
      INSERT INTO articles VALUES('1번 글', '1번글 내용');
      
      # 테이블 이름 바꾸기
      ALTER TABLE articles RENAME TO news;
      
      # 필드 추가
      ALTER TABLE news ADD COLUMN created_at TEXT;
      ALTER TABLE news ADD COLUMN updated_at TEXT NOT NULL DEFAULT 1;
      INSERT INTO news VALUES('title','content',datetime('now'));
      
      # 필드 삭제
  ALTER TABLE 테이블_이름 DROP 속성_이름 CASCADE|RESTRICT;
      // 제약조건이나 참조하는 속성이 존재할 때
      // cascade : 함께 삭제 / restrict : 삭제를 막는다.
      ALTER TABLE users DROP created_at RESTRICT;
      
      # 제약 조건 추가
      ALTER TABLE 테이블_이름
        ADD CONSTRAINT 제약조건_이름 제약조건_내용;
      ALTER TABLE Movie
        ADD CONSTRAINT CHK_ATD CHECK(attendance >= 0);
        
      # 제약 조건 삭제
      ALTER TABLE 테이블_이름
        DROP CONSTRAINT 제약조건_이름;
      ```
      
    - 

- **DML**

  - 데이터 조작 언어 (데이터 추가, 수정, 삭제, 읽기)
  - 데이터를 저장, 수정, 삭제 , 조회 등을 하기 위한 언어이다

  

  - INSERT(데이터삽입) 

    - `INSERT INTO table(column1,column2,...) VALUES(value1,value2,...`)

    - ```sqlite
      INSERT INTO classmates(name, age, address)
      VALUES ('홍길동', 23, '서울');
      
      # 모든 필드에 데이터를넣을때는 필드명을 작성할 필요가 없다.
      INSERT INTO classmates VALUES('김길동', 25, '부산');
      
      # 한번에 여러개값 추가
      INSERT INTO classmates VALUES('김길동', 25, '부산'),('홍길동', 23, '서울');
      
      # 다른 테이블에서 검색한 데이터를 튜플로 삽입할 수 있다.
      INSERT INTO COMPANY_BKP
      SELECT * FROM COMPANY
      WHERE ID IN (SELECT ID
                   FROM COMPANY);
      ```

  - UPDATE(갱신)

    - `UPDATE table SET column1=value1, column2=value2,... WHERE condition;`

    - ```sqlite
      
      ```

  - DELETE(삭제)

    - `DELETE FROM table WHERE condition;`

    - ```sqlite
      # 모든 데이터 삭제
      DELETE FROM classmates;
      
      DELETE FROM classmates where age='22';
      ```

      

  - SELECT(검색,조회)

    - ```sqlite
      # SELECT 보고싶은필드 FROM 테이블명
      sqlite> SELECT * FROM examples;
      sqlite> SELECT id,name FROM classmates;
      
      # 하나의 값만 가져오고 싶을때
      SELECT rowid,name FROM classmates LIMIT 1;
      
      # 시작 조회 아이디 값부터 조회(처음은 0번)
      SELECT rowid,name FROM classmates LIMIT 2 OFFSET 2;
      ```

    - WHERE

      - ```sqlite
        SELECT rowid,name FROM classmates WHERE name='이길동';
        SELECT rowid,name FROM classmates WHERE age=22;
        
        # 중복없이 가져올때
        SELECT DISTINCT age FROM classmates;
        SELECT DISTINCT age FROM classmates where address='광주';
        
        # 특정 조건
        SELECT * FROM users WHERE age>=30;
        # 조건 두개 (AND, OR 사용가능)
        SELECT first_name,age FROM users WHERE age>=30 and last_name='김';
        
        # IN, BETWEEN 사용 가능
        WHERE col_1 = 100
        WHERE col2 IN (2, 7, 9)
        WHERE col4 BETWEEN 10 AND 20
        
        #갯수
        SELECT COUNT(*) FROM users;
        SELECT COUNT(age) FROM users;
        
        # 산술식 검색
        SELECT 영화이름, 관객수 + 10000 AS 조정 관객수
        FROM 영화;
        
        영화이름 | 조정 관객수
        -------------------
        뮬란    | 10032 (기존 32)
        
        SELECT 이름, 월급, 월급*12 AS "연봉"
        FROM 부서명록;
        
        이름 | 월급 | 연봉
        ----------------
        철수 | 300 | 3600
        영희 | 400 | 4800
        영수 | 500 | 6000
        
        
        # 평균(AVG(),SUM(),MIN(),MAX())
        SELECT AVG(age) FROM users;
        SELECT AVG(age) from users WHERE age>=30;
        
        # 잔액이 가장 높은 사람의 잔액과 이름
        SELECT MAX(balance),first_name FROM users;
        
        # 30살 이상인 사람의 계좌 평균잔액?
        SELECT AVG(balance) FROM users WHERE age>=30;
        
        # LIKE : 패턴을 확인하여 해당하는 값을 반환
        # users에서 20대인 사람은?
  SELECT * FROM users WHERE age LIKE'2_';
        # users에서 지역번호가 02인 사람만?
        SELECT * FROM users WHERE phone LIKE'02-%';
        # users에서 이름이 '준'으로 끝나는 사람만?
        SELECT * FROM users WHERE first_name LIKE'%준';
        # users에서 중간번호가 5114인 사람만?
        SELECT * FROM users WHERE phone LIKE'%-5114-%';
        
        # ORDER (정렬)
  SELECT columns FROM table ORDER BY colunm1, column2 ASC/DESC;
        # users에서 나이순으로 오름차순 정렬하여 상위 10개만 뽑아보면?
      SELECT * FROM users ORDER BY age ASC LIMIT 10;
        # users에서 나이순, 성순으로 오름차순 정렬하여 상위 10개만?
      SELECT * FROM users ORDER BY age,last_name ASC LIMIT 10;
        # users에서 계좌잔액순으로 내림차순 정렬하여 해당하는 사람의 성과 이름을 10개만?
      SELECT first_name, last_name FROM users ORDER BY balance DESC LIMIT 10;
        
        ```
      - GROUP BY (지정된 기준에 따라 행 세트를 그룹으로 결합한다, 데이터를 요약하는 상황)
      - users에서 각 성씨가 몇명씩 있는지 조회
      - SELECT last_name,COUNT(last_name) FROM users GROUP BY last_name;
      - 출력시 필드명이 별칭으로 나온다.
      - SELECT last_name,COUNT(last_name) AS name_count FROM users GROUP BY last_name;
      
        ```
        
        # 와일드카드(wild cards)
        - _(언더바)
          - 반드시 이 자리에 한개의 문자가 존재해야 한다.(a__ : abc,ads,ald..)
        - %
          - 이자리에 문자열이 있을수도 없을수도있다.
          - (a% : a,abc,ab)
          - (%a : a가 마지막에 오는)
          -  (%a% : a가 가운데 있는)
        
        ![image-20210325131435286](DB(sqlite3).assets/image-20210325131435286.png)
        ```
    
    
    
    
    
    - 좀더 이쁘게
    
      - ```sqlite
        sqlite> .headers on
        sqlite> .mode column
        sqlite> SELECT * FROM examples;
        
        # 다시 csv로 보기
        sqlite> .mode scv
        ```

- **DCL**

  - 데이터 제어 언어
  - 데이터베이스 사용자의 권한 제어를 위해 사용 되는 언어이다.

  

  - GRANT,REVOKE,COMMIT,ROLLBACK

---

- sqlite 문법

```sqlite
# 데이터베이스 생성 or 해당데이터베이스 접속
$ sqlite3 tutorial.sqlite3
sqlite> .databases

# scv 모드 전환후 hellodb.csv 파일을 가지고 users_user 테이블 생성(해당 테이블이 없을경우)
sqlite> .mode csv
sqlite> .import hellodb.csv users_user
```

- Table 및 Schema 조회
  - 테이블 목록 조회
    - .tables
  - 특정 테이블 스키마 조회
    - .schema table

---

- Datatype
  - INTEGER
  - TEXT (CHAR(20)-고정적으로 20칸 할당, VARCHAR(20)-맥시멈 20글자, TEXT)
  - REAL (REAL, DOUBLE, FLOAT)
  - NUMERTIC (NUMERIC, DECIMAL, BOOLEAN, DATE, DATETIME)
  - BLOB (이미지등 파일 그대로 저장)

