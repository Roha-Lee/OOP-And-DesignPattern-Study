class Citizen:
    """주민 클래스"""
    drinking_age: int = 19 # 음주 가능 나이 
    
    def __init__(self, name: str, age: int, resident_id: int) -> None:
        """이름, 나이, 주민등록번호"""
        # 멤버 변수, 메소드 앞에 __를 붙이면 외부에서 접근할 수 없게 된다. 
        self.name: str = name
        # 아래 변수들을 외부에서 접근할 수 없기 때문에 이대로는 제대로 사용할 수 없다. 
        # 변수를 무조건 숨기기만 하면 안된다! -> 변수에 접근하는 메소드를 따로 만들어 줘야 한다. 
        self.__age: int = age
        self.__resident_id: int = resident_id
        
    def authenticate(self, id_field: int) -> bool:
        """본인이 맞는지 확인하는 메소드"""
        return self.__resident_id == id_field
    
    def can_drink(self) -> bool:
        """음주 가능 나이인지 확인하는 메소드"""
        return self.__age >= Citizen.drinking_age
    
    def __str__(self) -> str:
        """주민 정보를 문자열로 리턴하는 메소드"""
        return "${}씨는 ${}살입니다.".format(self.name, self.__age)
    
    def get_age(self) -> int:
        # age의 값을 읽을 수 있다. 
        return self.__age
    
    def set_age(self, age: int) -> None:
        # age값을 설정해 줄 수 있다. 
        self.__age = age
        
roha = Citizen("rohagru", 20, "1234567")
print(roha.get_age())
roha.set_age(22)
print(roha.get_age())
'''
캡슐화의 두번째 정의: 객체의 속성과 그것을 사용하는 행동을 하나로 묶는 것. 
변수에 접근하는 방식을 몇개의 클래스로 제한하는 것. 
'''