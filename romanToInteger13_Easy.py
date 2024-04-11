class Solution:
    def romanToInt(self, s: str) -> int:
        val=0
        for i in range(len(s)):
            if s[i] == 'I':
                val += 1
            elif s[i] == 'V':
                if s[i-1]=='I':
                    val = 5 - val
                else:
                    val += 5
            elif s[i] == 'X':
                if s[i-1]=='I':
                    val = 10 - val
                else:
                    val += 10
            elif s[i] == 'L':
                if s[i-1]=='X':
                    val = 50 - val
                else:
                    val += 50

            elif s[i] == 'C':
                if s[i-1]=='X':
                    val = 100 - val
                else:
                    val += 100
            elif s[i] == 'D':
                if s[i-1]=='C':
                    val = 500 - val
                else:
                    val += 500
            elif s[i] == 'M':
                if s[i-1]=='C':
                    val = 1000  - val
                else:
                    val += 1000

        return val
