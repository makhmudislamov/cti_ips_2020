"""
Instructions from your teacher:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

For example:
Two is written as II in Roman numeral, just two one's added together. 
Twelve is written as, XII, which is simply X + II. 
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Prompt
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.



Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

We've gone ahead and provided you a helper function- this is an idea you should match from. Breaking the problem down into smaller bits is a great tactic- rather than solving the whole problem, break it down into smaller problems!
"""
ROMAN_VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def roman_to_decimal(roman_numeral):
    output = 0
    for i in range(len(roman_numeral)-1):
        c = roman_numeral[i]
        c_next = roman_numeral[i+1]
        if ROMAN_VALUES[c] < ROMAN_VALUES[c_next]:
            output -= ROMAN_VALUES[c]
        else:
            output += ROMAN_VALUES[c]
    output = output + ROMAN_VALUES[roman_numeral[-1]]

    return output
