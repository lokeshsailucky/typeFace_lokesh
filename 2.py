
def occur(x, y):
    c = 0
    l = [i for i in x if i == y[-1]]
    return len(l)

x = input()
y = input()
print(occur(x, y))