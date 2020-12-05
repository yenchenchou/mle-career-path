# find prime number
def is_perfect(value):
    if value <= 0:
        return False

    factor_sum = 0
    for num in range(1, value):
        if value % num == 0:
            factor_sum += num

    return factor_sum == value

if __name__ == "__main__":
    for i in range(1, 29):
        print(i, is_perfect(i))
