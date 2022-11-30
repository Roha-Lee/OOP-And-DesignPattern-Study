'''
캡슐화의 정의
1. 객체의 일부 구현 내용에 대한 외부로부터의 직접적인 액세스를 차단하는 것 
2. 객체의 속성과 그것을 사용하는 행동을 하나로 묶는 것
'''

class Citizen:
    """주민 클래스"""
    drinking_age: int = 19 # 음주 가능 나이 
    
    def __init__(self, name: str, age: int, resident_id: int) -> None:
        """이름, 나이, 주민등록번호"""
        # 멤버 변수, 메소드 앞에 __를 붙이면 외부에서 접근할 수 없게 된다. 
        self.name: str = name
        self.__age: int = age
        self.__resident_id: int = resident_id
        
    def __authenticate(self, id_field: int) -> bool:
        """본인이 맞는지 확인하는 메소드"""
        return self.__resident_id == id_field
    
    def can_drink(self) -> bool:
        """음주 가능 나이인지 확인하는 메소드"""
        return self.__age >= Citizen.drinking_age
    
    def __str__(self) -> str:
        """주민 정보를 문자열로 리턴하는 메소드"""
        return "${}씨는 ${}살입니다.".format(self.name, self.__age)
    
roha = Citizen("Roha", 20, "12345678")
# roha.__age # error
# roha.authenticate("12345678") # error