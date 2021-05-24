import shutil

def escreverArquivo(texto):
    arquivo = open('teste.txt','w')
    arquivo.write(texto)
    arquivo.close()

def atualizarArquivo(nomeArquivo, texto):
    arquivo = open(nomeArquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo,'r')
    texto = arquivo.read()
    print(texto)

def mediaNotas(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    alunoNota = arquivo.read()
    # print(alunoNota)
    alunoNota = alunoNota.split('\n')
    # print(alunoNota)
    listaMedia = []
    for x in alunoNota:
        listaNotas = x.split(',')
        aluno = listaNotas[0]
        listaNotas.pop(0)
        print(aluno)
        print(listaNotas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(listaNotas))
        listaMedia.append({aluno: media(listaNotas)})
    return listaMedia

def copiaArquivo(nomeArquivo):
    shutil.copy(nomeArquivo, 'C:/Users/Lucas/RodrixProjects/aula_python/files/')

def moveArquivo(nomeArquivo):
    shutil.move(nomeArquivo, 'C:/Users/Lucas/RodrixProjects/aula_python/files/')

if __name__ == '__main__':
    moveArquivo('notas.txt')
    # copiaArquivo('notas.txt')
    # listaMedia = mediaNotas('notas.txt')
    # print(listaMedia)
    # atualizarArquivo('medias.txt', str(listaMedia))
    # escreverArquivo('Primeira linha')
    # aluno = 'Andreas, 10,8,10,9\n'
    # lerArquivo('teste.txt')