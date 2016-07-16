from intervals import Gamma
from coloring import color

user = [3, 5, 6, 9, 8, 8.5, 8.6, 8.7, 12]
bs = [4, 7, 10, 13]
intervals = Gamma(user, bs)

n = len(user)
m = len(bs)

def u(i):
    return user[i - 1]

def b(i):
    return bs[i - 1]

def G(i):
    return intervals[i]

def arrow(bsp, usp):
    head = usp
    tail = 2 * bsp - usp
    return (tail, head)

def C(i, x, y, z):
    arrows = [arrow(b(i), u(j)) for j in range(x+1, y+1)]
    arrows.extend([arrow(b(i+1), u(j)) for j in range(y+1, z+1)])
    return color(arrows)

M = {}
D = {}
def X(a, b, c):
    if a == 1 and b == 0:
        return c
    if a == 1 and b != 0:
        print("Error!")
        import sys
        sys.exit(0)
    if (a, b, c) in M:
        return M[a, b, c]
    else:
        # M[a, b, c] = min([max(X(a-1, x, b), C(a-1, x, b, c)) for x in G(a-2)])

        minx = 10000
        minVal = 10000
        for x in G(a-2):
            if max(X(a-1, x, b), C(a-1, x, b, c)) < minVal:
                minVal = max(X(a-1, x, b), C(a-1, x, b, c))
                minx = x
        D[a-2] = x
        M[a, b, c] = minVal

        return M[a, b, c]

def solve():
    # ans = min([X(m, x, n) for x in G(m-1)])

    minx = 10000
    minX = 10000
    for x in G(m-1):
        if X(m, x, n) < minX:
            # do something
            minX = X(m, x, n)
            minx = x
    D[m-1] = minx

    ans = minX
    print("colors: " + str(ans))
    print("DPs: " + str(D))

if __name__ == '__main__':
    # print(C(1, 0, 1, 4))
    solve()
