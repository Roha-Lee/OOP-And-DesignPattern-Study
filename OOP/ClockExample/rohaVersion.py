class Clock:
    @staticmethod
    def seconds_to_hms(seconds):
        hour = seconds // 3600
        remainder = seconds % 3600
        minute = remainder // 60
        second = remainder % 60
        return hour, minute, second
    
    @staticmethod
    def hms_to_seconds(hour, minute, second):
        return hour * 60 * 60 + minute * 60 + second
    
    def __init__(self, hour, minute, second):
        self.seconds = Clock.hms_to_seconds(hour, minute, second)
    
    def __str__(self):
        hour, minute, second = Clock.seconds_to_hms(self.seconds)
        return "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    
    def tick(self):
        self.seconds = (self.seconds + 1) % (60 * 60 * 24)
    
    def set(self, hour, minute, second):
        self.seconds = Clock.hms_to_seconds(hour, minute, second)

# 1시 30분 48초인 시계 인스턴스 생성
clock = Clock(1, 30, 48)
    
# 13초를 늘린다
for i in range(13):
    clock.tick()
    
# 시계의 현재 시간 출력
print(clock)
    
# 2시 3분 58초로 시계 세팅
clock.set(2, 3, 58)
    
# 5초를 늘린다
for i in range(5):
    clock.tick()
    
# 시계의 현재 시간 출력
print(clock)
    
# 23시 59분 57초로 세팅
clock.set(23, 59, 57)
    
# 5초를 늘린다
for i in range(5):
    clock.tick()
    
# 시계의 현재 시간 출력
print(clock)