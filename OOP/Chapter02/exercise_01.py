class User:
    pass 


print(type(User()))
print(type(2))
print(type("string"))
print(type([]))
print(type({}))
print(type(()))

def print_hello():
    pass

print(type(print_hello))

'''
파이썬은 순수 객체 지향 언어: 모든 것들이 객체로 되어있다. 
<class '__main__.User'>: __main__은 현재 실행중인 파일을 나타냄
<class 'int'>
<class 'str'>
<class 'list'>
<class 'dict'>
<class 'tuple'>
<class 'function'>
'''