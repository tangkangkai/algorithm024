import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        word_dict = {}
        for word in wordList:
            word_dict[word] = False
            
            
        if endWord not in word_dict:
            return 0
        word_dict[beginWord] = True
            
        queue = [beginWord]
        new_queue = []
        level = 1
        
        while queue:
            for word in queue:
                word_lst = list(word)
                for i in range(len(word)):
                    temp = word_lst[i]
                    for ch in list(string.ascii_lowercase):
                        word_lst[i] = ch

                        new_word = "".join(word_lst)
                        if new_word == endWord:
                            return level + 1

                        if new_word in word_dict and not word_dict[new_word]:
                            new_queue.append(new_word)
                            word_dict[new_word] = True

                    word_lst[i] = temp
            queue = new_queue
            new_queue = []
            level += 1
            
        
        return 0     
                
            