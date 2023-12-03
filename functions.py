# def add_num(num1, num2, num3):
#     sum_num = num1 + num2 + num3
#     return sum_num
# print(add_num(2, 4, 7))

def simple_sum(a, c, b=2):
    print(f"a is {a}")
    print(f"b is {b}")
    print(f"c is {c}")
    result = a + b + c
    print(result)
# simple_sum(3,7)

def simple_sum_pro_max(a, c, d, b):
    print(f"a is {a}")
    print(f"b is {b}")
    print(f"c is {c}")
    print(f"d is {d}")
    result = a + b + c + d
# simple_sum_pro_max(1, 2, 3, 4)

def welcoming(customer_name, business_name):
    print(f"Hello {customer_name}, welcome to {business_name}. how can we help you today?")

# result = welcoming("Precious", "ShopiaDeck")
# print(result)

adder = lambda x: x+5
# print(adder(10))
multiplier = lambda x, y: x*y
# print(multiplier(3, 6))

puzzle = lambda x: x if x%2 == 0 else -99
# print(puzzle(8))

def puzzle(x):
    return x if x%2 == 0 else -99
# print(puzzle(4))

def puzzle(data):
    return [(data[0][::-1])]
   
# print(puzzle(data=[(10,5)]))


# def puzzle(data):
#     return [(x[1], x[0]) for x in data]
# print(puzzle(data=[(10,5), (2,5), (5,6)]))
base = [(10,5)]
# bs = []
# for element in base:
#     bs.append(element[::-1])
# print(bs)
bs = [element[::-1] for element in base]
# print(bs)

def reverse_item(input_list):
    return [element[::-1] for element in input_list]
# print(reverse_item(base))

# print(''.join(list(reversed('123'))))

def hello_func(greeting, name = 'Precious'):
    return f"{greeting} {name}"
# print(hello_func('Hi, Hello', name = 'Moses'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
courses = ['Math', 'Art']
info = {'name': 'John', 'Age': 22}
student_info(*courses, **info)