import json
import time


# Função de leitura de txt como JSON em vetor
# Utilizar com o arquivo songs3JSONvector.txt
def ler_vetor(nome):
    with open(nome, 'rb') as arquivo:
        return json.loads(arquivo.read())


# Função de leitura de txt como JSON linha a linha
# Utilizar com o arquivo songs3LineByLine.txt
def ler_linha(nome):
    return [json.loads(line) for line in open(nome, 'rb')]


# Função de carregamento do conteúdo do txt para um vetor
# Caso utilizar o arquivo songs3JSONvector.txt, alterar
# ler_linha por ler_vetor
def carregar_arquivo(nome):
    vet = []
    for i in ler_linha(nome):
        dado = {
            'arq': i['arq'],
            'ordem': i['ordem'],
            'notas': i['notas']
        }
        vet.append(dado)
    return vet


# Função que reúne as infos de cada arquivo em um txt
def separar_arquivos(vet):
    for i in vet:
        nome = 'arq_' + str(i.get('arq')) + '.txt'
        arquivo = open('./saida/temp/' + nome, 'a')
        arquivo.write(str(i).replace("'", '"') + '\n')


# Função que encontra o menor valor de um determinado tipo no vetor
def menor_valor(vet, tipo):
    menor = vet[0].get(tipo)
    for i in vet:
        if i.get(tipo) < menor:
            menor = i.get(tipo)
    return menor


# Função que encontra o maior valor de um determinado tipo no vetor
def maior_valor(vet, tipo):
    maior = vet[0].get(tipo)
    for i in vet:
        if i.get(tipo) > maior:
            maior = i.get(tipo)
    return maior


# Função que verifica a existência no vetor
def existe(arq, vet):
    for i in vet:
        if str(i.get('arq')) == arq:
            return True
    return False


# Algoritmo de ordenação Counting Sort
def counting_sort(vet_entrada, maior_valor):
    # Array auxiliar de contagem inicializado em
    # 0s para armazenar a quantidade de ocorrências
    # de cada elemento de vet_entrada
    count_vet_tam = maior_valor + 1
    count_vet = [0] * count_vet_tam

    # Etapa 1 -> Percorre o vet_entrada e incrementa
    # a contagem de cada elemento em 1 (equivale ao
    # índice do elemento no vet_saida)
    for el in vet_entrada:
        count_vet[el.get('ordem')] += 1

    # Etapa 2 -> Para cada elemento no count_vet, soma
    # o seu valor com o valor do elemento anterior a ele
    # e armazena como o valor do elemento atual
    for i in range(1, count_vet_tam):
        count_vet[i] += count_vet[i - 1]

    # Etapa 3 -> Calcula a posição do elemento com base
    # nos valores contidos em count_vet
    vet_saida = [0] * len(vet_entrada)  # encontra o valor do el atual
    i = len(vet_entrada) - 1  # subtrai 1 do valor
    while i >= 0:  # realiza a operação com todos os elementos
        pos_atual = vet_entrada[i]
        count_vet[pos_atual.get('ordem')] -= 1
        pos_nova = count_vet[pos_atual.get('ordem')]
        vet_saida[pos_nova] = pos_atual
        i -= 1

    return vet_saida  # contém os elementos de vet_entrada ordenados


# Função que reúne as infos de cada arquivo em um txt
def reescrever_arquivos(vet, num_arq):
    for i in vet:
        nome = 'song_' + num_arq + '.abc'
        arquivo = open('./saida/' + nome, 'a')
        arquivo.write(str(i.get('notas')) + '\n')


# Função principal main
if __name__ == '__main__':
    print(
        '\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
        '\n*              > MISSÃO CANÇÃO DO VECNA INICIALIZADA <              *'
        '\n* Bem vindo, amigo! Vamos juntos derrotar o Vecna com a computação! *'
        '\n* Vamos decifrar as músicas e salvar a cidade de uma vez por todas! *'
        '\n*               > INICIANDO EXECUÇÃO DO PROGRAMA... <               *'
        '\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
    )

    # Captura o tempo de início da execução
    inicio = time.time()

    # Carrega as informações do arquivo txt de entrada para um vetor
    vet_dados = carregar_arquivo('./entrada/songs3LineByLine.txt')
    print('* > Arquivo de músicas embaralhadas carregado                       *')

    # Separa as músicas em arquivos próprios
    separar_arquivos(vet_dados)
    print('* > Músicas separadas por arquivos                                  *')

    # Carrega as informações de cada arquivo em um vetor temporário,
    # ordena com Counting Sort e gera arquivo de música final
    for i in range(menor_valor(vet_dados, 'arq'), maior_valor(vet_dados, 'arq') + 1):
        if existe(str(i), vet_dados):
            nome = './saida/temp/arq_' + str(i) + '.txt'
            vet_temp = carregar_arquivo(nome)
            vet_ordenado = counting_sort(vet_temp, maior_valor(vet_temp, 'ordem'))
            reescrever_arquivos(vet_ordenado, str(i))
    print('* > Linhas ordenadas e músicas ABC geradas                          *')

    # Captura o tempo de fim da execução e exibe o tempo total
    # de execução do programa
    fim = time.time()
    print(
        '*                 > TEMPO DE EXECUÇÃO:', round(fim - inicio), 'SEGUNDOS <                *'
                                                                       '\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
    )
