class MRUQueue(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.l = []
        for i in range(1, n + 1):
            self.l.append(i)

    def fetch(self, k):
        """
        :type k: int
        :rtype: int
        """
        self.l.append(self.l[k - 1])
        self.l.pop(k - 1)
        return self.l[-1]

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)