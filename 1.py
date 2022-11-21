
def Base3Converter(n):
    if n < 3:
        return str(n)
    else:
        return Base3Converter(n // 3) + str(n % 3)

n = int(input())
print(Base3Converter(n))