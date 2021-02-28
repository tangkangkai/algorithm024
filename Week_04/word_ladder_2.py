class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        visited = {}
        for word in wordList:
            visited[word] = False
        visited[beginWord] = True
        
        res = []
        queue = [([beginWord], visited)]
        new_queue = []
        found = False
        
        while queue and not found:
            for word_list, v in queue:
                last_word = word_list[-1]
                
                for i in range(len(last_word)):
                    for ch in list(string.ascii_lowercase):
                        new_word = last_word[:i] + ch + last_word[i+1:]
                        if new_word == endWord:
                            found = True
                        
                        if new_word in v and not v[new_word]:
                            new_word_list = word_list.copy()
                            new_visited = v.copy()
                            
                            new_word_list.append(new_word)
                            new_visited[new_word] = True
                            new_queue.append((new_word_list, new_visited))
            
            queue = new_queue
            new_queue = []
                        
        if found:
            for word_list, _ in queue:
                if word_list[-1] == endWord:
                    res.append(word_list)
                    
        return res
                