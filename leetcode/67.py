"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            diff = len(b) - len(a)
            remains = diff * '0'
            a = remains + a
        elif len(a) > len(b):
            diff = len(a) - len(b)
            remains = diff * '0'
            b = remains + b
        constants = {
            '1+1+1': (1,1),
            '1+1+0': (0,1),
            '1+0+0': (1,0),
            '1+0+1': (0,1),
            '0+0+0': (0,0),
            '0+0+1': (1,0),
            '0+1+1': (0,1),
            '0+1+0': (1,0)
            }
        index = len(a) - 1
        carry_over = 0
        result = ''
        while index >= 0:
                next_sum,carry_over = constants[f'{carry_over}+{a[index]}+{b[index]}'][0],constants[f'{carry_over}+{a[index]}+{b[index]}'][1]
                print(next_sum)
                result = f'{next_sum}' + result
                index -= 1

        return f'{carry_over}'+ result if carry_over != 0 else  result
