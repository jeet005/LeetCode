class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if s == "":
            return True

        count = 0
        for n in t:
            if count < len(s) and s[count] == n:
                count += 1

        if count >= len(s):
            return True
        else:
            return False

        