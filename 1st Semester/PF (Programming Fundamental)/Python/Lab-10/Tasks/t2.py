class rational:
    pass

#Single integer Rational Number
def createRationalsingle(p):
    p = int(p)
    r = rational()
    r.p = p
    r.q = 1
    return r

#Double integer Rational Number
def createRational(p, q):
    p = int(p)
    q = int(q)
    if(q == 0):
        raise Exception("Denominator cannot be Zero")
    r = rational()
    r.p = p
    r.q = q
    return r

# Simplification of Rational Number
def simplify(r):
    tillDivider = 0
    if(r.q == 0):
        raise Exception("Denominator cannot be Zero") 
    if(r.p > r.q):
        tillDivider = r.q
    else:
        tillDivider = r.p
    i = 2
    while(i <= tillDivider ):
        if(r.p % i == 0) and (r.q % i == 0):
            num = r.p/i
            den = r.q/i
            r.p = num 
            r.q = den
            i = 2
        else:
            i += 1
    r.p = int(r.p)
    r.q = int(r.q)
    return r
    
#Conversion to string form
def toString(r):
    return '(' + str(r.p) +','+ str(r.q) + ')'

#Uniary Negative Operation
def negate(r):
    r.p = - r.p
    return r

#Reciprocal Operation
def reciprocal(r):
    tmp = r.p
    r.p =  r.q
    r.q = tmp
    return r
    
#Addition Operation
def addition(r1, r2):
    den = r1.q * r2.q
    num1 = r1.p*r2.q
    num2 =  r2.p*r1.q
    num = num1 + num2
    r = createRational(num,den)
    return simplify(r)

#Subtraction Operation
def subtraction(r1, r2):
    den = r1.q * r2.q
    num1 = r1.p*r2.q
    num2 =  r2.p*r1.q
    num = num1 - num2
    r = createRational(num,den)
    return simplify(r)  
    
#Multiplication Operation
def multiplication(r1, r2):
    den = r1.q * r2.q
    num = r1.p * r2.p
    return simplify(createRational(num, den))
# Divisio Operation
def division(r1, r2):
    den = r1.p * r2.q
    num = r1.q * r2.p
    return simplify(createRational(num, den))
#Greaterthan COnditional Operation
def isGreater(r1, r2):
    first = r1.p*r2.q
    second = r2.p*r1.q
    if(first > second):
        return True
    else:
        return False
#Is Lessthan COnditional Operation
def isLess(r1, r2):
    first = r1.p*r2.q
    second = r2.p*r1.q
    if(first < second):
        return True
    else:
        return False

#The reset of Functions are left for your practice ;-)

def main():
    #1 
    r1 = createRationalsingle(2)
    print('1-',toString(r1))
    #2
    r2 = createRational(14,32)
    print('2-',toString(r2))
    #3
    r3 = simplify(r2)
    print('3-',toString(r3))
    #4
    string = toString(r3)
    print('4-',string)
    #5 
    r5 = negate(r3)
    print('5-', toString(r5))
    #6
    r6 = reciprocal(r5)
    print('6-', toString(r6))
    #7
    ra = createRational(2,5)
    rb = createRational(1,3)
    r7 = addition(ra, rb)
    print('7-', toString(r7))
    #8
    r8 = subtraction(ra, rb)
    print('8-', toString(r8))
    #9
    r9 = multiplication(ra, rb)
    print('9-', toString(r9))
    #10
    r10 = division(ra, rb)
    print('10-', toString(r10))
    
    #11
    print('11-', isGreater(ra, rb))
    #12
    print('11-', isLess(ra, rb))
    
    
    

main()