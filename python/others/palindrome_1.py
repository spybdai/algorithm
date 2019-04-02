"""
Find out if a string can be made a palindrome by removing at most 1 character
function CanBePalindromized(string text) boolean
Samples
aba -> true
yxaaxay -> true
yaxaaxy -> true
abc -> false
ab -> true
"""

def can_be_palindromized(input_str):
    """
    return True or False
    """
    not_equal_left = not_equal_right = 0

    i = 0
    j = len(input_str) - 1
    while i <= j:
        if input_str[i] != input_str[j]:
            not_equal_left += 1
        else:
            i += 1
        j -= 1

    i = 0
    j = len(input_str) - 1
    while i <= j:
        if input_str[i] != input_str[j]:
            not_equal_right += 1
        else:            
            j -= 1
        i += 1

    return not_equal_left <= 1 or not_equal_right <= 1


def test_can_be_palindromized():
    strs = {
            'a': True,
            'ab': True,
            'aba': True,
            'abc': False,
            'abca': True,
            'abcb': True,
            'accd': False,
            'eabcbe': True,
            'yxaaxay': True,
            'yxaayay': False,
            'yaxaaxy': True,
            }

    for string, result in strs.items():
        print string, result is can_be_palindromized(string)

if __name__ == '__main__':
    test_can_be_palindromized()
