# def range_like(from_, to_):
#     print(from_)
#     if from_ >= to_:
#         return
#     range_like(from_ + 1, to_)
#
# range_like(1, 10)
# print()
#
# def jump_to_to (start, final, jump=0):
#     print(start)
#     if start+jump >= final:
#         return
#     jump_to_to(start + jump, final, jump)
#
# jump_to_to(8,15,3)

#
# def factorial(num:int):
#     if num == 0 or num == 1:
#         return 1
#     return num * factorial (num - 1)
#
#
# print(factorial(5))

# def digit_sum(num):
#     if num == 0:
#         return 0
#     return num % 10 + digit_sum(num//10)
#
# print(digit_sum(45))

# def num_in_list(list:list, num:int):
#     counter = 0
#     if len(list) == 0:
#         return 0
#     if num in list:
#         num_in_list(list, num)
#         counter+=1
#         return counter

def num_in_list(list: list, num: int) -> int:
    if len(list) == 0:
        return 0
    if list[0] == num:
        return 1 + num_in_list(list[1:], num)
    return num_in_list(list[1:], num)

print(num_in_list([8,5,5,3,5,5],5))
