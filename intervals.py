def Gamma(user, bs):
    G = {}

    n = len(user)
    m = len(bs)
    user.sort()
    bs.sort()
    i = j = 0
    G[0] = [0]
    while j < m:
        if user[i] < bs[j]:
            G[j].append(i+1)
            i += 1
        else:
            G[j+1] = G[j][-1:]
            j += 1
    G[0] = [0]
    del G[m]
    return G

if __name__ == '__main__':
    user = [3, 5, 6, 9, 12]
    bs = [4, 7, 10]
    G = Gamma(user, bs)
    from pprint import pprint
    pprint(G)
