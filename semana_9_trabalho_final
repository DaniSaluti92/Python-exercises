import re
import math

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

#parametros de assinatura#

def tamanho_medio_palavras(texto):
    sentencas=separa_sentencas(texto)
    comprimento=len(sentencas)
    a=0
    total_palavras=0
    total_caracteres=0
    while (a<comprimento):
        sentenca=sentencas[a]
        frases=separa_frases(sentenca)
        comprimento_lista=len(frases)
        b=0
        while (b<comprimento_lista):
            frase=frases[b]
            palavras=separa_palavras(frase)
            n_palavras=len(palavras)
            total_palavras=total_palavras+n_palavras
            c=0
            while (c<n_palavras):
                palavra=palavras[c]
                caracteres=len(palavra)
                total_caracteres=total_caracteres+caracteres
                c=c+1
            b=b+1
        a=a+1
    tamanho_medio=(total_caracteres/total_palavras)
    return(tamanho_medio)


def relacao_type_token(texto):
    sentencas=separa_sentencas(texto)
    comprimento=len(sentencas)
    a=0
    total_palavras=0
    total_palavras_diferentes=0
    palavras_totais_lista=[]
    palavras_lista_unica=[]
    
    while (a<comprimento):
        sentenca=sentencas[a]
        frases=separa_frases(sentenca)
        comprimento_lista=len(frases)
        b=0
        while (b<comprimento_lista):
            frase=frases[b]
            palavras=separa_palavras(frase)
            palavras_totais_lista.append(palavras)
            n_palavras=len(palavras)
            total_palavras=total_palavras+n_palavras
            b=b+1
        a=a+1
    for item in palavras_totais_lista:
        for i in item:
            palavras_lista_unica.append(i)
    palavras_diferentes=n_palavras_diferentes(palavras_lista_unica)
    relacao=palavras_diferentes/total_palavras
    return relacao

def razao_hapax_legomana(texto):
    sentencas=separa_sentencas(texto)
    comprimento=len(sentencas)
    a=0
    total_palavras=0
    total_palavras_unicas=0
    palavras_totais_lista=[]
    palavras_lista_unica=[]
    while (a<comprimento):
        sentenca=sentencas[a]
        frases=separa_frases(sentenca)
        comprimento_lista=len(frases)
        b=0
        while (b<comprimento_lista):
            frase=frases[b]
            palavras=separa_palavras(frase)
            palavras_totais_lista.append(palavras)
            n_palavras=len(palavras)
            total_palavras=total_palavras+n_palavras
            b=b+1
        a=a+1
    for item in palavras_totais_lista:
        for i in item:
            palavras_lista_unica.append(i)
    palavras_unicas=n_palavras_unicas(palavras_lista_unica)
    razao=palavras_unicas/total_palavras
    return(razao)

def tamanho_medio_sentenca(texto):
    sentencas=separa_sentencas(texto)
    comprimento=len(sentencas)
    a=0
    total_palavras=0
    total_caracteres=0
    while (a<comprimento):
        sentenca=sentencas[a]
        frases=separa_frases(sentenca)
        comprimento_lista=len(frases)
        b=0
        while (b<comprimento_lista):
            frase=frases[b]
            palavras=separa_palavras(frase)
            n_palavras=len(palavras)
            total_palavras=total_palavras+n_palavras
            c=0
            while (c<n_palavras):
                palavra=palavras[c]
                caracteres=len(palavra)
                total_caracteres=total_caracteres+caracteres
                c=c+1
            b=b+1
        a=a+1
    tamanho_medio=(total_caracteres/comprimento)
    return(tamanho_medio)

def complexidade (texto):
    sentencas=separa_sentencas(texto)
    comprimento=len(sentencas)
    a=0
    total_frases=0
    while (a<comprimento):
        sentenca=sentencas[a]
        frases=separa_frases(sentenca)
        comprimento_lista=len(frases)
        b=0
        while (b<comprimento_lista):
            frase=frases[b]
            n_frases=len(frases)
            total_frases=total_frases+n_frases
            b=b+1
        a=a+1

    complexidade=(total_frases/comprimento)
    return(complexidade)

def tamanho_medio_frase(texto):
    sentencas=separa_sentencas(texto)
    comprimento=len(sentencas)
    a=0
    total_palavras=0
    total_caracteres=0
    n_frases=0
    while (a<comprimento):
        sentenca=sentencas[a]
        frases=separa_frases(sentenca)
        comprimento_lista=len(frases)
        n_frases=n_frases+comprimento_lista
        b=0
        while (b<comprimento_lista):
            frase=frases[b]
            palavras=separa_palavras(frase)
            n_palavras=len(palavras)
            total_palavras=total_palavras+n_palavras
            c=0
            while (c<n_palavras):
                palavra=palavras[c]
                caracteres=len(palavra)
                total_caracteres=total_caracteres+caracteres
                c=c+1
            b=b+1
        a=a+1
        
    tamanho_medio=(total_caracteres/n_frases)
    return(tamanho_medio)

#fim dos parametros de assinatura#

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    a=tamanho_medio_palavras(texto)
    b=relacao_type_token(texto)
    c=razao_hapax_legomana(texto)
    d=tamanho_medio_sentenca(texto)
    e=complexidade (texto)
    f=tamanho_medio_frase(texto)

    return[a,b,c,d,e,f]


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    z=0
    somatorio=0
    while (z<=5):
        nucleo=(as_a[z]-as_b[z])
        nucleoab=math.fabs(nucleo)
        somatorio=somatorio+nucleoab
        z=z+1
    sab=somatorio/6
    return(sab)

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    a=0
    n=len(textos)
    valores_similaridade=[]
    while (a<n):
        as_b=calcula_assinatura(textos[a])
        similaridade=compara_assinatura(ass_cp, as_b)
        valores_similaridade.append(similaridade)          
        a=a+1

    maior_similaridade=(min(valores_similaridade))
    b=0
    while (b<(len(valores_similaridade))):
        c=valores_similaridade[b]
        if (c==maior_similaridade):
            return (b+1)
        b=b+1
        

