class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # bills.sort()

        changes = {5:0, 10:0}
        for i in range(len(bills)):
            if bills[i] == 5:
                changes[5] += 1
            elif bills[i] == 10 and changes[5]:
                changes[10] += 1
                changes[5] -= 1
            elif bills[i] == 20 and ((changes[5] and changes[10]) or changes[5] >= 3):
                if changes[5] and changes[10]:
                    changes[5] -= 1
                    changes[10] -= 1
                else:
                    changes[5] -= 3
            else:
                return False
        return True



          

