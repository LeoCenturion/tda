import numpy


class KRHash:
    prevHash=None
    prevMSC=None
    p=None
    h=None
    lenPattern = None
    def __init__(self,p,hash="string"):
        self.prevMSCList = []
        self.prevHashList = []
        self.p=p
        if hash == "binary":
            self.h= self.hString

        elif hash == "string":
            self.h = self.hString

    def hashPattern(self,p):
        self.lenPattern = len(p)
        return self.h(p)


    def hString(self,x):
        result = 0
        n = len(x)
        for i in range(n):
            result += numpy.mod((256**(n-1-i))*ord(x[i]), self.p)
        return numpy.mod(result,self.p)

    def rollingHash(self,t):
        if self.prevHash==None:
            self.prevHash=self.h(t)
            self.prevMSC=ord(t[0])
            return self.prevHash

        a1=numpy.mod(self.prevHash*256,self.p)
        a2=numpy.mod((self.prevMSC*256**self.lenPattern),self.p)
        a3=ord(t[-1])
        result = numpy.mod(a1-a2+a3,self.p)

        self.prevMSC = ord(t[0])
        self.prevHash = result
        return result

    def multipleRollingHash(self,listT):
        resultList =[]
        for i in range(len(listT)):
            t= listT[i]
            if len(self.prevHashList)<=i:
                self.prevHashList.append((self.h(t)))
                self.prevMSCList.append(ord(t[0]))
                resultList.append(self.prevHashList[i])

            a1=numpy.mod(self.prevHashList[i]*256,self.p)
            a2=numpy.mod((self.prevMSCList[i]*256**self.lenPattern),self.p)
            a3=ord(t[-1])
            result = numpy.mod(a1-a2+a3,self.p)

            self.prevMSCList[i] = ord(t[0])
            self.prevHashList[i] = result
            resultList.append(result)
        return resultList
