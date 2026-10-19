class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")]*n

        dist[src] = 0
        for i in range(k+1):
            dc = dist.copy()
            for edge in flights:
                start, end, price = edge
                if dc[start] == float("inf"):
                    continue
                if dc[start] + price < dist[end]:
                    dist[end] = dc[start] + price
                    print(start, end, price)
        if dist[dst] == float("inf"):
            return -1
        return dist[dst]

