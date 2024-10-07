# first = input(int())
# second = input(int())
# third = input(int())
# if first == second and first == third:
#     print(first,second,third)
# elif first == second:
#     print(first,second)
# elif first == third:
#     print(first,third)
# elif second == third:
#     print(second,third)
# else:
#     print('Uvolen')

# first = input(int())
# second = input(int())
# third = input(int())
# if first == second == third:
#     print(3)
# elif first == second or first == third or second == third:
#     print(2)
# else:
#     print(0)

# first = int(input())
# second = int(input())
# third = int(input())
# if first == second == third:
#     print(3)
# elif first == second or first == third or second == third:
#     print(2)
# else:
#     print(0)

first = int(input('1 Input: '))
second = int(input('2 Input: '))
third = int(input('3 Input: '))
if first == second == third:
    print('matches: 3')
elif first == second or first == third or second == third:
    print('matches: 2')
else:
    print('matches: 0')