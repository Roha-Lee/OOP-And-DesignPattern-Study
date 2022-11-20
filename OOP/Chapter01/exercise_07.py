# using decorator
def add_print_to(original):
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")
    return wrapper

def print_hello():
    print("안녕하세요!")

@add_print_to    
def print_hello2():
    print("안녕하세요!")

print_hello = add_print_to(print_hello)
print_hello()

print_hello2()