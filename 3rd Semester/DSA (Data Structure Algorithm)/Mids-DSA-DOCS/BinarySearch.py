def BinarySearch(A, x):
    return BinarySearchWorker(A, 1, len(A), x)
  
def BinarySearchWorker(A, p, r, x):
    if p <= r:
        q = int((p+r)/2)
        if x == A[q]:
	        return True
        elif x < A[q]:
	        r = q-1
        else:
	        p = q+1
        return BinarySearchWorker(A, p, r, x)
    return False
  
def main():
    nums = [2,4,5,8,9,12,17,22,31,47]
    r1 = BinarySearch(nums, 31)
    print(r1)
    r2 = BinarySearch(nums, 6)
    print(r2)

main()	
	
  