class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank_set = set(bank)
        
        if end not in bank_set:
            return -1
        
        start_set = set([start])
        end_set = set([end])
        visited_set = set([start, end])
        min_mutation = 0
        
        while start_set:
            min_mutation += 1
            new_set = set()
            
            for mut in start_set:
                for i in range(len(mut)):
                    for c in ["A", "C", "G", "T"]:
                        if mut[i] == c:
                            continue
                        new_mut = mut[:i] + c + mut[i + 1:]
                        
                        if new_mut in end_set:
                            return min_mutation
                        
                        if new_mut in bank and new_mut not in visited_set:
                            new_set.add(new_mut)
                            visited_set.add(new_mut)
            start_set = new_set
            
            if len(start_set) > len(end_set):
                start_set, end_set = end_set, start_set
                
        return -1
