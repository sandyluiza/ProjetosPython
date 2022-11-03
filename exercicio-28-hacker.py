# print(set(enumerate(['H', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k'])))

def average(array, n):
    media = round((sum(array))/n, 3)
    return media

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # o map aplica uma função em cada elemento da lista.
    # nesse caso, ele está transformando cada elemento da lista em inteiro
    result = average(arr, n)
    print(result)