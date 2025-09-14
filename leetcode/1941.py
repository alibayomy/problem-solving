"""1941. Check if All Characters Have Equal Number of Occurrences"""

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        frequency = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        last = 0
        for letter in s:
            current = frequency[ord(letter) - ord('a')]
            frequency[ord(letter) - ord('a')] = current + 1
            last = current + 1
        for f in frequency:
            if f != 0:
                if f != last:
                    return False
        return True
            
