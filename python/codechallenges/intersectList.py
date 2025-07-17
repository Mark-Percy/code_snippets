
def longestPalindrome(s: str) -> str:
    if len(s) == 1:
        return s
    currLongest = s[0]
    for k, i in enumerate(s):
        isPal = True
        pal = i
        mid = 1
        hasChanged = True
        while isPal and hasChanged:
            hasChanged = False
            if(k - mid >= 0):
                pal = f'{s[k-mid]}{pal}'
                hasChanged = True
            
            isPal = pal == pal[::-1]
            
            if isPal and len(currLongest) < len(pal):
                currLongest = pal
                hasChanged = True
            
            if(k + mid < len(s)):
                pal = f'{pal}{s[k+mid]}'
            
            isPal = pal == pal[::-1]
            
            if isPal and len(currLongest) < len(pal):
                currLongest = pal
            mid += 1

    return currLongest

longestPalindrome('bb')