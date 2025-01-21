class Solution(object):
    def findMinMoves(self, machines):
        total_clothes = sum(machines)
        n = len(machines)
        
        if total_clothes % n != 0:
            return -1
        
        target = total_clothes // n
        max_moves = 0
        cumulative_diff = 0
        
        for clothes in machines:
            diff = clothes - target
            cumulative_diff += diff
            max_moves = max(max_moves, abs(cumulative_diff), diff)
        
        return max_moves
