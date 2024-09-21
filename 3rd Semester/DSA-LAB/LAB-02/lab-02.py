class Polynomial:

    def __init__(self, degree):

        self.degree = degree
        self.array = [0] * (degree+1)

    # def setCoefficinet(self):

    #     j = self.degree
    #     for i in range(self.degree + 1):
    #         self.array[i] = input(f'Enter the value of x^{j}: ')
    #         j -= 1
    def setCoefficinet(self, array):
        self.array = array

    def __str__(self) -> str:
        s = ''
        j = self.degree
        for i in range(len(self.array)):
            if self.array[i] != 0:
                s += f'{self.array[i]}x^{j} '
            
            j -= 1
        return s

    def __add__(self, obj):

        if len(self.array) >= len(obj.array):
            new_obj = Polynomial(len(self.array)-1)
            new_obj.array = self.array
            flag = True
        else:
            new_obj = Polynomial(len(obj.array)-1)
            new_obj.array = obj.array
            flag = False

        min_len = min(len(self.array), len(obj.array))
        index = -1
        for i in range(min_len):
            if flag:
                new_obj.array[index] += obj.array[index]
            else:
                new_obj.array[index] += self.array[index]
            index -= 1
        return new_obj

    def value(self, x):
        if x == 0:
            temp = -1
        else:
            temp = ((-x)-1)
        return (self.array[temp])


if __name__ == '__main__':
    obj1 = Polynomial(5)
    obj2 = Polynomial(3)
    obj1.setCoefficinet([3,0,-7,4,10,2])
    obj2.setCoefficinet([3,0,-5,4])
    print(obj1)
    print(obj2)
    new_obj = obj1 + obj2
    print(new_obj)
    print(f'The value is :{new_obj.value(3)}')