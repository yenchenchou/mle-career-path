# find prime number
def is_abundant(value):
    sum_num = 0
    if value <= 0:
        return False
    for num in range(1, value):
        if value % num == 0:
            sum_num += num
    return sum_num > value


if __name__ == "__main__":
    for i in range(1, 29):
        print(i, is_abundant(i))
