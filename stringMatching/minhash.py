import random


class JaccardMinhash():

    randomIndexesPattern=[]
    randomIndexesText=[]
    def __init__(self,setsLenght,samples):
        indexes=range(setsLenght)
        random.shuffle(indexes)
        self.randomIndexesPattern=indexes[0:samples]
        random.shuffle(indexes)
        self.randomIndexesText = indexes[0:samples]

    def minhash(self,s1, s2):
        tries = 0
        for i in range(len(self.randomIndexesText)):
            indexPattern=self.randomIndexesPattern[i]
            indexText = self.randomIndexesText[i]

            if s1[indexPattern] == s2[indexText]:
                return tries
            tries+=1
        return tries

    @classmethod
    def shingle(cls,string,shingle="word",nGrams=2):
       if(shingle=="word"):
           s= string.split(" ")
           if(len(s)==1):
               return s
           elif len(s)>2:
               s=s[:-2]
           return  s[1:]
       elif(shingle=="ngram"):
           return cls.ngrams(string,nGrams)

    @classmethod
    def ngrams(cls,string, nGrams):
        #newString = "$"*(nGrams-1)+ string + "$"*(nGrams-1)
        shingles=[]
        for i in xrange(len(string)):
            shingles.append(string[i:i+nGrams])
        return shingles
