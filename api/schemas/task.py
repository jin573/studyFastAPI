from pydantic import BaseModel, Field #PyDantic 라이브러리로 타입 힌트를 사용해 유효성 검사

#API 스키마 (요청과 응답) - 데이터베이스의 스키마와 다르다!
"""
스키마 형태
변수명: 타입 힌트 = Field(기본 값, 속성)
속성 1. example 예시
속성 2. description 인수 설명

str|None 은 titel이 str 혹은 None을 허용한다는 의미. Optional[str] 로 사용해도 됨
"""
class Task(BaseModel):
    id: int
    title :str | None = Field(None, example = "세탁소에 맡긴 것을 찾으러 가기")
    done: bool = Field(False, description = "완료 플래그")