def count_substring(string, sub_string):
    # cont = 0
    # quant_carac = len(string)
    # for _ in range(quant_carac):
    #     if sub_string in string:
    #         cont = cont + 1
    a = string.count(sub_string)
    return a


if __name__ == '__main__':
    string = input().strip()   # o .strip() é para separa o que foi digitado na primeira linha, da segunda
    sub_string = input().strip()
    # print(string)
    # print(sub_string)

    count = count_substring(string, sub_string)
    print(count)