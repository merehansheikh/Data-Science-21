from abc import *

class My_ABC:
    @abstractmethod
    def abstract_function(self):
        print ('I am abstract function')

def main():
    my_abc = My_ABC()
    my_abc.abstract_function()

main()
