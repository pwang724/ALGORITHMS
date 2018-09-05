# add x and y
def add(x, y):
    lx = len(x)
    ly = len(y)
    if lx > ly:
        for i in range(lx - ly):
            y.insert(0, 0)
    else:
        for i in range(ly - lx):
            x.insert(0,0)

    result = []
    carry = 0
    for i in reversed(range(len(x))):
        out = x[i] + y[i] + carry
        rem = out % 10
        carry = out // 10
        result.insert(0, rem)
    if carry:
        result.insert(0, carry)
    return result

# multiply single digit number num with list y
def multiply(num, y):
    result = []
    carry = 0
    for i in reversed(range(len(y))):
        out = num * y[i]
        rem = out % 10
        assert(rem + carry < 10)
        result.insert(0, rem + carry)
        carry = out // 10
    if carry:
        result.insert(0, carry)
    return result

# shift list y with i zeros
def shiftzeros(y, i):
    for j in range(i):
        y.append(0)

def mult(x,y):
    result = []
    for i in reversed(range(len(x))):
        num = x[i]
        z = multiply(num, y)
        shiftzeros(z, len(x) - i - 1)
        result = add(z, result)
    return result


print(mult([1, 3, 9, 9, 7],[9, 9, 9]), 13997 * 999)