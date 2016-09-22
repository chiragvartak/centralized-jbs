"""Solve the JBS problem using the Centralized Algorithm based on Dynamic Programming."""

from intervals import Gamma
from coloring import color

# Input the user list and the basestation list here.
user = [3, 6, 7, 9, 12]
bs = [2, 5, 8, 11, 14]

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

# Theoretical check done - working correctly
def C(i, x, y, z):
    arrows = [arrow(b(i), u(j)) for j in range(x+1, y+1)]
    arrows.extend([arrow(b(i+1), u(j)) for j in range(y+1, z+1)])
    return color(arrows)

M = {}
D = {}
def X(a, b, c):
    ans = None
    if a == 1 and b == 0:
        ans = c
    elif a == 1 and b != 0:
        print("Error!")
        import sys
        sys.exit(0)
    elif (a, b, c) in M:
        ans = M[a, b, c]
    else:
        # M[a, b, c] = min([max(X(a-1, x, b), C(a-1, x, b, c)) for x in G(a-2)])

        minx = 10000
        minVal = 10000
        for x in G(a-2):
            X_val = X(a-1, x, b)
            cols = C(a-1, x, b, c)
            if max(X_val, cols) < minVal:
                minVal = max(X_val, cols)
                minx = x
        D[a-2] = minx
        M[a, b, c] = minVal

        ans = M[a, b, c]

    # print("a", a, "b", b, "c", c, "X", ans)
    return ans

def solve():
    # ans = min([X(m, x, n) for x in G(m-1)])

    minx = 10000
    minX = 10000
    for x in G(m-1):
        X_val = X(m, x, n)
        if X_val < minX:
            # do something
            minX = X_val
            minx = x
    D[m-1] = minx

    ans = minX
    print("colors: " + str(ans))
    print("DPs: " + str(D))
    for i in range(1, m):
        print("BS at posn", b(i), "serves users at", [u(i) for i in range(D[i-1]+1, D[i]+1)])
    print("BS at posn", b(m), "serves users at", [u(i) for i in range(D[m-1]+1, n+1)])

if __name__ == '__main__':
    # print(C(1, 0, 1, 4))
    solve()
