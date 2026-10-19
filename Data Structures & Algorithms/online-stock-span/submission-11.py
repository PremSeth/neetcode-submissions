class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        while self.stack and price >= self.stack[-1][0]:
            print(self.stack)
            old, day = self.stack.pop()
            print(price, day)
            count += day
        self.stack.append( (price, count) )
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)