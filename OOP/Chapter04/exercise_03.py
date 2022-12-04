class Citizen:
    """주민 클래스"""
    drinking_age: int = 19 # 음주 가능 나이 
    
    def __init__(self, name: str, age: int, resident_id: int) -> None:
        """이름, 나이, 주민등록번호"""
        # 멤버 변수, 메소드 앞에 __를 붙이면 외부에서 접근할 수 없게 된다. 
        self.name: str = name
        # 아래 변수들을 외부에서 접근할 수 없기 때문에 이대로는 제대로 사용할 수 없다. 
        # 변수를 무조건 숨기기만 하면 안된다! -> 변수에 접근하는 메소드를 따로 만들어 줘야 한다. 
        self.set_age(age)
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
    
    def get_age(self) -> int:
        # age의 값을 읽을 수 있다. getter 메소드
        return self._age
    
    def set_age(self, age: int) -> None:
        # age값을 설정해 줄 수 있다. setter 메소드
        if age < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.")
            self._age = 0
        else:
            self._age = age
        
'''
파이썬 개발자들을 변수 앞에 _ 한개를 붙이는 것을 외부에서 접근하지 말라는 표시로 간주한다. 
사실 _ 1개는 아무런 기능이 없다. 하지만 다른 개발자들에게 이게 붙은 변수/메소드는 클래스 
외부에서 직접 접근하지 말라는 안내 역할을 한다. 
_ 1개가 있는 경우 getter/setter를 사용하도록 하자. 
'''