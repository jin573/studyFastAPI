print("문법 복습용 - 데코레이터")

'''
1. 데코레이터
@wrapper() 혹은 @wrapper(arg1, arg2) -> wrapper라는 함수가 어딘가 정의되어 있어야 함. wrapper를 통해 매개변수 내의 인수, 함수 호출

2. 많이 쓰는 데코레이터
@staticmethod: 클래스 내 메서드를 정적 메서드로 변경, 클래스 인스턴스와 관계없이 호출 가능 (클래스 이름).(함수명)

        class MathUtils:
            @staticmethod
            def add(a, b):
                return a + b

        result = MathUtils.add(5, 3)  # 클래스 이름으로 직접 호출
        print(result)  # 8
        
@classmethod: 클래스 메서드로 변경 -> 클래스 자체를 첫 번째 인자로 받음. 클래스 변수에 접근해 상태를 변경하거나, 객체 생성시 유용

        class Circle:
            pi = 3.14

            @classmethod
            def area(cls, radius):
                return cls.pi * radius ** 2

        result = Circle.area(5)  # 클래스 이름으로 호출
        print(result)  # 78.5

3. 왜?
재사용성 및 중복을 줄이기 위해
'''

def log_function_call(func):
    def wrapper(*args, **kwargs): #*args 튜플 형태, **kwargs 딕셔너리 형태 
        print(f"함수 '{func.__name__}'이 호출 되었습니다.")
        print(f"인자: {args}, 키워드 인자: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a+b

@log_function_call
def multiply(a, b):
    return a*b

'''
데코레이터를 쓰지 않을 때때
def add(a, b):
    log_function_call()
    return a+b

def multiply(a, b):
    log_function_call()
    return a*b
'''

if __name__=="__main__":
    print("직접 실행할 경우에만 실행")
    result = add(5, 3)
    result2 = multiply(1, 2)
    print(f"결과: {result}, {result2}")
