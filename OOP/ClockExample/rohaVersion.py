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
 

# 초가 60이 넘을 때 분이 늘어나는지 확인하기
print("시간을 1시 30분 48초로 설정합니다")
clock = Clock(1, 30, 48)
print(clock)

# 13초를 늘린다
print("13초가 흘렀습니다")
for i in range(13):
    clock.tick()
print(clock)

# 분이 60이 넘을 때 시간이 늘어나는지 확인
print("시간을 2시 59분 58초로 설정합니다")
clock.set(2, 59, 58)
print(clock)

# 5초를 늘린다
print("5초가 흘렀습니다")
for i in range(5):
    clock.tick()
print(clock)

# 시간이 24가 넘을 때 00:00:00으로 넘어가는 지 확인
print("시간을 23시 59분 57초로 설정합니다")
clock.set(23, 59, 57)
print(clock)

# 5초를 늘린다
print("5초가 흘렀습니다")
for i in range(5):
    clock.tick()
print(clock)