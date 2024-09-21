class rational_n:
    p=0
    q=0
def c_rational():
    x=rational_n()
    x.p=6
    x.q=5
    print("The Rational Number is:", x.p, "/", x.q)
c_rational()
def s_rational():
    x=rational_n()
    x.p=6
    x.q=5
    print("The Simplify Rational Number is:", x.p/x.q)
s_rational()
def string_f():
    x=rational_n()
    x.p=6
    x.q=5
    x=(x.p,x.q)
    print("The string form is:", x)
string_f()
def Unary_minus_operator():
    x=rational_n()
    x.p=6
    x.q=5
    print("The Unary minus opertaion is:",-x.p,"/",x.q)
Unary_minus_operator()
def reciprocal_f():
    x=rational_n()
    x.p=6
    x.q=5
    print("The Reciprocal Form is:",x.q,"/",x.p)
reciprocal_f()
def add():
    x1=rational_n()
    x1.p=6
    x1.q=5
    x2=rational_n()
    x2.p=6
    x2.q=5
    a=x1.p*x2.q
    b=x1.q*x2.p
    c=x1.q*x2.q
    print("The binary addition is:",a+b/c)
add()
def mul():
    x1=rational_n()
    x1.p=4
    x1.q=5
    x2=rational_n()
    x2.p=6
    x2.q=5
    a=x1.p*x2.p
    b=x1.q*x2.q
    print("The binary multiplication is:",a/b)
mul()
def sub():
    x1=rational_n()
    x1.p=6
    x1.q=5
    x2=rational_n()
    x2.p=6
    x2.q=5
    a=x1.p*x2.q
    b=x1.q*x2.p
    c=x1.q*x2.q
    print("The binary subtraction is:",a-b/c)
sub()
def division():
    x1=rational_n()
    x1.p=6
    x1.q=5
    x2=rational_n()
    x2.p=6
    x2.q=5
    a=x1.p*x2.q
    b=x1.q*x2.p
    print("The binary division is:",a/b)
division()
def conditional_operation():
    x1=rational_n()
    x1.p=6
    x1.q=5
    x2=rational_n()
    x2.p=6
    x2.q=5
    a=x1.p/x1.q
    b=x2.p/x2.q
    min=a if a<b else b
    print("The minimum value is:", min)
conditional_operation()
def to_data_type():
    x=rational_n()
    x.p=6
    x.q=5
    x=float(x.p/x.q)
    print("The appropiate data type is:",x)
to_data_type()
def from_data_type():
    x=rational_n()
    x.p=int(6)
    x.q=int(5)
    x=str(x.p)+"/"+str(x.q)
    print("Conversion from other data type:",x)
from_data_type()
def from_string():
    x=rational_n()
    x.p='6'
    x.q='5'
    x.p=float(6)
    x.q=float(5)
    x=x.p/x.q
    print("Conversion from an appropiate string is:",x)
from_string()
