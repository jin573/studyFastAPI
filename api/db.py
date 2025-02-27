from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# sqlalchemy: orm 라이브러리

DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"

db_engine=create_engine(DB_URL, echo=True) #데이터베이스와 연결하는 엔진 생성, echo=True가 있어야 쿼리를 콘솔에 출력할 수 있다
db_session=sessionmaker(autocommit=False, autoflush=False, bind=db_engine)#세션 설정. 자동 커밋 X, 변경 사항 즉시 반영 X, 데이터베이스 엔진과 세션 연결

Base=declarative_base() #orm에서 사용하는 기본 클래스를 생성

"""
의존성 주입으로 세션 제공
세션을 생성하고 yield 요청 시 전달
with문으로 자동 닫음
"""
def get_db():
    with db_session() as session:
        yield session