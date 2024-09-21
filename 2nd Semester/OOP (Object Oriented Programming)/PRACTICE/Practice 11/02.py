class Complex:
    def __init__(self):
        self.real = 0
        self.imag = 0

    def set(self, real, imag):
        self.real = real
        self.imag = imag
        self.magnitude = ((self.real)**2 + (self.imag)**2)**0.5

        self.magnitude = (self.real)
    
    def __mul__(self,obj):
        new_obj = Complex()
        new_obj.real = self.real * obj.real
        new_obj.imag = self.imag * obj.imag

        return new_obj
    def __add__(self,obj):
        new_obj = Complex()
        new_obj.real = self.real + obj.real
        new_obj.imag = self.imag + obj.imag

        return new_obj

    def __sub__(self,obj):
        new_obj = Complex()
        new_obj.real = self.real - obj.real
        new_obj.imag = self.imag - obj.imag

        return new_obj
    
    def __eq__(self,obj):
        if self.magnitude == obj.magnitude :
            return True
        return False
    
    def __lt__(self,obj):
        if self.magnitude < obj.magnitude :
            return True
        return False
    
    def __gt__(self,obj):
        if self.magnitude > obj.magnitude :
            return True
        return False
    
    def __str__(self):
        return f'{self.real} + {self.imag}j'

def main():
    o1 = Complex()
    o1.set(3,4)
    o2 = Complex()
    o2.set(2,3)
    print(o1 < o2)
    print(o1 * o2)

main()