# Short 1
# def name():
#     name = input("Name goes here ")
#     return name

# def subject():
#     subject = input("Subject goes here ")
#     return subject

# print(f"{name()} favorite subject is {subject()}")

# Short 2
# def CtF():
#     C = int(input("Place the temperature here, in C "))
#     return (C * 9/5) + 32

# print(CtF())       

# # Short 3
# def FtC():
#     F = int(input("Place your temperature in F "))
#     return (F-32) * 5/9

# print(FtC())

#4 Short 4
# def if_even():
#     x = int(input("Is your # divisible by 2?"))
#     if x / 2 == 1:
#         print('True')
#         return True   
#     else:
#         print('False')
#         return False

# if_even()

#5 Short 5 Write an is_odd function that uses your is_even function to determine if a number is odd. 
# (That is, do not do the calculation - call a function that does the calculation.)
# Hint: You'll use the not keyword

# def if_even():
#     x = int(input("Pick a number, any number "))
#     if x % 2 == 1:
#         print('True')
#         return True   
#     else:
#         print('False')
#         return False

# def if_odd(if_even):
#     if if_even() == True:
#             print("Odd")
#     else:
#         if_even() == False
#         print("Even")

# if_odd(if_even)


#6 Only Evens

# only_evens = ([11, 20, 42, 97, 23, 10])

# def if_even(x):
#     for x in only_evens:
#         if x % 2 == 0: 
#             print("True")
#         else:
#             print("False")

# print(if_even(x))


# # Medium
# """1. Find the smallest number
# Write a function smallest that accepts a List of numbers as an argument.
# It should return the smallest number in the List."""

# Min
# myList = [1,2,3,4,5,6,7,8,9]

# def FindMin():
#     number = min(myList)
#     return number
# print("the smallest is:", FindMin())

"""How to do it without built in functions"""
# myList = [5,8,3,4,2]
# def smallestZ(myList):
#     smallest = myList[0]
#     for num in myList:
#         if smallest > num:
#             smallest = num
#     print(smallest)
# smallestZ(myList)

"""Another Example"""
# def large(x):
#     y = x[0]
#     for i in x:
#         if i > y:
#             y = i
 
#     return(y)
# print(large( [2,3,4,55, 1,6]))

"""Another Example"""
# list_o_strings = ['hello', 'goodbye', 'Kearney', 'let\'s go!', 'Ohio State', 'more', 'lesson', 'help!']
# def shortest(string_list):
#     shortest_str = string_list[0]
#     for each_string in string_list:
#         if len(each_string) < len(shortest_str):
#             shortest_str = each_string            
#     return shortest_str
# print(f'Your list of strings is: {list_o_strings}')
# print(f'The shortest string in your list is: {shortest(list_o_strings)}')


# # # Max
# myList = [1,2,3,4,5,6,7,8,9]

# def FindMax():
#     myList = [1,2,3,4,5,6,7,8,9]
#     number = max(myList)
#     return number
# print("the largest is:", FindMax())

# Strings Short
# def ShortString():
#     strings = ["hey", "now", "you're", "an", "all-star", "go", "play"]
#     lilstring = min(strings, key=len)
#     return lilstring
# print(ShortString())

# # # #Srings Long
# def LongString():
#     strings = ["hey", "now", "you're", "an", "all-star", "go", "play"]
#     bigstring = max(strings, key=len)
#     return bigstring
# print (LongString())