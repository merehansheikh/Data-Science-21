
class Set:
    def __init__(self):
        self.__elements = []

    def is_not_exist(self, element):
        for e in self.__elements:
            if e == element:
                return False
        return True

    def is_exist(self, element):
        for e in self.__elements:
            if e == element:
                return True
        return False

    def add_element(self, element):
        if self.is_not_exist(element):
            self.__elements.append(element)

    def __str__(self):
        s = '{'
        for element in self.__elements:
            s = s + str(element) + ', '
        string = ''
        string = s[0:len(s)-2]
        string += '}'
        return string

    def is_subset(self, obj):
        count = 0
        for el in self.__elements:
            if obj.is_exist(el):
                count += 1
        if count == len(self.__elements):
            return True
        return False
    def is_superset(self, obj):
        count = 0
        for el in self.__elements:
            if obj.is_exist(el):
                count += 1
        if count == len(obj.__elements):
            return True
        return False

    def compare(self, obj):
        if len(self.__elements) != len(obj.__elements):
            return False
        count = 0
        for el in self.__elements:
            if obj.is_exist(el):
                count += 1
        if count == len(obj.__elements):
            return True
        return False
    

    def count_difference(self, obj):
        count = 0
        for el in self.__elements:
            if obj.is_exist(el):
                count += 1
        elements_not_existing = len(self.__elements) - count

        return elements_not_existing

def main():
    s1 = Set()
    s1.add_element(1)
    s1.add_element(2)
    s1.add_element(3)
    s1.add_element(4)
    print(s1)
    s2 = Set()
    s2.add_element(1)
    s2.add_element(2)
    s2.add_element(3)
    # s2.add_element(4)
    print(s2)

    print(f'Wheter s1 is the subset of s2   {s1.is_subset(s2)}')
    print(f'Wheter s1 is the superset of s2 {s1.is_superset(s2)}')
    print(f'Wheter s1 and s2 have same elements or not  {s1.compare(s2)}')
    print(f'The number of elements of current object that not exist in second set: {s1.count_difference(s2)}')

main()