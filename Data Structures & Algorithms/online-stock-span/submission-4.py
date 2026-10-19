class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        self.copy = self.stack.copy()
        count = 0
        while self.copy and price >= self.copy[-1]:
            count +=1
            self.copy.pop()
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)