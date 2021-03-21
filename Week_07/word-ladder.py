class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        word_set = set(wordList)
        
        # edge case where end word not in word list
        if endWord not in word_set:
            return 0
        
        begin_set = set([beginWord])
        end_set = set([endWord])
        
        visited_set = set([beginWord, endWord])
        
        word_num = 1
        
        while begin_set:
            word_num += 1
            new_set = set()
            for word in begin_set:
                for i in range(len(word)):
                    for c in list(string.ascii_lowercase):
                        if word[i] == c:
                            continue
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in end_set:
                            return word_num
                        if new_word in visited_set:
                            continue
                        if new_word in word_set:
                            new_set.add(new_word)
                            visited_set.add(new_word)
            begin_set = new_set
            
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
        return 0
            
        
        