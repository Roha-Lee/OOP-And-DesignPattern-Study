class User:
    count = 0
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
        User.count += 1

    def say_hello(self):
        print("안녕하세요! 저는 {} 입니다.".format(self.name))
    
    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)
    
    @classmethod
    def from_string(cls, string_params):
        name, email, password = string_params.split(",")
        return cls(name, email, password)

    @classmethod
    def from_list(cls, list_params):
        return cls(list_params[0], list_params[1], list_params[2])

    @staticmethod
    def is_valid_email(email_address):
        '''
        정적 메소드: 인스턴스 변수와 클래스 변수를 전혀 다루지 않는 메소드의 경우 정적 메소드로 만든다. 
        아래의 예시와 같이 인스턴스, 클래스 모두를 통해 사용 가능하다. 
        클래스 가까이에 함수를 두기 위하여 만들어진 기능이지만, 실제 필요성에 대해서는 논의가 있다.
        (전문가를 위한 파이썬)
        '''
        return "@" in email_address

user1 = User.from_string("******,********,******")
user2 = User.from_list(["******", "******", "******"])

print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)

print(User.is_valid_email("roha"))
print(User.is_valid_email("roha@gmail.com"))
    
print(user1.is_valid_email("roha"))
print(user1.is_valid_email("roha@gmail.com"))