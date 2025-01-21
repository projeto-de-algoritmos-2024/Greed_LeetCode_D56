class Solution(object):
    def findMinMoves(self, machines):
        
        total_clothes = sum(machines)
        n = len(machines)

        if total_clothes % n != 0:
            return -1

        target = total_clothes // n
        moves = 0

        for clothes in machines:
            moves += abs(clothes - target)

        return moves
