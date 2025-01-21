import heapq

class Solution:
    def scheduleCourse(self, courses):

        # 1) Sort by lastDay
        courses.sort(key=lambda x: x[1])

        total_time = 0
        max_heap = [] 

        for duration, lastDay in courses:
            # Adiciona a duração do curso no heap
            heapq.heappush(max_heap, -duration)
            total_time += duration

            # se extrapolar o lastDay, remove o curso de maior duração
            if total_time > lastDay:
                longest_duration = -heapq.heappop(max_heap)
                total_time -= longest_duration

        return len(max_heap)
