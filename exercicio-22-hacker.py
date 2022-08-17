def merge_the_tools(string, k):
    n = len(string)
    # print(n)
    # divisao_elementos = int(n/k)
    for x in range(0, n, k):
        a = k+x
        substring = string[x:a]
        print(substring)
        new = ''
        for i in substring:
            if i not in new:
                new+=i
        # print(new)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)