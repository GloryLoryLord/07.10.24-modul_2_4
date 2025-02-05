# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
#
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         not_primes.append(i)
#     if i % 2 > 0:
#         primes.append(i)
# print('primes: ',primes)
# print('not_primes: ', not_primes)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    if num < 2:
        continue
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

print('primes: ',primes)
print('not_primes: ', not_primes)