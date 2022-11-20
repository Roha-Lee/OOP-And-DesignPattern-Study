class User:
    # 클래스 변수
    count = 0
    
    # 매직 메소드, 특수 메소드: 특정 상황에서 자동으로 호출되는 메소드 
    # init은 객체가 생성될 때 자동으로 호출된다. 
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        User.count += 1
    
    def __str__(self):
        return "이메일: {}, 이름: {}, 비밀번호: ******".format(self.email, self.name)

# 인스턴스 생성과 초기화를 한 번에 할 수 있다.
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# 인스턴스 변수를 설정하면 클래스 변수보다 우선순위가 스코프가 더 좁다. (우선순위 높음)
# 클래스 변수를 설정할 때는 클래스 이름을 가지고 변경하는 것이 좋다. 
# user1.count = 5
User.count = 5

# 모든 유저의 수를 나타내는 변수 
print(User.count)
print(user1.count)
print(user2.count)
print(user3.count)
