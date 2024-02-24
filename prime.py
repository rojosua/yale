def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


start = 2**33
end = start+50


for num in range(start, end+1):
    if is_prime(num):
        print(num, end=" ")