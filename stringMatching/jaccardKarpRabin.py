import time
import minhash


def jaccardKarpRabin(text,pattern,shingle,nGrams,nMinHashes,samplesPerMinHash,threshold):
    results = {}
    matches = []
    t = text
    sp = minhash.JaccardMinhash.shingle(string=pattern,shingle=shingle,nGrams=nGrams)

    if samplesPerMinHash <1:
        s = len(sp) * samplesPerMinHash
    else:
        s = samplesPerMinHash

    minhashes=[minhash.JaccardMinhash(len(sp),s) for i in xrange(nMinHashes)]
    t=minhash.JaccardMinhash.shingle(string=t, shingle=shingle, nGrams=nGrams)
    start = time.clock()
    for i in xrange(len(t)-len(pattern)):
        st= t[i:i+len(sp)]
        distances = [mh.minhash(sp,st) for mh in minhashes]
        d = float(sum(distances))/float(len(distances))
        if d <= threshold:
            matches.append(i)

    finish = time.clock()
    results["time"] = finish - start
    results["matches"] = matches
    return results


