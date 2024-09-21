from bag import *

if __name__ == '__main__':
    
    
    bag = Bag()
    
    bag.insert(2)
    bag.insert(4)
    bag.insert(6)
    bag.insert(1)
    bag.insert(9)
    bag.insert(2)
    
    bag.display_bag()
    
    
    bag.remove(4)
    # bag.remove(69)
    print('The bag after the updation: ', end = '')
    bag.display_bag()
    
    bag.update(9, 69)
    print('The bag after the updation of 69:')
    bag.display_bag()
    
    print('The size of the bag is', bag._size())
    
    # print('Find 7', bag.search(7))
    
    bag2 = [10,11,12,13]
    bag3 = (bag.join(bag2))
    # bag3 = bag.join(bag2)
    bag3.display_bag()
    
    bag4 = bag.clone()
    
    bag4.display_bag()
    
    