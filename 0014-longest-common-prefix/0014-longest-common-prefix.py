class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix_ = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix_):
                prefix_ = prefix_[:-1]
                if not prefix:
                    return ""

        return prefix_