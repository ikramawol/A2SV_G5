class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        res = []
        idx = []
        #boxes = list(map(int, boxes.split()))
        print(boxes)
        for i in range(len(boxes)):
            if boxes[i] == '1':
                idx.append(i)
        print(idx)
        for j in range(len(boxes)):
            counter = 0
            for k in range(len(idx)):
                counter += abs(idx[k] - j)
            res.append(counter)
        return res
