'''
mutable: 한번 생성한 인스턴스의 속성을 변경 가능 - list
immutable: 한번 생성한 인스턴스의 속성을 변경할 수 없음 - tuple
'''
list_var = [1, 2, 3]
tuple_var = (1, 2, 3)

list_var[0] = 4
tuple_var[0] = 4 # error! - immutable

# tuple을 새로 생성해서 할당하는 것은 가능
tuple_x = (6, 4)
tuple_x = (4, 6)
