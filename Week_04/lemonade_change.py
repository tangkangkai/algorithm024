class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num_of_five = 0
        num_of_ten = 0
        
        for bill in bills:
            if bill == 5:
                num_of_five += 1
            elif bill == 10:
                if num_of_five < 1:
                    return False
                num_of_five -= 1
                num_of_ten += 1
            elif bill == 20:
                if num_of_ten < 1 and num_of_five < 3:
                    return False
                elif num_of_ten < 1:
                    num_of_five -= 3
                else:
                    num_of_ten -= 1
                    num_of_five -= 1
        return num_of_five >= 0 and num_of_ten >= 0
                    