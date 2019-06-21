def solve(nums, k, t):
	l = len(nums)
	
	if(len(nums) <= 1):
	    return False
	
	for i in xrange(l-1):
	    if(i+k >= l):
	        end = l
	    else:
	        end = i+k+1
	    for j in xrange(i+1, end):
	        if max(nums[i], nums[j]) - min(nums[i], nums[j]) <= t:
	            return True
	return False

if __name__ == '__main__':
	print(solve([-3,3], 1, 4))
