class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        p = defaultdict(list)
        for word in wordList: 
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                p[pattern].append(word)
        
        q = deque()
        q.append(beginWord)
        seen = set()
        seen.add(beginWord)
        count = 1
        while q:
            for _ in range(len(q)): 
                word = q.popleft()
                if word == endWord: 
                    return count
                for i in range(len(word)):
                    combo = word[:i] + "*" + word[i+1:]
                    for nxt in p[combo]:
                        if nxt in seen:
                            continue
                        q.append(nxt)
                        seen.add(nxt)
            count +=1
        return 0

