def max_benefit(w,p,n,limit):
    if n==0 or limit==0:
        return 0
    
    if w[n-1]>limit:  #skip_case if weight of item > weight of bag
        return max_benefit(w,p,n-1,limit)
    
    else: #max of in case if item is skipped and if item is included
        return max(max_benefit(w,p,n-1,limit),p[n-1] + max_benefit(w,p,n-1,limit-w[n-1]))
    
def main():
    values =[60,100,120]
    weights =[10,20,30]
    li =10
    print(max_benefit(weights,values,3,50))

main()