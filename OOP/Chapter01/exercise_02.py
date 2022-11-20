class User:
    # instance method
    def say_hello(self):
        # 인사 메시지 출력 메소드 
        print("Hello My name is {}".format(self.name)) 
        
    def login(self, my_email, my_password):
        # 로그인 메소드
        if (self.email == my_email and self.password == my_password):
            print("로그인 성공, 환영합니다")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호 입니다.")
            
    def check_name(self, name):
        # 이름을 확인하여 불린으로 반환하는 메소드
        return self.name == name

user1 = User()
user2 = User()
user3 = User()

# instance variable
user1.name = "Roha"
user1.email = "rohagru@gmail.com"
user1.password = "12345"

user2.name = "Roha2"
user2.email = "rohagru2@gmail.com"
user2.password = "12345"

user3.name = "Roha3"
user3.email = "rohagru3@gmail.com"
user3.password = "12345"

# 인스턴스 메소드 사용
User.say_hello(user1)
User.say_hello(user2)
User.say_hello(user3)

# 인스턴스 메소드를 사용하는 다른 방법 - 첫번째 파라미터로 user1, user2, user3이 각각 전달된다. 
user1.say_hello()
user2.say_hello()
user3.say_hello()

user1.login("rohagru@gmail.com", "12345")