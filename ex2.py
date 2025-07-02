lista=[('jonas',3), ('joão',5), ('maria',7), ('robson',1), ('julio',2), ('julia',7)]


def frequencia(*args):
    alunos = args[0]
    frequentes=[]
    a=0
    b=0
    for _ in alunos:
        if alunos[a][1] >=3 and alunos[a][1] <=7:
            frequentes.append(alunos[a][0]+ ' -Ativo')
        a+=1
    for _ in frequentes:
        print(frequentes[b])
        b+=1
    



frequencia(lista)

