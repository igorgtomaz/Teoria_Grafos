# -*- coding: utf-8 -*-
import sys

# ==================================================================================
# Le a matriz de um arquivo

def catchMatriz(arquivo, tipo, nMatriz):
    # Endereco do arquivo
    arq = open(arquivo, 'r')
    entrada = arq.read()
    
    # Adiciona um 'ponto de parada' ao final do arquivo lido
    entrada += '\0'
    tam = len(entrada)
    i = 0
    matriz = []
    vet_linha = []
    len_mat_c = 0
    len_mat_l = 0
    entrada_quebrada = ''

    # Se o caracter for quebra de linha ou final, ele adiciona ao vetor
    while (i < tam):
        if (entrada[i] == '\n' or entrada[i] == '\0'):
            vet_linha.append(entrada_quebrada)
            entrada_quebrada = ''
        else:
            if (entrada[i] != '\r'):
                entrada_quebrada += entrada[i]
        i += 1

    # Separa os caracteres lidos pelo espaÃ§o ' '
    for i in range(len(vet_linha)):
        catch = vet_linha[i].split(' ')
        if (catch != ['']):
            matriz.append(catch)

    if tipo == 'Incidencia':
        len_mat_l = len(matriz)
        len_mat_c = len(matriz[0])
    else:
        len_mat_l = len(matriz)
        len_mat_c = len_mat_l

    # Transforma os caracteres lidos em inteiro
    for i in range(len_mat_l):
        for j in range(len_mat_c):
            matriz[i][j] = int(matriz[i][j])

    # Assim que terminado a matriz incidente será criado um menu
    print('==========================================================')
    print('Matriz ' + tipo + ' ' + nMatriz + '\n')
    for i in range(len(matriz)):
        print(matriz[i])

    arq.close

    return matriz

# ==================================================================================
# Retorna o maior valor

def maiorValor(vet_vertices):
    tam_vet = len(vet_vertices)
    maior_valor = 0

    for i in range(tam_vet):
        if (maior_valor < vet_vertices[i][2]):
            maior_valor = vet_vertices[i][2]

    return maior_valor

# ==================================================================================
# Trata o retorno da função

def trataRetorno(returnFun, nOp):
    Mensagem1 = ''
    Mensagem2 = ''

    returnFun = returnFun.replace('[','')
    returnFun = returnFun.replace(']','')
    returnFun = returnFun.replace("'",'')
    returnFun = returnFun.replace(",",'')
    returnFun = returnFun.split(' ')

    if nOp == 1:
        Mensagem1 += '(' + returnFun[0] + ', ' + returnFun[1] + '), '
        Mensagem1 += '(' + returnFun[2] + ', ' + returnFun[3] + '), '
        Mensagem1 += '(' + returnFun[4] + ', ' + returnFun[5] + ')'

        Mensagem1 = 'Caminho percorrido: ' + Mensagem1 + '.'
        Mensagem2 += 'Distancia: ' + returnFun[6] + 'km.'
    elif nOp == 2:
        Mensagem1 += '(' + returnFun[0] + ', ' + returnFun[1] + '), '
        Mensagem1 += '(' + returnFun[2] + ', ' + returnFun[3] + '), '
        Mensagem1 += '(' + returnFun[4] + ', ' + returnFun[5] + '), '
        Mensagem1 += '(' + returnFun[6] + ', ' + returnFun[7] + ')'

        Mensagem1 = 'Caminho percorrido: ' + Mensagem1 + '.'
        Mensagem2 += 'Distancia: ' + returnFun[8] + 'km.'
    elif nOp == 3:
        Mensagem1 += '(' + returnFun[0] + ', ' + returnFun[2] + '), '
        Mensagem1 += '(' + returnFun[2] + ', ' + returnFun[4] + '), '
        Mensagem1 += '(' + returnFun[4] + ', ' + returnFun[6] + '), '
        Mensagem1 += '(' + returnFun[6] + ', ' + returnFun[7] + ')'
        
        Mensagem1 = 'Caminho percorrido: ' + Mensagem1 + '.'
        Mensagem2 += 'Distancia: ' + returnFun[8] + 'km.'
    else:
        Mensagem1 += '(' + returnFun[0] + ', ' + returnFun[2] + '), '
        Mensagem1 += '(' + returnFun[2] + ', ' + returnFun[4] + '), '
        Mensagem1 += '(' + returnFun[4] + ', ' + returnFun[5] + ')'

        Mensagem1 = 'Caminho percorrido: ' + Mensagem1 + '.'
        Mensagem2 += 'Distancia: ' + returnFun[6] + 'km.'

    return [Mensagem1, Mensagem2]

# ==================================================================================
# Retorna o menor valor/aresta

def retAresta(vet_vertices, valor):
    tam_vet = len(vet_vertices)
    menor_valor = maiorValor(vet_vertices)
    pos_saida = 0
    pos_entrada = 0

    # Procura o menor valor dentre as ligações do vértice
    for i in range(tam_vet):
        if (vet_vertices[i][0] == valor):
            if (vet_vertices[i][2] <= menor_valor
                and vet_vertices[i][2] > 0):
                menor_valor = vet_vertices[i][2]
                pos_saida = vet_vertices[i][0]
                pos_entrada = vet_vertices[i][1]
    
    return([
        pos_saida,
        pos_entrada,
        menor_valor
    ])

# ==================================================================================
# Retorna o menor valor/aresta incidente

def retAresta_inc(vet_vertices, valor, coluna):
    tam_vet = len(vet_vertices)
    menor_valor = maiorValor(vet_vertices)
    pos_saida = 0
    pos_entrada = 0

    # Procura o menor valor dentre as ligações do vértice
    for i in range(tam_vet):
        if (vet_vertices[i][1] == coluna 
            and vet_vertices[i][2] == (valor*(-1))):
                pos_entrada = vet_vertices[i][0]
                break

    for i in range(tam_vet):
        if (vet_vertices[i][0] == pos_entrada
            and vet_vertices[i][2] > 0
            and  vet_vertices[i][2] <= menor_valor):
            menor_valor = vet_vertices[i][2]
            pos_saida = vet_vertices[i][1]

    return ([pos_entrada, pos_saida, menor_valor])
    


# ==================================================================================
# Procura vertice repetido

def procuraVertice(vet_vertices, vertice):
    tam_vet = len(vet_vertices)

    for i in range(tam_vet):
        if (vet_vertices[i][0] == vertice):
            return True
    
    return False

# ==================================================================================
# Soma o valor final

def somaValor(vetor):
    tam_vet = len(vetor)
    vetor_aux = []
    valor_final = 0

    for i in range(tam_vet):
        vetor_aux.append([vetor[i][0], vetor[i][1]])
        valor_final += vetor[i][2]

    return([vetor_aux, valor_final])

# ==================================================================================
# Matriz Adjacente

def mat_adj(vet_vertices, tam_vet, nOp):
    i = 0
    vet_final = []
    retorno = []
    valor = 1

    while (True):
        retorno = retAresta(vet_vertices, valor)
        valor = retorno[1]

        if ((procuraVertice(vet_final, valor)) == True) or (valor == 0):
            if (nOp == 1):
                for i in range(len(vet_final)):
                    if (vet_final[i][0] == 1):
                        vet_final[i][0] = 'Inicio'
                    elif (vet_final[i][1] == 7):
                        vet_final[i][1] = 'Objetivo'
                
                return somaValor(vet_final)
            else:
                return somaValor(vet_final)
        else:
            vet_final.append(retorno)

# ==================================================================================
# Matriz Incidente

def mat_inc(vet_vertices, tam_vet, nOp):
    valor = 1
    retorno = retAresta(vet_vertices, valor)
    prox_busca = retorno[1]
    valor = retorno[2]
    vet_final = []
    vet_final.append([retorno[0], retorno[1], retorno[2]])

    while (True):
        retorno = retAresta_inc(vet_vertices, valor, prox_busca)
        
        if ((procuraVertice(vet_final, retorno[1])) == True) or (retorno[0] == 0 or retorno[1] == 0):
            if (nOp == 1):
                for i in range(len(vet_final)):
                    if (vet_final[i][0] == 1):
                        vet_final[i][0] = 'Inicio'
                    elif (vet_final[i][1] == 7 or vet_final[i][1] == 8):
                        vet_final[i][1] = 'Objetivo'

                return somaValor(vet_final)
            else:
                return somaValor(vet_final)
        else:
            prox_busca = retorno[1]
            valor = retorno[2]
            vet_final.append([retorno[0], retorno[1], retorno[2]])

# ==================================================================================
# Main

def main():
    matriz_adj1 = catchMatriz('matriz1_adj.txt', 'Adjacencia', '1')
    matriz_inc1 = catchMatriz('matriz1_inc.txt', 'Incidencia', '1')
    matriz_adj2 = catchMatriz('matriz2_adj.txt', 'Adjacencia', '2')
    matriz_inc2 = catchMatriz('matriz2_inc.txt', 'Incidencia', '2')
    vet_mat1 = []
    vet_mat2 = []
    vet_mat3 = []
    vet_mat4 = []
    tam_matriz1 = len(matriz_adj1)
    tam_matriz2 = len(matriz_adj2)
    tam_linha_m3 = len(matriz_inc1)
    tam_coluna_m3 = len(matriz_inc1[0])
    tam_linha_m4 = len(matriz_inc2)
    tam_coluna_m4 = len(matriz_inc2[0])
    valor_caminho = 0
    retorno = ''

    # Cria o vetor de ligacoes existentes
    for i in range(tam_matriz1):
        for j in range(tam_matriz1):
            if (matriz_adj1[i][j] > 0):
                vet_mat1.append([(i+1), (j+1), matriz_adj1[i][j]])

    for i in range(tam_matriz2):
        for j in range(tam_matriz2):
            if (matriz_adj2[i][j] > 0):
                vet_mat2.append([(i+1), (j+1), matriz_adj2[i][j]])

    for i in range(tam_linha_m3):
        for j in range(tam_coluna_m3):
            if (matriz_inc1[i][j] != 0):
                vet_mat3.append([(i+1), (j+1), matriz_inc1[i][j]])
    
    for i in range(tam_linha_m4):
        for j in range(tam_coluna_m4):
            if (matriz_inc2[i][j] != 0):
                vet_mat4.append([(i+1), (j+1), matriz_inc2[i][j]])

    print('\n==========================================================')
    print('Grafo 1\n\n')

    retorno = str(mat_adj(vet_mat1, tam_matriz1, 0))
    retorno = trataRetorno(retorno, 2)

    print('Adjacencia:\n\n'+ retorno[0] + '\n' + retorno[1])

    retorno = str(mat_inc(vet_mat3, (tam_linha_m3 * tam_coluna_m3), 0))
    retorno = trataRetorno(retorno, 3)

    print('\nIncidencia:\n\n'+ retorno[0] + '\n' + retorno[1])

    print('==========================================================')
    print('Grafo 2\n\n')

    retorno = str(mat_adj(vet_mat2, tam_matriz2, 1))
    retorno = trataRetorno(retorno, 1)

    print('Adjacencia:\n\n'+ retorno[0] + '\n' + retorno[1])

    retorno = str(mat_inc(vet_mat4, (tam_linha_m4 * tam_coluna_m4), 1))
    retorno = trataRetorno(retorno, 4)

    print('\nIncidencia:\n\n'+ retorno[0] + '\n' + retorno[1])
    print('==========================================================')

# ==================================================================================
# Execucao

main()