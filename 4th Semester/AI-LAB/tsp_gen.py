import random as ra

def fitness_function(child) -> int:
    sum_ = 0
    from_ = child[0]
    to_ = child[1]
    for i in range(len(costs)):
        from_ = child[i]
        to_ = child[i+1]
        sum_ += costs[from_-1][to_-1]
    
    return sum_

def generate_child_by_cross_over(arr1: list, arr2: list) -> list:
    
    index_1 = ra.randint(1,8)
    index_2 = ra.randint(1,8)
    while index_1 == index_2:
        index_2 = ra.randint(1,8)
        
    if index_2 < index_1:
        index_1 , index_2 = index_2, index_1
        
    # print(index_2, index_1)
        
        
    c1 = [0]*10
    c2 = [0]*10
    
    c1[0], c1[9], c2[0], c2[9] = 1, 1, 1, 1
    
    # genertaing the chil
    
    c1[index_1:index_2+1] = p1[index_1:index_2+1]
    c2[index_1:index_2+1] = p2[index_1:index_2+1]
    
    
    # generate 1st child
    child_index1 = index_2 +1
    i = 1 
    while True:

        if child_index1 > 9: child_index1 = 1
        if 0 not in c1:
            break
        if i > 9:
            break
        
        if arr2[child_index1] in c1:
            child_index1 += 1
            
        elif arr2[child_index1] not in c1:
            if c1[i] == 0:
                c1[i] = arr2[child_index1]
                child_index1 += 1
                i += 1
            else:
                i += 1
                
    
    #generating second child 
    child_index2 = index_2 +1
    i = 1 
    while True:

        if child_index2 > 9: child_index2 = 1
        if 0 not in c2:
            break
        if i > 9:
            break
        
        if arr1[child_index2] in c2:
            child_index2 += 1
            
        elif arr1[child_index2] not in c2:
            if c2[i] == 0:
                c2[i] = arr1[child_index2]
                child_index2 += 1
                i += 1
            else:
                i += 1
    
    return c1, c2

def generate_child_by_mutation(arr: list) -> list:
    index_1 = ra.randint(1,8)
    index_2 = ra.randint(1,8)
    while index_1 == index_2:
        index_2 = ra.randint(1,8)
    
    arr[index_1] ,arr[index_2] = arr[index_2], arr[index_1]
    
    return arr

#? helper function
def generate_cost() -> None:
    for i in range(len(costs)):
        for j in range(len(costs)):
            if i == j:
                costs[i][j] = 0
            else:
                costs[i][j] = ra.randint(1,5)
                
def genetic_algo(): 
    
    
    i = 0
    while i< 1010:
        
        probability = ra.randint(1,10)
        
        if probability < 3: #?if the probability is less 30 we will call mutation
            print('Mutation is chooses')
            n = len(children)
            for j in range(n):
                c = generate_child_by_mutation(children[j])
                children.append(c)
        else:
            print('Cross over is choosen') #! if the probability is greater than 30
            try:
                c_i = 0
                c_j = 0
                
                for k in range(5):
                    c1, c2 = generate_child_by_cross_over(children[c_i], children[c_j])
                if c1 not in children:
                    children.append(c1)
                if c2 not in children:
                    children.append(c2)    
                if k == 2:
                    c_i += 2
                    c_j += 2
            except:
                continue
        i += 1
            
        best_fit()
            
    print_choosen_one(the_choosen_one())

def best_fit():
    best_fit_sums = []
    best_child = []
    i = 0
    global children
    global min_
    for child in children:
        s = fitness_function(child)
        if s not in best_fit_sums:
            best_fit_sums.append(s)
            i += 1
        
    
    best_fit_sums.sort()
    min_ = min(best_fit_sums)
    best_fit_sums = best_fit_sums[:4]
    
    n = len(children)
    i = 0
    while i < n:
        if len(best_fit_sums) == 0 or len(best_child) == 4:
            break
        check = fitness_function(children[i])
        if check in best_fit_sums:
            best_child.append(children[i])
            best_fit_sums.remove(check)
        i += 1
        
    children = best_child
    # return min_
    
def the_choosen_one():
    
    for child in children:
        if fitness_function(child) == min_:
            return child, min_
        
    # print('No child')
    
    
def print_choosen_one(arr):
    print('\n\n<--The best path that will be followed will be-->\n\n')
    
    for i in range(len(arr[0])):
        print(arr[0][i], end = ' ')
        if i != len(arr[0]) - 1:
            print("->", end = ' ')
            # print('\t\t', "v")
            
    print(f'\n\nWith the minimum cost of {min_}')
        
        
            
if __name__ =="__main__":
    
    """
    .########.....###....########..########.##....##.########..######.
    .##.....##...##.##...##.....##.##.......###...##....##....##....##
    .##.....##..##...##..##.....##.##.......####..##....##....##......
    .########..##.....##.########..######...##.##.##....##.....######.
    .##........#########.##...##...##.......##..####....##..........##
    .##........##.....##.##....##..##.......##...###....##....##....##
    .##........##.....##.##.....##.########.##....##....##.....######.
    """
    
    p1 = [1,2,3,4,5,6,7,8,9,1]
    p2 = [1,2,6,9,7,3,5,8,4,1]
    p3 = [1,3,4,2,8,6,9,7,5,1]
    p4 = [1,2,9,7,6,4,8,3,5,1]
    
    min_ = -9999
    children = [p1, p2, p3, p4] #? initial childeren 
    
    """
    ..######...#######...######..########..######.
    .##....##.##.....##.##....##....##....##....##
    .##.......##.....##.##..........##....##......
    .##.......##.....##..######.....##.....######.
    .##.......##.....##.......##....##..........##
    .##....##.##.....##.##....##....##....##....##
    ..######...#######...######.....##.....######.
    """
    
    costs = [[0 for i in range(9)]for j in range(9)]
    generate_cost() #?generating the cost
    

    """
    .########..######..########.
    ....##....##....##.##.....##
    ....##....##.......##.....##
    ....##.....######..########.
    ....##..........##.##.......
    ....##....##....##.##.......
    ....##.....######..##.......
    """
    #! genetic algorithm is called
    genetic_algo() 
    
    
