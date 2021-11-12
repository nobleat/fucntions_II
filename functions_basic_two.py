# # 1

def countdown(start):
    return list(range(start, -1,-1))
print(countdown(5))

# # 2
def p_and_r(num):
    print(num[0])
    return num[1]
print(p_and_r([55,99]))

# #3
def first_sum(list):
    sum= len(list) + list[0]
    return sum
print(first_sum([55,16,5]))

#4---help
# def value_second(list):


# 5
def length_value(size,value):
    list = []
    for i in range(size):
        list.append(value)
    return list
print(length_value(5,3))