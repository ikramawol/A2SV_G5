class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)

        result = []

        r = 0
        for l in range(0, len(tasks), 4):
            timeTaken = []
            timeTaken.append(processorTime[r] + tasks[l])
            timeTaken.append(processorTime[r] + tasks[l+1])
            timeTaken.append(processorTime[r] + tasks[l+2])
            timeTaken.append(processorTime[r] + tasks[l+3])

            result.append(max(timeTaken))
            r += 1
            
        return max(result)
            