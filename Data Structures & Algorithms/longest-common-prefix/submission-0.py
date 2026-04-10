class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lenghts = []
        result = ""
        for s in strs:
            lenghts.append(len(s))
        for i in range(min(lenghts)):
            for s in strs:
                if s[i] != strs[0][i]:
                    return result               
            result += strs[0][i]
        return result

            