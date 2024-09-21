def KS(n, C, v, w):
	if n==0 or C <= 0:
		return 0, []
	if w[n-1] > C:
		return KS(n-1, C, v, w)
	exKSv, exKSs = KS(n-1, C, v, w)
	inKSv, inKSs = KS(n-1, C-w[n-1], v, w)
	if exKSv >= inKSv + v[n-1]:
		return exKSv, exKSs
	else:
		inKSv = inKSv + v[n-1]
		inKSs.append(n)
		return inKSv, inKSs

def main():
    prices = [60, 100, 120]
    weights = [10, 20, 30]
    ov, os = KS(3, 50, prices, weights)
    print("Max benifit", ov)
    print("Optimal set", os)
    
main()

