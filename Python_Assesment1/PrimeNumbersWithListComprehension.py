def generate_primes():
    for num in range(2, 100):  # Start from 2 because 1 is not a prime number
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to the square root of num
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

generate_primes()
