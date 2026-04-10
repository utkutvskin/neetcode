class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ""
        for i in range(len(min(strs, key=len))):
            for s in strs:
                if s[i] != strs[0][i]:
                    return result               
            result += strs[0][i]
        return result

            