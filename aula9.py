# parametro "w" gera e substitui o arquivo
# parametro "a" atualiza texto ao arquivo
import shutil

def escrever_arquivo(texto):
    diretorio = 'C:/Users/bruno/Documents/teste.txt'
    arquivo = open(diretorio,'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo,'a')
    arquivo.write(texto)
    arquivo.close()
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    texto = arquivo.read()
    print(texto)
def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        #print(aluno)
        #print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        lista_media.append({aluno:media(lista_notas)})
        #print(media(lista_notas))
    return lista_media


def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo,'C:/Users/bruno/Documents/copia.txt')

def mover_arquivo(nome_arquivo):
    shutil.move(nome_arquivo,'C:/Users/bruno/Documents/')

if __name__ == '__main__':
    #escrever_arquivo('Primeira linha. \n')
    #atualizar_arquivo('Terceira linha. \n')
    #escrever_arquivo('arquivo txt em documentos \n')
    #aluno = 'Cesar,8,9,10,9\n'
    #atualizar_arquivo('notas.txt',aluno)
    #ler_arquivo('notas.txt')
    print(media_notas('notas.txt'))
    mover_arquivo('teste.txt')