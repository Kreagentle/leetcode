class Leaderboard(object):

    def __init__(self):
        self.d = dict()

    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        if playerId not in self.d:
            self.d[playerId] = 0
        self.d[playerId] += score

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        result = 0
        iter = 0
        tempd = sorted(self.d.items(), key=lambda item: item[1], reverse=True)
        for i, j in tempd:
            result += j
            if iter == K - 1:
                break
            iter += 1
        return result

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        self.d[playerId] = 0