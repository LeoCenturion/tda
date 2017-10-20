import time


def naiveStringMatching(text,pattern):

    results={}
    matches=[]

    t = text
    p = pattern

    start = time.clock()
    for i in xrange(len(t)-len(p)):
        match=True
        j=0
        while(match and j<len(p)):
            if (t[i + j] != p[j]):
                match=False
            if (j >= (len(p) - 1) and match):
                matches.append(i)
            j+=1
    finish = time.clock()
    results["time"]=finish-start
    results["matches"]=matches


    return results
