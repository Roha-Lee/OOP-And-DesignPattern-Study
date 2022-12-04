class Citizen:
    """주민 클래스"""
    drinking_age: int = 19 # 음주 가능 나이 
    
    def __init__(self, name: str, age: int, resident_id: int) -> None:
        """이름, 나이, 주민등록번호"""
        self.name: str = name
        self._age: int = age
        self._resident_id: int = resident_id
        
    def authenticate(self, id_field: int) -> bool:
        """본인이 맞는지 확인하는 메소드"""
        return self._resident_id == id_field
    
    def can_drink(self) -> bool:
        """음주 가능 나이인지 확인하는 메소드"""
        return self._age >= Citizen.drinking_age
    
    def __str__(self) -> str:
        """주민 정보를 문자열로 리턴하는 메소드"""
        return "${}씨는 ${}살입니다.".format(self.name, self._age)
    
    @property
    def age(self):
        print("나이를 리턴합니다.")
        return self._age
    
    @age.setter
    def age(self, value):
        print("나이를 설정합니다.")
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.")
            self._age = 0
        else:
            self._age = value
    
roha = Citizen("Roha", 20, "12345678")
# decorator property를 사용하게 되면 roha.age가 있는 부분에서 getter함수가 자동으로 호출된다. 
print(roha.age)
# 아래 코드에서는 setter가 실행된다. 
roha.age = 10
print(roha.age)