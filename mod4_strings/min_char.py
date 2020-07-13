"""
Minimum Characters required to make a String Palindromic
You are given a string. The only operation allowed is to insert characters in the beginning of the string. Return the number of characters that are needed to be inserted to make the string a palindrome string


Examples:
Input: ABC
Output: 2
Input: AACECAAAA
Output: 2
"""


def minimumCharacters(string):
    prep_arr = []
    string = list(string)
    counter = 0
    strings_last = len(string) - 1

# while prep array != reversed prep array:
    while strings_last != 0:
        # append prep arrap (last item of input string)
        prep_arr.append(string[strings_last])
        strings_last -= 1
        counter += 1
        prep_arr.extend(string)

        if prep_arr == prep_arr[::-1]:
            return counter
        else:
            prep_arr = prep_arr[:counter]
            continue

    return counter
