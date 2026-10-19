class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        req = {c: set() for word in words for c in word}
        graph = {c: set() for word in words for c in word}
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            min_len = min(len(w1), len(w2))

            if w1 > w2 and w1[:min_len] == w2[:min_len]:
                return ""
            
            for j in range(min_len):
                if not w1[j] == w2[j]:
                    req[w2[j]].add(w1[j])
                    graph[w1[j]].add(w2[j])
                    break
        
        order = []
        in_degree = {}
        q = deque()
        print(graph, req)
        for i in req: 
            if not req[i]: 
                q.append(i)
                in_degree[i] = 0
                order.append(i)
            else: 
                for _ in req[i]: 
                    in_degree[i] = in_degree.get(i, 0) +1    
                in_degree[i] = in_degree.get(i, 1)
        while q: 
            start = q.popleft()
            for depend in graph[start]:
                print(depend)
                in_degree[depend] = in_degree[depend] -1
                if in_degree[depend] == 0: 
                    q.append(depend)
                    order.append(depend)
        print(order)
        if len(order) == len(graph):
            return "".join(order)
        else: 
            return ""