class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        container = []
        for i in range(n): container.append(True)
        container[0], container[1] = False, False
        for num in range(2,n):
            if container[num]:
                for i in range(num*2, n, num):
                    container[i] = False
        return container.count(True)
            