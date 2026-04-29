class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordlist: List[str]) -> int:
        wordset=set(wordlist)
        if endWord not in wordset:
            return 0
        q=deque([(beginWord, 1)])   
        while q:
            word, steps=q.popleft()
            if word==endWord:
                return steps
            for i in range(len(word)):
                for ch in 'qwertyuihlobfjkcmnapsvxzdg':
                    new=word[:i]+ch+word[i+1:]
                    if new in wordset:
                        q. append((new, steps+1))
                        wordset. remove(new)
        return 0