from Colussi import COLUSSI
from naive import ingenuo
from ZhuTakaoka import ZhuTakaokaSearch
from kmp import KMP
import csv
import time
import random


def main(texto):
	tFile = open(texto, 'r')
	t = tFile.read().strip()
	patron = buscar_palabra(texto)

	start1 = time.clock()
	matches1 = COLUSSI(patron,t)
	finish1 = time.clock()

	start2 = time.clock()
	matches2 = ingenuo(t,patron)
	finish2 = time.clock()

	start3 = time.clock()
	matches3 = ZhuTakaokaSearch(patron,len(patron),t,len(t))
	finish3 = time.clock()

	start4 = time.clock()
	matches41 = KMP(t, patron)
	finish4 = time.clock()
	matches4 = [matches41]

	print "texto: ", texto
	print "patron: ", patron
	print "time Colussi:", finish1-start1
	print "time kmp: ", finish4 - start4	
	print "time Naive: ", finish2 - start2
	print "time Zhu Takaoka: ", finish3 - start3

	verdad = (matches1 == matches2 == matches3)
	print verdad
    

"""
def main(texto, patron):
   tFile = open(texto, 'r')
   t = tFile.read().strip()

   start1 = time.clock()
   print "texto: ", texto
   matches1 = COLUSSI(patron,t)
   finish1 = time.clock()

   start2 = time.clock()
   print "texto: ", texto
   matches2 = COLUSSI(patron,t)
   finish2 = time.clock()

   print "texto: ", texto
   print "time Colussi:", finish1-start1
   print "time Naive: ", finish2 - start2
   print matches1 == matches2
"""

def abrir_archivos (): 
    try:
        textos=open("StringMatching3.csv")
    except IOError:
        raise IOError ("El archivo 'StringMatching.csv' no se pudo abrir")
    try:
        linea=textos.readline()
    except IndexError:
        print "Error en una columna (campo) del archivo 'StringMatching.csv'"
        return
    textos_leer=csv.reader(textos)
    for texto in textos_leer:
        #print "texto: ",texto[0]
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


abrir_archivos ()