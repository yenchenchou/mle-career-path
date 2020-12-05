# find prime number
def is_composite(value):
    if value <= 1:
        return False
    for num in range(2, value):
        if value % num == 0:
            return True
    return False


if __name__ == "__main__":
    for i in range(1, 29):
        print(i, is_composite(i))
