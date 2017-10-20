import pandas as pd
from stringMatching import naive
from stringMatching import karpRabin
from stringMatching import jaccardKarpRabin
import os
import random


def makeJKRFunctions(nGrams, nMinHashes, samplesPerMinHash, threshold):
    fList = []
    for ng in nGrams:
        for nMH in nMinHashes:
            for samples in samplesPerMinHash:
                for thr in threshold:
                    f = lambda t, p: jaccardKarpRabin.jaccardKarpRabin(t, p, \
                                                                       shingle="ngram", nGrams=ng, nMinHashes=nMH,
                                                                       samplesPerMinHash=samples, threshold=thr)
                    fList.append(
                        [f, "jkr: ngram, {}-gram, nmh = {}, spMH = {}, threshold={}".format(ng, nMH, samples, thr)])

    return fList

def main():
    results=[]
    texts=os.listdir("./datasets")

    for t in texts:
        if t.split(".")[1]=="gb":
            texts.remove(t)
    nGrams=[2,3]
    samplesPerMinHash = [5,10]
    nMinHashes=[5,1]
    threshold=[0,5]
    n = [naive.naiveStringMatching,"naive"]
    kr = [karpRabin.karpRabin,"kr"]
    algorithms=makeJKRFunctions(nGrams=nGrams,samplesPerMinHash=samplesPerMinHash,\
                              nMinHashes=nMinHashes,threshold=threshold)
    # algorithms=[]
    algorithms.append(n)
    algorithms.append(kr)

    patterns = []
    l = range(10, 50)
    n = 10
    # for f in texts:
    #     tFile = open("./datasets/" + f, "r")
    #     t = tFile.read().rstrip()
    #     p = []
    #     tLen = len(t)
    #     for i in range(n):
    #         pLen = random.choice(l)
    #         index = random.choice(range(tLen - pLen))
    #         p.append(t[index:index + pLen])
    #
    #     patterns.append(p)
    #     tFile.close()

    df = pd.read_csv("StringMatching.csv",delimiter=";")

    for i in xrange(len(texts)):

        f = texts[len(texts)-i-1]
        # pattern = patterns[len(texts)-i-1]
        pattern = df[df.Texto==f]["Patron"].values

        tFile = open("./datasets/" + f, "r")
        t = tFile.read().rstrip()
        tLen = len(t)
        print "processing  text {}".format(f)
        for p in pattern:
            print "processing  pattern: {}".format(p)
            for a in algorithms:
                print "processing with algorithm: {}".format(a[1])
                result = a[0](t, p)
                results.append([f, tLen, p, len(p), a[1], result["time"], len(result["matches"])])
                print "time taken: {}".format(result["time"])
                print "matches found: {}".format((len(result["matches"])))

        resultsDf = pd.DataFrame(results,columns=["text", "len_text", "pattern", "len_pattern", "algorithm", "time", "matches"])

        csv = open("resultadosjkr.csv", "w")
        resultsDf.to_csv(csv)

        tFile.close()




    df = pd.DataFrame(results, columns=["text", "len_text", "pattern", "len_pattern", "algorithm", "time", "matches"])

    csv = open("resultadosjkr.csv","w")
    df.to_csv(csv)
    csv.close()


main()