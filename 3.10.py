sequence = 2
list_prime = [2]
number = 3
while sequence < 11:
    check = True
    for i in range(2, number):
        if number % i == 0:
            check = False
    
    if check == True:
        list_prime.append(number)
        number += 2
        sequence += 1
    else:
        number += 2

for i in range(len(list_prime)):
    list_prime[i] = str(list_prime[i])

print ', '.join(list_prime)