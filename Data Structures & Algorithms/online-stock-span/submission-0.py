class StockSpanner:

    def __init__(self):
        self.stack=[] # Each element: [price, span]
        

    def next(self, price: int) -> int:
        span=1  # While stack exists AND the top price is <= current price
        while self.stack and self.stack[-1][0]<=price:
            span+=self.stack.pop()[1]
        self.stack.append([price,span]) # Push current price and the calculated span
        return span
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)