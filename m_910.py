import math

class Solution:
    def smallestRangeII(self, A, K):

        n = len(A)
        A.sort()

        print(A)
        static_diff = A[n-1] - A[0]

        a = max(A[0] + K, A[0] - K)
        b = min(A[n-1] + K, A[n-1] - K)
        _min = min(a,b)
        _max = max(a,b)
        max_diff = _max - _min

        print("sss:", static_diff, _max, _min)
        if n > 2:
            for i in range(1,n-1):
                if max_diff >= static_diff:
                    break

                num = A[i]
                nums = [num + K, num - K]

                a = max(nums)
                b = min(nums)

                if a > _max and b < _min:
                    _a = a - _max
                    _b = _min - b

                    if _a < _b:
                        max_diff += _a
                        _max = a
                    else:
                        max_diff += _b
                        _min = b

                elif b > _max:
                    _b = b - _max
                    max_diff += _b
                    _max = b

                elif a < _min:
                    _a = _min - a
                    max_diff += _a
                    _min = a

                print(num, b, a, _min, _max, max_diff)
        return min(max_diff, static_diff)

s = Solution()
# assert(s.smallestRangeII([1], 0) == 0)
# assert(s.smallestRangeII([1], 1) == 0)
# assert(s.smallestRangeII([1,1], 1) == 0)
# assert(s.smallestRangeII([0,10], 2) == 6)
# assert(s.smallestRangeII([1,3,6], 3) == 3)
# assert(s.smallestRangeII([1,4,4,6], 3) == 3)
# assert(s.smallestRangeII([1,2,3,4,5,6], 5) == 5)
assert(s.smallestRangeII([8038,9111,5458,8483,5052,9161,8368,2094,8366,9164,53,7222,9284,5059,4375,2667,2243,5329,3111,5678,5958,815,6841,1377,2752,8569,1483,9191,4675,6230,1169,9833,5366,502,1591,5113,2706,8515,3710,7272,1596,5114,3620,2911,8378,8012,4586,9610,8361,1646,2025,1323,5176,1832,7321,1900,1926,5518,8801,679,3368,2086,7486,575,9221,2993,421,1202,1845,9767,4533,1505,820,967,2811,5603,574,6920,5493,9490,9303,4648,281,2947,4117,2848,7395,930,1023,1439,8045,5161,2315,5705,7596,5854,1835,6591,2553,8628], 4643) == 8870)
