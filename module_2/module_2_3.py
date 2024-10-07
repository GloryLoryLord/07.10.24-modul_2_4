# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# while True:
#     if len(my_list[0]) % 1 > 0:
#         print(my_list[0])
#         break

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

i = 0

while i < len(my_list):
    if my_list[i] < 0:
        break

    if my_list[i] > 0:
        print(my_list[i])

    i += 1


