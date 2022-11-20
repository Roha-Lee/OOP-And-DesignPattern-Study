# 클래스 메소드 연습하기 

class User:
    count = 0
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        User.count += 1
    
    def __str__(self):
        return "이메일: {}, 이름: {}, 비밀번호: ******".format(self.email, self.name)
    
    # # 클래스 메소드의 첫번째 인자는 cls를 적는 것을 규칙으로 한다. 
    # # cls는 유저 클래스를 나타낸다. 
    # @classmethod
    # def number_of_users(cls):
    #     print("총 유저 수는 {}입니다.".format(cls.count))
    
    def number_of_users(self):
        print("총 유저 수는 {}입니다.".format(User.count))    
        

user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

User.number_of_users(user1)
user1.number_of_users()

'''
인스턴스 메소드 사용 
User.say_hello(user1)
user1.say_hello()

클래스 메소드 사용 
User.number_of_users()
user1.number_of_users()
'''