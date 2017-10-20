import numpy
import random
import time
import krh


def convertToBiteArray(x):
    byteArray =  bytearray(x)
    bitArray=numpy.array(byteArray)

    bitArray=map(lambda x: format(x,"b"),bitArray)

    bitArray = reduce(lambda x,y: x+y,bitArray)
    return bitArray



def primes(n):

    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]


def karpRabin(text,pattern):
    result = {}
    matches = []

    t = text
    p = pattern
    I = len(t) * (len(p) ** 2)
    h = krh.KRHash(p=numpy.ceil(random.random()*I))
    hp = h.hashPattern(p)

    start = time.clock()
    for i in xrange(len(t) - len(p)):
        hti = h.rollingHash(t[i:i + len(p)])
        if hp == hti:
            matches.append(i)

    finish = time.clock()

    result["time"] = finish - start
    result["matches"] = matches

    return result
