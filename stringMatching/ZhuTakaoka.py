#- *- coding: utf-8 - *-

#CONTANTE sigma = Alfabeto
ASIZE = 256
import time
import random
import csv

def preZtBc (x, m, ztbc):

    for a in x:
        ztbc[a] = {}
        for b in x:
            ztbc[a][b] = m
    for a in x:
        ztbc[a][x[0]] = m - 1

    for i in range (1, m - 1):
        ztbc[x[i - 1]][x[i]] = m - i -1


def preBmGsZhu (x , m , bmgs):
    suff = [0] * m

    ztsuffixes(x, m, suff)

    for i in range (m - 1, -1, -1):

        if (suff[i] == i + 1):

            for j in range (m - i - 1):

                if (bmgs[j] == m):
                    bmgs[j] = m - i - 1

    for i in range (m-1):
        bmgs[m - suff[i] - 1 ] = m - i - 1


def ztsuffixes (x, m, suff):
    suff[m - 1] = m
    g = m - 1
    f = 0

    for i in range (m - 2, -1, -1):

        if ((i > g) and (suff[i + m - f -1] < i - g)):

            suff[i] = suff [i + m - f - 1]

        else:

            if (i < g):
                g = i

            f = i

            while ((g > -1) and (x[g] == x[g + m - f -1])):
                g -= 1

            suff[i] = f - g


def ZhuTakaokaSearch (y, x):
    m=len(x)
    n=len(y)
    output = []
    bmgs = [m] * m
    ztbc = {}
    j = 0

    preZtBc(x, m, ztbc)
    preBmGsZhu(x, m, bmgs)

    #i = m -1
    result = {}
    start = time.clock()
    while (j <= n - m):
        i = m-1
        while ((i < m) and (x[i] == y[i + j])):
            i -= 1

        if (i < 0):

            output.append(j)
            j += bmgs[0]

        else:
            if ((not y[j + m - 2] in ztbc) or (not y[j + m - 1] in ztbc)):
                z = 0
            else:
                z = ztbc[y[j + m - 2]][y[j + m - 1]]
            j += max(bmgs[i], z )
        i = m -1

    finish = time.clock()
    result["time"]=finish-start
    result["matches"]=output
    return result


def asignar(i,m):
    return m -1


def crear_matriz(x, y):
    matriz=[]
    for i in range(0,x,1):
        matriz.append([])
        for j in range(0,y,1):
            matriz[i].append(0)
    return matriz

def main(texto):
    tFile = open(texto, 'r')
    t = tFile.read().strip()
    patron = buscar_palabra(texto)
    start = time.clock()
    print start
    ZhuTakaokaSearch(patron,t)
    print patron
    finish = time.clock()
    ingenuo(t,patron)
    finish2 = time.clock()
    print finish-start, finish2-start


def abrir_archivos (): 
    try:
        textos=open("StringMatching.csv")
    except IOError:
        raise IOError ("El archivo 'StringMatching.csv' no se pudo abrir")
    try:
        linea=textos.readline()
    except IndexError:
        print "Error en una columna (campo) del archivo 'StringMatching.csv'"
        return
    textos_leer=csv.reader(textos, delimiter=';')
    for texto in textos_leer:
        print "texto: ",texto[0]
        main(texto[0])
        print ("\n")
    textos.close()

def buscar_palabra(texto):
    A = 7
    tFile = open(texto, 'r')
    t = tFile.read().strip()
    x = len(t)
    y = random.randrange(x - A)
    cadena = ""
    print x
    for i in range (x):
        if i == y:
            for j in range(A):
                cadena += t[i+j]
    return cadena

def ingenuo(t,p):
    matches=[]
    for i in xrange(len(t)- len(p)):
        for j in xrange(len(p)):
            if(t[i+j]!=p[j]):
                break
            if(j==len(p)-1):
                matches.append(i)
    print matches


#abrir_archivos ()

