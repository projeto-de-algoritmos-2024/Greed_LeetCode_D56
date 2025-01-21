class Solution:
    def scheduleCourse(self, courses):

        self.ans = 0

        def backtrack(i, current_time, count):

            # Atualiza resposta global
            self.ans = max(self.ans, count)

            if i == len(courses):
                return

            # 1) Não pegar o curso i
            backtrack(i+1, current_time, count)

            # 2) Tentar pegar o curso i, se couber
            duration, lastDay = courses[i]
            if current_time + duration <= lastDay:
                backtrack(i+1, current_time + duration, count + 1)

        backtrack(0, 0, 0)
        return self.ans
