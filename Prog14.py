def is_Power_of_two(n):
        return n > 0 and (n & (n - 1)) == 0
print(is_Power_of_two(4))
print(is_Power_of_two(36))
print(is_Power_of_two(16))