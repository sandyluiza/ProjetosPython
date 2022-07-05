import textwrap
import sys

def wrap(string, max_width):
    # b = []
    v = int(len(string))
    # print(v)

    # a = string[b:max_width]
    # b = 0
    x = 0
    # i = 0
    c = max_width
    # print(a)
    for _ in string:
        # for _ in range(0, v):
        a = string[x:c]
        # return \
        if x > v:
            return a
        print(a)
        # sys.stdout.write(a)
        # return (a)
        # b.append(a)
            # b = (max_width+1)*x
        x += max_width
        # print(x)
            # print(b)
            # b = x
            # print(b)
        c = c+max_width
        # print(c)
            # c = string[b:d]
            # a = a.append(d)

            # a = string[b:max_width]
            # x += max_width
            # print(a)
        # print(c)
    # for i in b:
    #     if b[i] != ['']:
    #         print(b[i])
    # return b
    # return

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)