def mini(a, b):
    if a < b:
        return a
    else:
        return b

def minimaln(a, b, c, d):
    return mini(mini(a, b), mini(c, d))

line = input().split(' ')
print(minimaln(int(line[0]), int(line[1]), int(line[2]), int(line[3])))



