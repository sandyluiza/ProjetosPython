def print_formatted(number):
    for x in range(1, number+1):
        f = (bin(number))[2:]
        a = str(x)
        b = (oct(x))[2:]
        c = (hex(x))[2:]
        g = c.upper()
        d = (bin(x))[2:]
        e = len(f)
        print('{} {} {} {}'.format(a.rjust(e), b.rjust(e), g.rjust(e), d.rjust(e)))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)