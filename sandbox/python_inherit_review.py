print("문법 복습용 - 상속")
'''
클래스 변수에 접근할 때는 (클래스).(속성) 으로 바로 접근
인스턴스 변수에 접근할 경우는 생성자에서 초기화 -> getter
'''

#상위 클래스
class Animal():
    height = 30

    def get_height(self):
        print(f"Animal {self.height}")

#상속 클래스
class Dog(Animal):
    height = 20

    def get_height(self):
        print(f"Dog {self.height}")
        return self.height
        
def inherit():
    dog = Dog()
    print(dog.get_height()) #20


if __name__=="__main__":
    print("직접 실행할 경우에만 실행")
    inherit()
    print(Animal.height)
