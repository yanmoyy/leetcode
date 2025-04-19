# 901. Online Stock Span

from typing import List


class StockSpanner:

    def __init__(self):
        self.stack = []
        self.prices = []

    def next(self, price: int) -> int:
        p = self.prices
        s = self.stack
        while s and p[s[-1]] <= price:
            s.pop()
        res = len(p) - s[-1] if s else len(p) + 1
        s.append(len(p))
        p.append(price)
        return res


class StockSpanner2:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span
