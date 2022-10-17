class Fraction:

    def __init__(self,num=0,den=1):
        self.num = num
        self.den = den
    def printfraction(self):
        if self.num==0:
            print(0)
        elif self.den ==1:
            print(self.num)
        else:
            print(self.num,'/',self.den)
    def simplify(self):
        current = min(self.num,self.den)
        while current > 1:
            if self.num % current == 0 and self.den % current == 0:
                break
            current-=1
        self.num = self.num // current
        self.den = self.den // current
    def add(self,other):
        newnum = other.den * self.num + self.den * other.num
        newden = other.den * self.den
        self.num = newnum
        self.den = newden
        self.simplify()
    def multiply(self,other):
        newnum = self.num * other.num
        newden = other.den * self.den
        self.simplify()

f1 = Fraction(2,8)
f2 = Fraction(1,4)
f1.multiply(f2)
f1.printfraction()
