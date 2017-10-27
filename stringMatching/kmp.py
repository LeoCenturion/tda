import time


def prefix_table(p, m):
    pt = [0] * m
    i = 1
    matchLen = 0
    while i < m:
        while i < m and p[i] == p[matchLen]:
            matchLen += 1
            pt[i] = matchLen
            i += 1
        matchLen = 0
        i += 1
    return pt

def KMP(t,p):
    m = len(p)
    n = len(t)
    lookup = prefix_table(p, m)
    coincidencias=[]
    i = 0
    start = time.clock()
    while i < n - m + 1:
        j = 0
        matchLen = 0
        while j < m:
            if t[i + j] == p[j]:
                matchLen += 1
                if matchLen == m:
                    #print "Match found at pos: %d" % (i)
                    coincidencias.append(i)
                    i += 1
                    break
                j += 1
            elif matchLen > 0 and lookup[matchLen] > 1:
                i = i + lookup[matchLen]
                break
            else:
                i += 1
                break
    finish = time.clock()
    result={}
    result["time"]=finish-start
    result["matches"]=coincidencias
    return result