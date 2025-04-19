# 1268. Search Suggestions System

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            if len(cur.suggestions) < 3:
                # should be sorted
                cur.suggestions.append(word)

    def get_suggestions(self, word: str) -> List[str]:
        cur = self.root
        res = []
        not_found = False
        for char in word:
            if char not in cur.children:
                not_found = True
            if not_found:
                res.append([])
                continue
            cur = cur.children[char]
            res.append(cur.suggestions)
        return res


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        trie = Trie()
        products.sort()
        for product in products:
            trie.insert(product)
        return trie.get_suggestions(searchWord)
