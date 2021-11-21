# def power(a, b):
#     if b == 0:
#         return 1
#     else:
#         half_result = power(a, b//2)
#         if b % 2 == 0:
#             return half_result * half_result
#         else:
#             return half_result * half_result * a

# if __name__ == "__main__":
#     assert power(2, 4) == 16
#     assert power(2, 5) == 32
#     assert power(2, 1) == 2
#     assert power(2, 0) == 1