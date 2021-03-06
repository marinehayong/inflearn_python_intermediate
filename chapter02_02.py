# 200311 13:43
# Chapter02-02
# 클래스 상세 설명

# 클래스 재 선언
class Car():
    """
    Car Class
    Author : Kim
    Date : 2019.11.08
    """

    # 클래스 변수
    car_count = 0

    def __init__(self, company, details):
        # 인스턴스 변수를 선언할 때 _를 붙이는 습관
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self): # 인스턴스 메소드를 만들어봅시다.
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    def __del__(self):
        Car.car_count -= 1


# Self 의미: 클래스를 기반으로 생성된 인스턴스 자기 내부에 고유의 값을 저장하기 위한 예약된 지시어
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__ 확인
# 모든 클래스는 object를 상속받는다.
print(dir(car1))
print(dir(car2))

print()
print()

print(car1.__dict__)
print(car2.__dict__)

# Doctring
print(Car.__doc__)
print()

# 실행
# self를 넘기지 않지만 저절로, 자동으로 매개변수가 전달됨
car1.detail_info() # ID값을 출력한 거랑, 인스턴스 메소드로 self 출력한 거랑 ID가 같음
car2.detail_info()

# 에러
# Car.detail_info()
# 인자가 자동으로 전달되지 않기 때문에 명시적으로 전달
Car.detail_info(car1)
Car.detail_info(car2)

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__) == id(car3.__class__))

print()

# 인스턴스 변수
# 직접 접근(PEP 문법적으로 권장X)
print(car1._company, car2._company)
print(car2._company, car3._company)

print()
print()

# 클래스 변수

# 접근
# 공유가 됨
# 정석은 클래스 네임으로 접근
print(car1.car_count)
print(car2.car_count)
print(Car.car_count)

print()
print()


# 공유 확인
print(Car.__dict__)
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)
print(dir(car1))

del car2
# 삭제 확인
print(car1.car_count)
print(Car.car_count)

# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))