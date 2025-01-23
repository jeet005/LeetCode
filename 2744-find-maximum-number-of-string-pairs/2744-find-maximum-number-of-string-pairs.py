class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        hashmap = {}
        count = 0

        for word in words:
            reversed_ = word[::-1]

            if reversed_ in hashmap:
                count += 1
            else:
                hashmap[word] = 1

        return count