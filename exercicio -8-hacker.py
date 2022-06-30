# como fazer um número criptografado
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_list = tuple(integer_list)
    print(integer_list)
    print(hash(integer_list))  #hash é para criar tipo uma criptografia do resultado