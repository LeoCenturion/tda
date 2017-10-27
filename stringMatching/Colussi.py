import csv
import time
import random
ASIZE = 256

def preColussi(x, m, h, sig, shift):
    hmax = [0]*(m+1)
    kmin = [0]*m
    nhd0 = [0]*m
    rmin = [0]*m

    #/* Computation of hmax */
    i = 1
    k = 1
    while (k <= m):
      while(x[i] == x[i - k]):
         i += 1
      hmax[k] = i
      q = k + 1
      while(hmax[q - k] + k < i):
         hmax[q] = hmax[q - k] + k
         q += 1
      k = q
      if (k == i + 1):
         i = k
    #print "hmax: ", hmax


    #/* Computation of kmin */
    for i in range (m, 0, -1): #va desde m hasta 1
      if (hmax[i] < m):
         kmin[hmax[i]] = i
    #print "kmin: ", kmin


    #/* Computation of rmin */
    #r=0
    for i in range (m-1, -1, -1):
      if (hmax[i + 1] == m):
         r = i + 1
      if (kmin[i] == 0):
         rmin[i] = r
      else:
         rmin[i] = 0
    #print "rmin: ", rmin


    #/* Computation of h */
    s = -1
    r = m
    for i in range (0, m):
      if (kmin[i] == 0):
         r -= 1
         h[r] = i
      else:
         s += 1
         h[s] = i
    nd = s
    #print "h: ", h


    #/* Computation of shift */
    i = 0
    while (i <= nd):
      shift[i] = kmin[h[i]]
      i += 1
    i = nd + 1
    while (i < m):
      shift[i] = rmin[h[i]]
      i += 1
    shift[m] = rmin[0]
    #print "shift: ", shift


    #/* Computation of nhd0 */
    s = 0
    i = 0
    while (i < m):
      nhd0[i] = s
      if (kmin[i] > 0):
         s += 1
      i += 1
    #print "nhd0", nhd0


    #/* Computation of sig */
    i = 0
    while (i <= nd):
      sig[i] = nhd0[h[i] - kmin[h[i]]]
      i += 1
    i= nd+ 1
    while (i<m):
      #print "len(nhd0):", len(nhd0)
      #print "cuenta: ", m - rmin[h[i]]
      #chau = nhd0[m - rmin[h[i]]]
      sig[i] = nhd0[m - rmin[h[i]]]
      i+=1
    sig[m] = nhd0[m - rmin[h[m - 1]]]
    #print "sig: ", sig

    return nd

def COLUSSI(y, x):
    m = len(x)
    x = x+"  " ###################
    n = len(y)
    h =[0]*m
    sig = [0]*(m+1)
    shift =[0]*(m+1)

    #/* Processing */
    nd = preColussi(x, m, h, sig, shift)

    #/* Searching */
    i = 0
    j = 0
    last = -1
    matches=[]
    result ={}
    start = time.clock()
    while (j <= (n - m)):
        while ((i < m) and (last < j + h[i]) and (x[h[i]] == y[j + h[i]])):
            i += 1
        if ((i >= m) or (last >= j + h[i])):

            matches.append(j)
            i = m
        if (i > nd):
            last = j + m - 1
        j += shift[i]
        i = sig[i]
    finish = time.clock()
    result["time"]=finish-start
    result["matches"]=matches
    #print "El patron coincide con el texto en las siguientes posiciones del texto: ", matches
    return result

    """
    def main(texto):
    tFile = open(texto, 'r')
    t = tFile.read().strip()
    patron = buscar_palabra(texto)
    start = time.clock()
    print start
    print patron
    COLUSSI(patron,t)
    finish = time.clock()
    print finish-start
    
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
    cadena = " "
    while (cadena[0] == " "):
      A =7
      tFile = open(texto, 'r')
      t = tFile.read().strip()
      x = len(t)
      y = random.randrange(x - A)
      cadena = ""
      #print x
      for i in range (x):
         if i == y:
            for j in range(A):
               cadena += t[i+j]
    
    return cadena
    
    """
    #abrir_archivos()