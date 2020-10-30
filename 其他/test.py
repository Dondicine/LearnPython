# test.py
# import sys

# if __name__ == "__main__":
#     print(sys.path)

# a = int(input("get a number:"))

# print(a**2)

a = int(input("输入多少行："))

for i in range(1, a + 1):
    print("{}{}".format(" " * (a - i), "*" * (2 * i - 1)))
