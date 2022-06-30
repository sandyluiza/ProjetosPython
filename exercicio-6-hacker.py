#trabalhando com dicionario e notas de alunos
if __name__ == '__main__':
    # essa parte formou a lista
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(student_marks)
    print(n)
    print(query_name)
    notas = sum(student_marks[query_name])/3
    print('{:.2f}'.format(notas))

    # student_marks=list(student_marks)
    # print(student_marks)
    # for x in range(n):
    #     alunos.append(student_marks[0])
    #     student_marks.pop(0)
    # print(alunos)
    # print(student_marks)

    # calcular a média do nome escolhido
