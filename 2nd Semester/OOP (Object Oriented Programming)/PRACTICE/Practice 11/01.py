class Rational:
    def __init__(self):
        self.__p = 0
        self.__q = 1

    def set(self, p, q):
        self.__p = p
        if q == 0:
            q = 1
        self.__q = q

    def __str__(self):
        if self.__p < 0 and self.__q< 0:
            return f'{str(-(self.__p))}/{str(-(self.__q))}'
        elif self.__q < 0 and self.__p > 0:
            return f'-{str(self.__p)}/{str(-(self.__q))}'

        return f'{str(self.__p)}/{str(self.__q)}'

    def __eq__(self, obj):
        return self.__p == obj.__p and self.__q == obj.__q

    def __sub__(self, obj):
        new_object = Rational()
        new_object.__q = self.__q * obj.__q
        new_object.__p = (self.__p * obj.__q) - (self.__q * obj.__p)
        return new_object
    
    def normalize(self, p, q):
        divisor = 1
        for i in range(1, min(p,q)+1):
            if p%i == q%i == 0:
                divisor = i
        p = int(p / divisor)
        q = int(q / divisor)
        return p, q

        # print(f'{p} / {q}')
    def LCM(self, a,b):
        loop = a*b
        for i in range(max(a,b), loop+1):
            if i % a== 0 and i % b == 0:
                return i

    def __add__(self, obj):
        new_obj = Rational()

        self.__p, self.__q = self.normalize(self.__p, self.__q)
        obj.__p, obj.__q = obj.normalize(obj.__p, obj.__q)
        
        new_obj.__q = new_obj.LCM(self.__q, obj.__q)
        new_obj.__p = ((new_obj.__q //self.__q)*self.__p) + ((new_obj.__q//obj.__q)*obj.__p)
        new_obj.__p, new_obj.__q = new_obj.normalize(new_obj.__p, new_obj.__q)

        return f'{new_obj.__p} / {new_obj.__q}'
    
    def __sub__(self, obj):
        new_obj = Rational()

        self.__p, self.__q = self.normalize(self.__p, self.__q)
        obj.__p, obj.__q = obj.normalize(obj.__p, obj.__q)
        
        new_obj.__q = new_obj.LCM(self.__q, obj.__q)
        new_obj.__p = ((new_obj.__q //self.__q)*self.__p) - ((new_obj.__q//obj.__q)*obj.__p)
        new_obj.__p, new_obj.__q = new_obj.normalize(new_obj.__p, new_obj.__q)

        return f'{new_obj.__p} / {new_obj.__q}'

    def __mul__(self,obj):
        new_obj = Rational()

        self.__p, self.__q = self.normalize(self.__p, self.__q)
        obj.__p, obj.__q = obj.normalize(obj.__p, obj.__q)

        new_obj.__p = self.__p * obj.__p
        new_obj.__q = self.__q * obj.__q

        new_obj.__p, new_obj.__q = new_obj.normalize(new_obj.__p, new_obj.__q)
        return f'{new_obj.__p} / {new_obj.__q}'

    def __eq__(self, obj):
        if self.__p/self.__q == obj.__p/obj.__q:
            return True
        return False
    def __gt__(self, obj):
        if self.__p/self.__q > obj.__p/obj.__q:
            return True
        return False
    
    def __lt__(self, obj):
        if self.__p/self.__q < obj.__p/obj.__q:
            return True
        return False


def main():
    r1 = Rational()
    r2 = Rational()
    # r3 = Rational()
    r1.set(3,4)
    r2.set(1,2)
    # r3.set(24,48)
    # print(r3.normalize(24,48))
    print(r1)
    print(r2)
    print(r1 + r2)
    print(r1-r2)
    print(r1 * r2)
    print(r1 == r2)
    print(r1 > r2)
    print(r1<r2)


    # if r1 == r2:
    #     print ('Both are equal')
    # if r1 == r3:
    #     print ('Both are equal')
    # else:
    #     print ('Both are different')
    # r4 = r1 - r3
    # print(r4)

main()