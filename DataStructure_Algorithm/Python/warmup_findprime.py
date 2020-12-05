# find prime number
def is_prime(value):
    if value <= 1:
        return False
    else:
        for num in range(2, int(value**0.5 + 1)):
            if value % num == 0:
                return False
        return True

if __name__ == "__main__":
    for i in range(-10, 26):
        print(i, is_prime(i))