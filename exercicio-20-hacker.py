def solve(s):
    c = s.split(' ')
    e = []
    g = len(c)
    for x in range(g):
        d = c[x]
        b = d.capitalize()
        e.append(b)
    f = ' '.join(e)
    return f

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
