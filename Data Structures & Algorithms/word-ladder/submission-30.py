class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = {word: set() for word in wordList}
        graph[beginWord] = set()
        for w1 in wordList:
            diff_begin = 0
            for i in range(len(w1)):
                if not w1[i] == beginWord[i]:
                    diff_begin +=1
            if not diff_begin > 1:
                graph[beginWord].add(w1)
            for w2 in wordList:
                if w1 == w2:
                    continue
                diff = 0
                for i in range(len(w1)):
                    if not w1[i] == w2[i]:
                        diff +=1
                if not diff >1:
                    graph[w1].add(w2)
                    graph[w2].add(w1)
        q = deque()
        q.append(beginWord)
        seen = set()
        steps = 1
        seen.add(q[0])
        while q:
            print(q, len(q))
            for _ in range(len(q)):
                print(q)
                word = q.popleft()
                print(word)
                if word == endWord:
                    return steps
                for connection in graph[word]:
                    if connection in seen:
                        continue
                    else:
                        q.append(connection)
                        seen.add(connection)
            steps +=1
        return 0
                        
                    
                    
                    
